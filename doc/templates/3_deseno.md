# Deseño

## Esquema (boceto ou wireframe).

https://app.mockflow.com/wire/Mb6449180842d0cff1bbe658e1386800a1773158697960#/page/874188fae98e4c52b423ba445942a2f0/mode/design
 
## Identidade visual 

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