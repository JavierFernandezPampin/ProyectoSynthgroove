<template>
  <footer class="footer">
    <div class="footer-wrapper">
      <div class="separador"></div>

      <div class="footer-content">
        <!-- Redes sociales -->
        <div class="footer-social">
          <a
            href="https://www.instagram.com/synthgroove.collect/_"
            target="_blank"
            class="social-link"
          >
            <!-- Instagram -->
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="20"
              height="20"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              stroke-width="1.5"
            >
              <rect x="2" y="2" width="20" height="20" rx="5" ry="5" />
              <circle cx="12" cy="12" r="4" />
              <circle
                cx="17.5"
                cy="6.5"
                r="1"
                fill="currentColor"
                stroke="none"
              />
            </svg>
            Instagram
          </a>
          <a
            href="https://soundcloud.com/synthgroove"
            target="_blank"
            class="social-link"
          >
            <!-- Soundcloud -->
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="20"
              height="20"
              viewBox="0 0 24 24"
              fill="currentColor"
            >
              <path
                d="M1.175 12.225c-.042 0-.08.03-.083.072l-.445 3.902.445 3.77c.003.04.041.072.083.072.04 0 .077-.03.08-.072l.504-3.77-.504-3.902c-.003-.042-.04-.072-.08-.072zm1.57-.9c-.05 0-.09.037-.094.085l-.38 4.787.38 4.6c.004.05.044.085.094.085.048 0 .088-.036.092-.085l.43-4.6-.43-4.787c-.004-.048-.044-.085-.092-.085zm1.59-.4c-.057 0-.104.045-.107.1l-.32 5.187.32 4.43c.003.057.05.1.107.1.056 0 .102-.043.106-.1l.362-4.43-.362-5.187c-.004-.055-.05-.1-.106-.1zm1.59-.2c-.065 0-.118.052-.12.116l-.26 5.387.26 4.26c.002.064.055.116.12.116.064 0 .116-.052.12-.116l.295-4.26-.295-5.387c-.004-.064-.056-.116-.12-.116zm1.6-.1c-.072 0-.13.058-.133.13l-.2 5.487.2 4.09c.003.072.061.13.133.13.07 0 .128-.058.132-.13l.228-4.09-.228-5.487c-.004-.072-.062-.13-.132-.13zm1.59.1c-.08 0-.145.065-.147.144l-.14 5.387.14 3.92c.002.08.067.144.147.144.08 0 .144-.064.147-.144l.16-3.92-.16-5.387c-.003-.08-.067-.144-.147-.144zm1.6-.2c-.087 0-.157.07-.16.157l-.08 5.587.08 3.75c.003.087.073.157.16.157.086 0 .156-.07.158-.157l.092-3.75-.092-5.587c-.002-.087-.072-.157-.158-.157zm1.59-.4c-.095 0-.172.077-.174.172l-.02 5.987.02 3.58c.002.095.079.172.174.172.094 0 .17-.077.173-.172l.023-3.58-.023-5.987c-.003-.095-.079-.172-.173-.172zm1.59.6c-.1 0-.182.082-.184.183v5.587l.184 3.41c.002.1.084.183.184.183.1 0 .18-.083.183-.183l.208-3.41-.208-5.587c-.003-.1-.083-.183-.183-.183zm4.17-3.8c-.23-.087-.476-.134-.732-.134-1.173 0-2.13.87-2.248 1.99-.06.003-.118.01-.175.018v9.337c.057.006.114.01.175.01h6.79c.9 0 1.63-.73 1.63-1.63 0-.9-.73-1.63-1.63-1.63-.09 0-.177.008-.263.022.04-.178.062-.363.062-.553 0-1.46-1.183-2.643-2.643-2.643-.36 0-.703.072-1.016.203z"
              />
            </svg>
            Soundcloud
          </a>
        </div>

        <!-- Legal -->
        <div class="footer-legal">
          <a href="/privacidad" class="legal-link">Política de privacidad</a>
          <span class="dot">·</span>
          <a href="/cookies" class="legal-link">Política de cookies</a>
          <span class="dot">·</span>
          <a href="/aviso-legal" class="legal-link">Aviso legal</a>
        </div>

        <!-- Copyright -->
        <p class="footer-copy">
          © {{ new Date().getFullYear() }} Synthgroove. Todos los derechos
          reservados.
        </p>
      </div>
    </div>
  </footer>
</template>

<style>
.footer {
  background-color: black;
  padding: 0 1.5rem 2rem;
}

.footer-wrapper {
  max-width: 960px;
  margin: 0 auto;
}

.footer-content {
  display: flex;
  flex-direction: column;
  gap: 1.25rem;
  padding-top: 1.5rem;
}

.footer-social {
  display: flex;
  gap: 2rem;
}

.social-link {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  color: #666;
  text-decoration: none;
  font-size: 0.75rem;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  transition: color 0.2s;
}

.social-link:hover {
  color: #f7f1e8;
}

.footer-legal {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  flex-wrap: wrap;
}

.legal-link {
  color: #444;
  text-decoration: none;
  font-size: 0.7rem;
  letter-spacing: 0.1em;
  transition: color 0.2s;
}

.legal-link:hover {
  color: #f7f1e8;
}

.dot {
  color: #333;
  font-size: 0.7rem;
}

.footer-copy {
  color: #333;
  font-size: 0.7rem;
  letter-spacing: 0.1em;
  margin: 0;
}

@media (max-width: 640px) {
  .footer {
    padding: 0 1rem 1.75rem;
  }

  .footer-social {
    justify-content: center;
    flex-wrap: wrap;
    gap: 1rem 1.25rem;
  }

  .footer-legal {
    justify-content: center;
  }

  .footer-copy {
    text-align: center;
    line-height: 1.6;
  }

  .social-link,
  .legal-link {
    font-size: 0.68rem;
  }
}
</style>
