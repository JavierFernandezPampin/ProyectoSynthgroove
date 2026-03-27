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
    int id PK
    string nombre
    string descripcion
    string imagen
}

RELEASES {
    int id PK
    string titulo
    string url
    string imagen
    date fecha_release
    int artistas_id
}

PODCASTS {
    int id PK
    string title
    string url
    string imagen
    date fecha_release
    int artistas_id
}

EVENTOS {
    int id PK
    string nombre
    string localizacion
    date fecha_release
    string imagen
}

PRODUCTOS {
    int id PK
    string nombre
    float precio
    string imagen
    string categoria
}

USUARIOS {
    int id PK
    string mail
    string contrasena
    string tipo
}

ARTISTAS ||--o{ RELEASES : tienen
ARTISTAS ||--o{ PODCASTS : tienen

USUARIOS ||--o{ ARTISTAS : crean_modifican
USUARIOS ||--o{ RELEASES : crean_modifican
USUARIOS ||--o{ PODCASTS : crean_modifican
USUARIOS ||--o{ EVENTOS : crean_modifican
USUARIOS ||--o{ PRODUCTOS : crean_modifican
```