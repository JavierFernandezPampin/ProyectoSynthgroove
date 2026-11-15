$ErrorActionPreference = "Stop"

function New-RandomHex {
    param([int]$ByteCount)

    $bytes = New-Object byte[] $ByteCount
    $generator = [System.Security.Cryptography.RandomNumberGenerator]::Create()
    try {
        $generator.GetBytes($bytes)
    }
    finally {
        $generator.Dispose()
    }

    return ([BitConverter]::ToString($bytes) -replace "-", "").ToLowerInvariant()
}

function Test-LocalPort {
    param([int]$Port)

    $client = New-Object System.Net.Sockets.TcpClient
    try {
        $connection = $client.BeginConnect("127.0.0.1", $Port, $null, $null)
        if (-not $connection.AsyncWaitHandle.WaitOne(1000)) {
            return $false
        }

        $client.EndConnect($connection)
        return $true
    }
    catch {
        return $false
    }
    finally {
        $client.Close()
    }
}

$docker = Get-Command docker -ErrorAction SilentlyContinue
if (-not $docker) {
    $winget = Get-Command winget -ErrorAction SilentlyContinue
    if (-not $winget) {
        throw "Docker no esta instalado y no se encontro winget. Instala App Installer desde Microsoft Store y vuelve a ejecutar este script."
    }

    Write-Host "Docker no esta instalado. Instalando Docker Desktop con winget..."
    & winget install --id Docker.DockerDesktop --exact --source winget --accept-source-agreements --accept-package-agreements --silent --disable-interactivity
    if ($LASTEXITCODE -ne 0) {
        throw "No se pudo instalar Docker Desktop. Puede que necesites permisos de administrador o instalarlo manualmente desde https://www.docker.com/products/docker-desktop/."
    }

    $env:Path = [Environment]::GetEnvironmentVariable("Path", "Machine") + ";" +
        [Environment]::GetEnvironmentVariable("Path", "User")
    $docker = Get-Command docker -ErrorAction SilentlyContinue
    if (-not $docker) {
        $dockerDirectory = Join-Path $env:ProgramFiles "Docker\Docker\resources\bin"
        if (Test-Path (Join-Path $dockerDirectory "docker.exe")) {
            $env:Path = $dockerDirectory + ";" + $env:Path
            $docker = Get-Command docker -ErrorAction SilentlyContinue
        }
    }

    if (-not $docker) {
        throw "Docker Desktop se instalo, pero no se encontro docker.exe en el PATH. Reinicia PowerShell y vuelve a ejecutar este script."
    }
}

$dockerDesktopCandidates = @(
    (Join-Path $env:ProgramFiles "Docker\Docker\Docker Desktop.exe"),
    (Join-Path $env:LOCALAPPDATA "Programs\Docker\Docker\Docker Desktop.exe")
)
$dockerDesktop = $dockerDesktopCandidates |
    Where-Object { Test-Path $_ } |
    Select-Object -First 1

& docker info *> $null
if ($LASTEXITCODE -ne 0 -and $dockerDesktop) {
    Write-Host "Iniciando Docker Desktop..."
    Start-Process -FilePath $dockerDesktop
}

$dockerDeadline = (Get-Date).AddMinutes(5)
while ((Get-Date) -lt $dockerDeadline) {
    & docker info *> $null
    if ($LASTEXITCODE -eq 0) {
        break
    }

    Start-Sleep -Seconds 5
}

if ($LASTEXITCODE -ne 0) {
    throw "El motor de Docker no esta disponible. Abre Docker Desktop; si solicita reiniciar, habilitar WSL 2 o aceptar sus terminos, completa ese paso y vuelve a ejecutar este script."
}

Set-Location $PSScriptRoot
$envFile = Join-Path $PSScriptRoot ".env"
if (-not (Test-Path $envFile)) {
    $secretKey = New-RandomHex -ByteCount 32
    $databasePassword = New-RandomHex -ByteCount 24
    $environment = @(
        "DJANGO_SECRET_KEY=$secretKey"
        "DJANGO_DEBUG=False"
        "DB_NAME=synthgroove"
        "DB_USER=synthgroove"
        "DB_PASSWORD=$databasePassword"
        "DB_PORT=3306"
        "CLOUDINARY_CLOUD_NAME="
        "CLOUDINARY_API_KEY="
        "CLOUDINARY_API_SECRET="
        "STRIPE_SECRET_KEY="
        "STRIPE_PUBLISHABLE_KEY="
        "STRIPE_WEBHOOK_SECRET="
        "FRONTEND_URL=http://localhost:5173"
    )
    Set-Content -Path $envFile -Value $environment -Encoding ascii
    Write-Host "Se creo .env con credenciales aleatorias para esta instalacion."
}
else {
    Write-Host "Se usará el .env existente sin modificarlo."
}

Write-Host "Construyendo e iniciando Synthgroove..."
& docker compose up --build --detach
if ($LASTEXITCODE -ne 0) {
    & docker compose logs --tail 80
    throw "No se pudieron iniciar los servicios. Revisa los logs mostrados arriba."
}

$deadline = (Get-Date).AddMinutes(3)
while ((Get-Date) -lt $deadline) {
    if ((Test-LocalPort -Port 5173) -and (Test-LocalPort -Port 8000)) {
        Write-Host ""
        Write-Host "Synthgroove esta disponible:"
        Write-Host "  Frontend:  http://localhost:5173"
        Write-Host "  Backend:   http://localhost:8000"
        Write-Host "  phpMyAdmin: http://localhost:8080"
        exit 0
    }

    Start-Sleep -Seconds 3
}

& docker compose ps
& docker compose logs --tail 80
throw "Los servicios no quedaron listos en 3 minutos. Revisa los logs mostrados arriba."
