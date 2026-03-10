# Estudo preliminar - Anteproxecto

## Descrición do proxecto

El presente proyecto consiste en el diseño y desarrollo de una aplicación web para un colectivo
de música electrónica, con el objetivo de centralizar su presencia digital y mejorar la
comunicación con su público.

La aplicación permitirá mostrar información corporativa del colectivo, presentar a sus artistas,
anunciar los próximos eventos y ofrecer merchandising oficial.

### Xustificación do proxecto.

El objetivo principal es crear una web oficial que permita centralizar la información del
colectivo, mejorar su imagen profesional y facilitar el acceso a datos sobre artistas, próximos
eventos y merchandising. De esta manera, se busca reforzar su identidad de marca y ofrecer un
canal de comunicación más directo y organizado con su público.


### Funcionalidades do proxecto.

La aplicación reunirá la identidad del grupo. Permitirá a los usuarios escuchar música en vivo, gestionar la compra de entradas para eventos, explorar o comprar en el catálogo de productos y suscribirse a contenido exclusivo.


### Estudo de necesidades. Proposta de valor respecto ao que hai no mercado.

Este proyecto surge de la necesidad del colectivo de música electrónica de disponer de una
página web propia y centralizada. Hasta el momento, el colectivo no contaba con una plataforma
donde se pudiera encontrar toda la información reunida en un único espacio, dependiendo
únicamente de redes sociales para difundir artistas, eventos y novedades.

### Persoas destinatarias.

La aplicación está dirigida principalmente a personas aficionadas a la música electrónica,
seguidores del colectivo y público interesado en asistir a sus eventos o adquirir su
merchandising. Por tanto, el público objetivo está formado principalmente por personas jóvenes
y adultas interesadas en la cultura musical electrónica.

### Promoción.

Principalmente promocionaremos nuestra página web a través de nuestra cuenta de Instagram, donde se concentra la mayor parte de nuestra comunidad y contamos con un alto nivel de interacción.

Además, lanzaremos una newsletter dirigida a nuestros seguidores más fieles, con el objetivo de mantenerlos informados de manera exclusiva y anticipada sobre nuestras novedades, lanzamientos y promociones especiales. 

### Modelo de negocio.

En primer lugar, la página web funcionará como plataforma oficial para la venta de merchandising, permitiendo obtener ingresos directos mediante la comercialización de productos como camisetas, sudaderas u otros artículos personalizados del colectivo.

En segundo lugar, la web servirá como canal de promoción y redirección hacia la venta de entradas para eventos, generando ingresos indirectos a través de la organización de fiestas y actuaciones. En caso de que el colectivo actúe como organizador, los beneficios procederán directamente de la venta de entradas.

Tambien tendremos contenidos exclusivos o membresías para los seguidores que se registren en nuestra newsletter (por ejemplo, acceso anticipado a entradas, descuentos en merchandising o contenido exclusivo), reforzando así la fidelización del público.

## Requirimentos

La infraestructura del proyecto se basará en Hostinger y utilizará una base de datos MySQL para gestionar toda la información de forma relacional. La web no almacenará archivos de audio pesados, sino que funcionará como una plataforma de gestión que incorpora los reproductores externos de distintas webs mediante enlaces, lo que garantiza rapidez y estabilidad.

En el Backend, vamos a utilizar Python como lenguaje de programación y el framework Django. Usaremos Class-Based Views en Django. Para identificar y mantener las sesiones de los usuarios, emplearemos el motor de Sessions de Django.
La seguridad del sitio es muy importante. Por eso, vamos a reforzarla con CSRF tokens en los formularios.De esta manera, podemos garantizar que la información de los usuarios esté protegida.

El frontend se desarrollará con Vue.js 3. Para el diseño y la estética visual de la interfaz, se utilizarán hojas de estilo CSS. De esta manera, se logrará un aspecto moderno y profesional, totalmente adaptable a dispositivos móviles.

