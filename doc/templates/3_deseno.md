# Diseño

## Esquema (boceto o wireframe).

https://app.mockflow.com/view/Mb6449180842d0cff1bbe658e1386800a1773158697960

## Identidad visual 

![alt text](image.png)

El azul es el color principal. El negro también es importante porque representa la parte oscura y industrial de la música techno. El blanco se utiliza para crear contraste con los fondos oscuros. La fuente que se usa se llama Outfit. Esta fuente es moderna, limpia y digital, lo que va muy bien con la estética del proyecto.


## Diagrama de Bases de Datos

```mermaid
erDiagram

ARTISTAS {
    int id PK auto_increment
    string nombre
    string descripcion
    string imagen
}

RELEASES {
    int id PK auto_increment
    string titulo
    string url
    string imagen
    date fecha_release
    int artistas_id FK
}

PODCASTS {
    int id PK auto_increment
    string title
    string url
    string imagen
    date fecha_release
    int artistas_id FK
}

EVENTOS {
    int id PK auto_increment
    string nombre
    string localizacion
    date fecha_release
    string imagen
}

PRODUCTOS {
    int id PK auto_increment
    string nombre
    float precio
    string imagen
    string categoria
}

USUARIOS{
    int id PK auto_increment
    string mail
    string contraseña
    string tipo
}

ARTISTS ||--o{ RELEASES : tienen
ARTISTS ||--o{ PODCASTS : tienen
```