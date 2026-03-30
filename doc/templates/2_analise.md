# Análise: Requirimentos do sistema
## Descrición xeral

Queremos crear una página web que esté viva y sea útil para un grupo de música electrónica. Esta página web debe reunir toda la información sobre los artistas, los lanzamientos de música y los podcasts, las ventas de productos y los eventos. La página web será como un catálogo que se puede usar de manera interactiva y será un lugar donde la comunidad se pueda reunir. Para hacer esto, habrá un sistema de suscripción.


## Requirimentos

Requerimientos funcionales:

    -La web deberá mostrar información corporativa del colectivo
    -Mostrará la información de los artistas junto a la imagen más el nombre artístico de estos
    -Mostrara releases y podcast musicales permitiendo su reproduccion desde el navegador
    -Mostrará los próximos eventos junto a un enlace que permitira la compra de estas entradas
    -Permitirá la visualización de los productos junto con el precio y el nombre de estos
    -Cada producto dispondrá de un botón para reservar mediante un mensaje predeterminado al WhatsApp de la empresa.
    -Permitirá la opción de registrarse en la newsletter para obtener beneficios
    -Se incluirá un sistema de búsqueda y/o filtrado para facilitar la localización de artistas, eventos o productos.
    -Se implementará un sistema de autenticación para administradores, permitiendo el acceso mediante login a un panel restringido.
    -Los usuarios administradores podrán crear, editar y eliminar artistas y sets/releases desde un panel de gestión.
    -El sistema de administración permitirá la gestión completa de contenidos (artistas, eventos, productos y releases) mediante operaciones CRUD.
    
    
Requerimientos no funcionales:

    -La web deberá ser intuitiva y facil de navegar en ella
    -La web tendrá un diseño responsive que se adaptará a los distintos dispositivos electrónicos
    -Los datos de los usuarios registrados deberán almacenarse de forma segura
    -Tendrá que estar disponible 24/7

## Tipos de usuarios

Contara con 4 roles de usuario:

<strong>Visitantes</strong>:
Los visitantes solo pueden leer la información de la plataforma. Pueden mirar la página de inicio, leer la biografía de los artistas, ver el catálogo de merchandising y escuchar los podcasts o releases que están disponibles.

<strong>Suscriptores(newsletter)</strong>:
Los suscriptores son usuarios que se han registrado en la plataforma. Gracias a esto, pueden acceder a ventajas especiales, recibir noticias personalizadas del colectivo y participar en la comunidad de manera interactiva.

<strong>Gestor</strong>:
El usuario gestor es un usuario registrado en la aplicación que, tras iniciar sesión, puede gestionar el contenido de la plataforma a través de un panel interno. Aunque tiene permisos para crear, editar y eliminar información, no tiene acceso al código ni a la base de datos a nivel técnico.

<strong>Administrador</strong>:
El administrador es el que tiene control total sobre la plataforma. Puede gestionar la base de datos, agregar nuevos artistas, actualizar la ropa que se vende, programar eventos y supervisar la lista de suscriptores.