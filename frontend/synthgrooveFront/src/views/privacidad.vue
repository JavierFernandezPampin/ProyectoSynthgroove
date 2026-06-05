<template>
  <div class="legal-wrapper">
    <div class="legal-container">
      <p class="legal-seccion">Política de Privacidad</p>
      <div class="separador"></div>

      <div class="legal-body">
        <section class="legal-bloque">
          <h2>1. Responsable del tratamiento</h2>
          <p>
            El responsable del tratamiento de los datos personales recogidos en
            este sitio web es <strong>Synthgroove Collective</strong>, con
            dirección de contacto en
            <a href="mailto:info@synthgroove.com">info@synthgroove.com</a>.
          </p>
        </section>

        <section class="legal-bloque">
          <h2>2. Datos que recogemos</h2>
          <p>
            Al registrarte en nuestra plataforma, recogemos los siguientes datos
            personales:
          </p>
          <ul>
            <li>Nombre de usuario</li>
            <li>Dirección de correo electrónico</li>
            <li>Nombre y apellido (opcionales)</li>
            <li>Contraseña (almacenada de forma cifrada)</li>
          </ul>
          <p>
            Cuando realizas una compra, los datos de pago son procesados
            directamente por <strong>Stripe</strong>; Synthgroove no almacena
            datos de tarjetas bancarias.
          </p>
        </section>

        <section class="legal-bloque">
          <h2>3. Finalidad del tratamiento</h2>
          <p>Los datos recogidos se utilizan exclusivamente para:</p>
          <ul>
            <li>Gestionar tu cuenta de usuario y autenticación.</li>
            <li>Procesar pedidos de merchandising y reservas de eventos.</li>
            <li>Enviarte comunicaciones relacionadas con tus compras.</li>
          </ul>
        </section>

        <section class="legal-bloque">
          <h2>4. Base legal</h2>
          <p>
            El tratamiento de tus datos se basa en la ejecución de la relación
            contractual derivada del registro y uso de la plataforma
            (art. 6.1.b RGPD) y, en su caso, en el consentimiento explícito que
            nos otorgues.
          </p>
        </section>

        <section class="legal-bloque">
          <h2>5. Conservación de los datos</h2>
          <p>
            Tus datos se conservan mientras mantengas una cuenta activa. Si
            solicitas la eliminación de tu cuenta, procederemos a su supresión
            en un plazo máximo de 30 días, salvo obligación legal de
            conservación.
          </p>
        </section>

        <section class="legal-bloque">
          <h2>6. Tus derechos</h2>
          <p>
            Conforme al RGPD y la LOPDGDD, puedes ejercer en cualquier momento
            los derechos de acceso, rectificación, supresión, portabilidad,
            limitación del tratamiento y oposición escribiendo a
            <a href="mailto:info@synthgroove.com">info@synthgroove.com</a>. Si
            consideras que el tratamiento no se ajusta a la normativa, puedes
            presentar una reclamación ante la
            <strong>Agencia Española de Protección de Datos</strong>
            (www.aepd.es).
          </p>
        </section>

        <section class="legal-bloque">
          <h2>7. Transferencias internacionales</h2>
          <p>
            Algunos servicios de terceros (Stripe, proveedores de
            infraestructura) pueden tratar datos fuera del Espacio Económico
            Europeo. Dichas transferencias se realizan bajo las garantías
            adecuadas previstas en el RGPD (cláusulas contractuales tipo,
            decisiones de adecuación, etc.).
          </p>
        </section>

        <section class="legal-bloque">
          <h2>8. Cambios en esta política</h2>
          <p>
            Podemos actualizar esta política para reflejar cambios normativos o
            de negocio. Te notificaremos cualquier cambio relevante a través del
            correo asociado a tu cuenta.
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
