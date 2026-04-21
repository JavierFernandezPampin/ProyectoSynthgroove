<script setup lang="ts">
import logoBlanco from "./assets/logoBlanco.png";

const sections = [
  {
    title: "Merchandising",
    subtitle: "Prendas, objetos y ediciones con identidad propia.",
    image:
      "linear-gradient(180deg, rgba(84,32,13,.2), rgba(36,15,11,.88)), radial-gradient(circle at 30% 20%, rgba(255,190,123,.7), transparent 28%), linear-gradient(135deg, #d7865c, #5b2416 75%)",
  },
  {
    title: "Eventos",
    subtitle: "Fechas, flyers y convocatorias del colectivo.",
    image:
      "linear-gradient(180deg, rgba(44,38,25,.18), rgba(20,18,14,.88)), radial-gradient(circle at 70% 18%, rgba(254,233,180,.65), transparent 24%), linear-gradient(135deg, #9f7443, #352314 72%)",
  },
  {
    title: "Releases",
    subtitle: "Nuevos lanzamientos y archivos sonoros destacados.",
    image:
      "linear-gradient(180deg, rgba(27,39,50,.15), rgba(15,19,24,.88)), radial-gradient(circle at 32% 24%, rgba(191,227,255,.6), transparent 24%), linear-gradient(135deg, #7b97a8, #243342 72%)",
  },
  {
    title: "Podcast",
    subtitle: "Sesiones, entrevistas y conversaciones largas.",
    image:
      "linear-gradient(180deg, rgba(17,39,53,.18), rgba(10,18,25,.88)), radial-gradient(circle at 65% 18%, rgba(151,255,236,.58), transparent 24%), linear-gradient(135deg, #2d7985, #1e2a3f 72%)",
  },
  {
    title: "Sobre",
    subtitle: "Quienes somos y hacia donde empuja el proyecto.",
    image:
      "linear-gradient(180deg, rgba(36,18,44,.16), rgba(18,12,25,.88)), radial-gradient(circle at 50% 15%, rgba(255,218,183,.44), transparent 22%), linear-gradient(135deg, #6f6079, #231929 72%)",
  },
];
</script>

<template>
  <div class="home-shell">
    <header class="brand-header" aria-label="Identidad del colectivo">
      <img
        class="brand-logo"
        :src="logoBlanco"
        alt="Logo blanco del colectivo"
      />
    </header>

    <main class="home-content">
      <section class="hero-panel" aria-label="Presentacion principal">
        <video
          class="hero-video"
          autoplay
          muted
          loop
          playsinline
          preload="auto"
        >
          <source src="/videoInicio.mp4" type="video/mp4" />
        </video>
      </section>

      <section class="sections-panel" aria-label="Secciones principales">
        <article
          v-for="section in sections"
          :key="section.title"
          class="section-card"
          :style="{ '--card-image': section.image }"
        >
          <div class="section-card__backdrop"></div>
          <div class="section-card__caption">
            <span class="section-card__index">{{
              section.title.slice(0, 2).toUpperCase()
            }}</span>
            <h2>{{ section.title }}</h2>
          </div>
          <div class="section-card__content">
            <h3>{{ section.title }}</h3>
            <p>{{ section.subtitle }}</p>
          </div>
        </article>
      </section>
    </main>
  </div>
</template>

