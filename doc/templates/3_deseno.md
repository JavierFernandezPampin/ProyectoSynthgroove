# Deseño

## Esquema (boceto ou wireframe).
 
## Identidade visual 

## Diagrama de Bases de Datos

erDiagram

ARTISTS {

    int id PK
    string name
    string description
}

RELEASES {

    int id PK
    string title
    string url
    int artist_id FK
}

PODCASTS {

    int id PK
    string title
    string url
    int artist_id FK
}

EVENTS {

    int id PK
    string name
    string location
    date event_date
}

CATEGORIES {

    int id PK
    string name
}

PRODUCTS {

    int id PK
    string name
    float price
    int category_id FK
}

NEWSLETTER {
    
    int id PK
    string email
}

ARTISTS ||--o{ RELEASES : creates

ARTISTS ||--o{ PODCASTS : creates

CATEGORIES ||--o{ PRODUCTS : contains