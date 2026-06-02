# API Reference

Esta referencia resume los endpoints principales disponibles en el backend de Synthgroove.

Base URL en desarrollo:

```text
http://localhost:8000
```

## Autenticación

La API usa JWT para las operaciones autenticadas. Cuando un endpoint requiere autenticación, debe enviarse:

```http
Authorization: Bearer <access_token>
```

## Endpoints públicos principales

### Artistas

- `GET /api/artistas/`
- `POST /api/artistas/`  
  Requiere permisos de gestor o administrador.

### Eventos

- `GET /api/eventos/`
- `POST /api/eventos/`  
  Requiere permisos de gestor o administrador.
- `GET /api/eventos/<id>/`
- `PUT /api/eventos/<id>/`
- `DELETE /api/eventos/<id>/`  
  Edición y borrado con permisos de gestor o administrador.

### Productos

- `GET /api/productos/`
- `POST /api/productos/`  
  Requiere permisos de gestor o administrador.

### Releases

- `GET /api/releases/`
- `POST /api/releases/`  
  Requiere permisos de gestor o administrador.

### Podcasts

- `GET /api/podcasts/`
- `POST /api/podcasts/`  
  Requiere permisos de gestor o administrador.

## Endpoints de usuario

### Registro

`POST /api/auth/register/`

Ejemplo de cuerpo:

```json
{
  "mail": "usuario@ejemplo.com",
  "usuario": "usuario_demo",
  "password": "contrasena123"
}
```

Respuesta esperada:

```json
{
  "access": "jwt_access_token",
  "refresh": "jwt_refresh_token",
  "usuario": "usuario_demo",
  "rol": "suscriptor"
}
```

### Inicio de sesión

`POST /api/auth/login/`

Ejemplo de cuerpo:

```json
{
  "mail": "usuario@ejemplo.com",
  "password": "contrasena123"
}
```

### Cierre de sesión

`POST /api/auth/logout/`

Ejemplo de cuerpo:

```json
{
  "refresh": "jwt_refresh_token"
}
```

### Renovación de token

`POST /api/auth/refresh/`

Ejemplo de cuerpo:

```json
{
  "refresh": "jwt_refresh_token"
}
```

## Pagos con Stripe

### Crear sesión de pago

`POST /api/pago/stripe/`

Este endpoint admite tanto usuarios autenticados como no autenticados. Si el usuario está autenticado, el backend puede aplicar el descuento configurado.

Ejemplo de cuerpo:

```json
{
  "tipo": "producto",
  "id": 1,
  "cantidad": 1
}
```

Valores admitidos para `tipo`:

- `producto`
- `evento`

Respuesta esperada:

```json
{
  "checkout_url": "https://checkout.stripe.com/..."
}
```

### Webhook de Stripe

`POST /api/webhook/`

Este endpoint está pensado para el uso interno de Stripe y actualiza el estado de los pagos completados.

## Notas

- Los métodos `GET` de consulta son públicos.
- Los métodos `POST`, `PUT` y `DELETE` de gestión de contenido están restringidos por permisos.
- La estructura exacta de los objetos devueltos depende de los serializers del backend, especialmente en el caso de artistas, eventos y productos.
