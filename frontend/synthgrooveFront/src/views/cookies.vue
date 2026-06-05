<template>
  <div class="legal-wrapper">
    <div class="legal-container">
      <p class="legal-seccion">Política de Cookies</p>
      <div class="separador"></div>

      <div class="legal-body">
        <section class="legal-bloque">
          <h2>1. ¿Qué son las cookies?</h2>
          <p>
            Las cookies son pequeños ficheros de texto que un sitio web almacena
            en tu navegador cuando lo visitas. Sirven para que el sitio recuerde
            tus preferencias y para facilitar la navegación en visitas
            posteriores.
          </p>
        </section>

        <section class="legal-bloque">
          <h2>2. Cookies que utilizamos</h2>
          <p>
            Synthgroove utiliza únicamente cookies técnicas y de sesión,
            estrictamente necesarias para el funcionamiento de la plataforma:
          </p>
          <ul>
            <li>
              <strong>Cookie de sesión / autenticación:</strong> almacena el
              token de acceso JWT para mantenerte identificado mientras navegas.
              Se elimina al cerrar el navegador o al cerrar sesión.
            </li>
            <li>
              <strong>Cookie de preferencias:</strong> puede guardar ajustes
              locales de la interfaz (por ejemplo, la sección activa).
            </li>
          </ul>
          <p>
            No utilizamos cookies de análisis, seguimiento publicitario ni
            redes sociales de terceros.
          </p>
        </section>

        <section class="legal-bloque">
          <h2>3. Cookies de terceros</h2>
          <p>
            El reproductor integrado de <strong>SoundCloud</strong> (iframes en
            las páginas de Releases y Podcasts) puede instalar sus propias
            cookies técnicas para gestionar la reproducción. Consulta la
            <a href="https://soundcloud.com/pages/privacy" target="_blank" rel="noopener">
              política de privacidad de SoundCloud
            </a>
            para más información.
          </p>
          <p>
            El servicio de pagos <strong>Stripe</strong> puede utilizar cookies
            propias durante el proceso de compra. Consulta la
            <a href="https://stripe.com/es/privacy" target="_blank" rel="noopener">
              política de privacidad de Stripe
            </a>.
          </p>
        </section>

        <section class="legal-bloque">
          <h2>4. Cómo gestionar las cookies</h2>
          <p>
            Puedes configurar tu navegador para bloquear o eliminar cookies.
            Ten en cuenta que deshabilitar las cookies técnicas puede impedir el
            correcto funcionamiento de la plataforma (inicio de sesión, compras,
            etc.).
          </p>
          <ul>
            <li>
              <a href="https://support.google.com/chrome/answer/95647" target="_blank" rel="noopener">Chrome</a>
            </li>
            <li>
              <a href="https://support.mozilla.org/es/kb/habilitar-y-deshabilitar-cookies-sitios-web-rastrear-preferencias" target="_blank" rel="noopener">Firefox</a>
            </li>
            <li>
              <a href="https://support.apple.com/es-es/guide/safari/sfri11471/mac" target="_blank" rel="noopener">Safari</a>
            </li>
          </ul>
        </section>

        <section class="legal-bloque">
          <h2>5. Cambios en esta política</h2>
          <p>
            Podemos actualizar esta política si incorporamos nuevos servicios que
            impliquen el uso de cookies adicionales. Te informaremos de los
            cambios relevantes.
          </p>
          <p class="legal-fecha">Última actualización: junio de 2025</p>
        </section>
      </div>
    </div>
  </div>
</template>

<style scoped>
.legal-wrapper {
  width: 100%;
  background: #000;
  padding: 3rem 1.5rem 4rem;
}

.legal-container {
  max-width: 720px;
  margin: 0 auto;
}

.legal-seccion {
  font-size: 0.75rem;
  letter-spacing: 0.3em;
  text-transform: uppercase;
  color: #666;
  margin: 0 0 1rem;
}

.separador {
  width: 100%;
  height: 1px;
  background: #222;
  margin-bottom: 2.5rem;
}

.legal-body {
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.legal-bloque h2 {
  font-size: 0.72rem;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: #666;
  margin: 0 0 0.75rem;
  font-weight: 600;
}

.legal-bloque p,
.legal-bloque li {
  font-size: 0.92rem;
  color: #aaa;
  line-height: 1.75;
  margin: 0 0 0.5rem;
}

.legal-bloque ul {
  padding-left: 1.25rem;
  margin: 0.25rem 0 0.5rem;
}

.legal-bloque a {
  color: #f7f1e8;
  text-decoration: none;
  border-bottom: 1px solid #333;
  transition: border-color 0.2s;
}

.legal-bloque a:hover {
  border-bottom-color: #f7f1e8;
}

.legal-fecha {
  color: #444 !important;
  font-size: 0.78rem !important;
  margin-top: 0.5rem !important;
}

@media (max-width: 640px) {
  .legal-wrapper {
    padding: 2rem 1rem 3rem;
  }
}
</style>