<style scoped>
.home-shell {
  min-height: 100vh;
  padding: clamp(0.85rem, 2vw, 1.5rem);
  background: #000;
}
.brand-header {
  display: flex;
  justify-content: center;
  padding: 0.1rem 0 0.55rem;
}
.brand-logo {
  width: clamp(42px, 4vw, 68px);
  height: auto;
  object-fit: contain;
}
.home-content {
  display: grid;
  gap: 1.5rem;
}
.hero-panel {
  position: relative;
  width: min(100%, 920px);
  min-height: 350px;
  margin-inline: auto;
  overflow: hidden;
  background: #121212;
}
.hero-panel::after {
  content: "";
  position: absolute;
  inset: 0;
  background: linear-gradient(
    180deg,
    rgba(12, 12, 12, 0.08),
    rgba(12, 12, 12, 0.28) 34%,
    rgba(12, 12, 12, 0.5)
  );
}
.hero-video {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
}
.sections-panel {
  display: flex;
  width: min(100%, 980px);
  min-height: 420px;
  margin-inline: auto;
  gap: clamp(2rem, 1.2vw, 1rem);
}
.section-card {
  position: relative;
  flex: 1 1 0;
  min-width: 0;
  overflow: hidden;
  background: #111;
  border: 1px solid rgba(255, 255, 255, 0.45);
  cursor: pointer;
  transition: flex 0.7s ease;
}
.section-card__backdrop {
  position: absolute;
  inset: 0;
  background:
    linear-gradient(180deg, rgba(255, 255, 255, 0.04), rgba(255, 255, 255, 0)),
    linear-gradient(145deg, rgba(255, 255, 255, 0.22), transparent 42%),
    var(--card-image);
  background-size: cover;
  background-position: center;
  transition:
    transform 0.5s ease,
    filter 0.5s ease;
}
.section-card__caption {
  position: relative;
  z-index: 1;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  gap: 0.75rem;
  height: 100%;
  padding: 1.2rem;
  background: linear-gradient(
    180deg,
    rgba(24, 24, 24, 0.04),
    rgba(24, 24, 24, 0.68)
  );
  color: #f7f1e8;
}
.section-card__index {
  width: fit-content;
  padding: 0.2rem 0.45rem;
  background: rgba(255, 248, 239, 0.18);
  font-size: 0.7rem;
  font-weight: 700;
  letter-spacing: 0.14em;
}
.section-card__caption h2 {
  margin: 0;
  font-size: 1.2rem;
  font-weight: 700;
  line-height: 1.05;
  text-transform: uppercase;
  text-shadow: 0 4px 20px rgba(0, 0, 0, 0.24);
}
.section-card__content {
  position: absolute;
  top: 50%;
  left: 50%;
  z-index: 2;
  width: min(72%, 18rem);
  padding: 1.1rem 1rem;
  background: rgba(255, 255, 255, 0.94);
  color: #111;
  text-align: center;
  transform: translate(-50%, -50%) scale(0);
  opacity: 0;
  pointer-events: none;
  transition:
    transform 0.5s ease,
    opacity 0.4s ease;
}
.section-card__content h3 {
  margin: 0 0 0.45rem;
  font-size: 1.1rem;
  font-weight: 700;
  line-height: 1.1;
  text-transform: uppercase;
}
.section-card__content p {
  margin: 0;
  font-size: 0.9rem;
  line-height: 1.45;
  color: rgba(17, 17, 17, 0.78);
}
.sections-panel:hover .section-card:hover {
  flex: 4.6 1 0;
}
.sections-panel:hover .section-card:not(:hover) .section-card__backdrop {
  filter: saturate(0.82) brightness(0.82);
}
.sections-panel:hover .section-card:hover .section-card__backdrop {
  transform: scale(1.06);
  filter: brightness(0.7);
}
.sections-panel:hover .section-card:hover .section-card__content {
  transform: translate(-50%, -50%) scale(1);
  opacity: 1;
}

@media (max-width: 1040px) {
  .sections-panel {
    min-height: 360px;
  }
}

@media (max-width: 700px) {
  .home-shell {
    padding: 0.7rem;
  }
  .brand-header {
    padding-bottom: 0.4rem;
  }
  .hero-panel {
    min-height: 280px;
  }
  .sections-panel {
    display: grid;
    width: 100%;
    min-height: auto;
  }
  .section-card {
    min-height: 220px;
  }
  .section-card__content {
    width: min(78%, 22rem);
    transform: translate(-50%, -50%) scale(1);
    opacity: 1;
  }
  .sections-panel:hover .section-card,
  .sections-panel:hover .section-card:hover {
    flex: 1;
  }
  .sections-panel:hover .section-card__backdrop {
    transform: none;
    filter: brightness(0.7);
  }
}
</style>
