# Synthgroove

Synthgroove es una aplicación web para centralizar la presencia digital de un colectivo de música electrónica. La idea era reunir en un solo sitio todo lo importante: el colectivo, los artistas, releases, podcasts, eventos y merchandising, sin depender solo de las redes sociales y con una imagen más profesional.

El frontend está hecho con Vue 3 y el backend con Django REST Framework. Incluye registro e inicio de sesión, roles de usuario, compra de merchandising y entradas mediante Stripe, y descuentos para usuarios registrados.

## Instalación

### Con Docker (recomendado)

Desde la raíz del proyecto:

```bash
docker compose up --build
```

Una vez arrancado:

- Frontend: `http://localhost:5173`
- Backend: `http://localhost:8000`
- phpMyAdmin: `http://localhost:8080`

El backend aplica las migraciones automáticamente al iniciarse.

### Manual

Backend:

```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Frontend:

```bash
cd frontend/synthgrooveFront
npm install
npm run dev
```

## Tecnologías

- Frontend: Vue 3, Vue Router, Pinia, Vite, TypeScript
- Backend: Django, Django REST Framework, Simple JWT
- Base de datos: MySQL
- Media: Cloudinary
- Pagos: Stripe
- Contenerización: Docker y Docker Compose

## Uso

- El enlace es synthgroove.es

- La parte pública es accesible sin cuenta.
- Para probar el registro, inicio de sesión y descuentos, puedes crear una cuenta desde `/registro`.
- Para probar compras, el merchandising y los eventos son accesibles desde la navegación pública con el numero de cuenta: 4242 4242 4242 4242 y cualquier credencial.

- API: `http://localhost:8000`
- Repositorio: `https://gitlab.iessanclemente.net/dawo/a25javierfp`

## Sobre mí

- Mis principales fortalezas, y también aquello que más me apasiona, están relacionadas con el desarrollo frontend. Disfruto especialmente de todo lo que implica la personalización y el diseño de sitios web, ya que me permite crear experiencias visuales atractivas y adaptadas a las necesidades de los usuarios.

- Uno de los principales motivos para llevar a cabo este proyecto fue la necesidad de reducir nuestra dependencia de diferentes redes sociales para darnos a conocer. Gracias a esta plataforma, hemos conseguido centralizar nuestras operaciones y mejorar la gestión de nuestra presencia digital.

- Para cualquier consulta o contacto, podéis escribirme al siguiente correo electrónico: [a25javierfp@iessanclemente.net](mailto:a25javierfp@iessanclemente.net).

## Licencia

- Este proyecto está distribuido bajo la licencia MIT. Consulta el archivo `LICENSE` para más información.

## Contribución

- Contribuciones bienvenidas: añade funcionalidades, corrige o optimiza código, crea tests automatizados, documenta la API o integra nuevos servicios. Haz un issue con tu propuesta y envía un pull request con los cambios.

## Memoria

1. [Estudio preliminar](doc/templates/1_estudo_preliminar.md)
2. [Análisis](doc/templates/2_analise.md)
3. [Diseño](doc/templates/3_deseno.md)
4. [Planificación y presupuesto](doc/templates/a3_orzamento.md)
5. [Codificación y pruebas](doc/templates/4_codificacion_probas.md)
6. [Futuro y comercialización](doc/templates/5_manuais.md)
