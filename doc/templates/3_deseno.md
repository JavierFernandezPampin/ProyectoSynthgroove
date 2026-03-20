# Diseño

## Esquema (boceto o wireframe).

https://app.mockflow.com/view/Mb6449180842d0cff1bbe658e1386800a1773158697960

## Identidad visual 

![alt text](image.png)

El azul es el color principal. El negro también es importante porque representa la parte oscura y industrial de la música techno. El blanco se utiliza para crear contraste con los fondos oscuros. La fuente que se usa se llama Outfit. Esta fuente es moderna, limpia y digital, lo que va muy bien con la estética del proyecto.


## Diagrama de Bases de Datos

erDiagram

ARTISTS {
    int id PK
    string name
    string description
    string image
}

RELEASES {
    int id PK
    string title
    string url
    string image
    date release_date
    int artist_id FK
}

PODCASTS {
    int id PK
    string title
    string url
    string image
    date release_date
    int artist_id FK
}

EVENTS {
    int id PK
    string name
    string location
    date event_date
    string image
}

CATEGORIES {
    int id PK
    string name
}

PRODUCTS {
    int id PK
    string name
    float price
    string image
    int category_id FK
}

NEWSLETTER {
    int id PK
    string email
}

ARTISTS ||--o{ RELEASES : creates
ARTISTS ||--o{ PODCASTS : creates
CATEGORIES ||--o{ PRODUCTS : contains