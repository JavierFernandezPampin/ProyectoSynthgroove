<template>
  <div class="legal-wrapper">
    <div class="legal-container">
      <p class="legal-seccion">Aviso Legal</p>
      <div class="separador"></div>

      <div class="legal-body">
        <section class="legal-bloque">
          <h2>1. Datos identificativos</h2>
          <p>
            En cumplimiento del artículo 10 de la Ley 34/2002, de Servicios de
            la Sociedad de la Información y Comercio Electrónico (LSSI-CE), se
            informa de los siguientes datos:
          </p>
          <ul>
            <li><strong>Denominación:</strong> Synthgroove Collective</li>
            <li>
              <strong>Correo electrónico:</strong>
              <a href="mailto:synthgroove@gmail.com">synthgroove@gmail.com</a>
            </li>
          </ul>
        </section>

        <section class="legal-bloque">
          <h2>2. Objeto y ámbito de aplicación</h2>
          <p>
            El presente Aviso Legal regula el acceso, navegación y uso del sitio
            web <strong>synthgroove.com</strong> (en adelante, «el sitio»).
            El acceso al sitio implica la aceptación plena y sin reservas de
            todas las disposiciones incluidas en este Aviso Legal.
          </p>
        </section>

        <section class="legal-bloque">
          <h2>3. Propiedad intelectual e industrial</h2>
          <p>
            Todos los contenidos del sitio web —incluyendo textos, imágenes,
            logotipos, diseño gráfico, código fuente y elementos audiovisuales—
            son propiedad de Synthgroove Collective o de terceros que han
            autorizado su uso, y están protegidos por la legislación española e
            internacional sobre propiedad intelectual e industrial.
          </p>
          <p>
            Queda prohibida la reproducción, distribución, comunicación pública
            o transformación de dichos contenidos sin autorización expresa y por
            escrito de Synthgroove Collective, salvo para uso privado.
          </p>
        </section>

        <section class="legal-bloque">
          <h2>4. Responsabilidad</h2>
          <p>
            Synthgroove Collective no se hace responsable de los daños o
            perjuicios que pudieran derivarse de:
          </p>
          <ul>
            <li>Interrupciones o fallos técnicos del sitio.</li>
            <li>
              Contenidos de terceros enlazados desde este sitio web (redes
              sociales, reproductores externos, etc.).
            </li>
            <li>
              El uso indebido del sitio por parte de los usuarios.
            </li>
          </ul>
        </section>

        <section class="legal-bloque">
          <h2>5. Legislación aplicable y jurisdicción</h2>
          <p>
            Las presentes condiciones se rigen por la legislación española. Para
            la resolución de cualquier conflicto derivado del acceso o uso de
            este sitio, las partes se someten a los juzgados y tribunales del
            domicilio del usuario, salvo que la ley disponga otro fuero
            imperativo.
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
