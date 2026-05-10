<script setup lang="ts">
import { ref } from "vue";

const cardsSection = ref<HTMLElement | null>(null);

function scrollToCards() {
  cardsSection.value?.scrollIntoView({ behavior: "smooth" });
}

const camisetaUrl = new URL("../assets/img/cami.webp", import.meta.url).href;
const imagenEvento = new URL("../assets/img/imagenEvento.jpg", import.meta.url)
  .href;
const tadeo = new URL("../assets/img/tadeo.jpg", import.meta.url).href;
const ycoxxx = new URL("../assets/img/ycox.jpg", import.meta.url).href;
const oss = new URL("../assets/img/oss.jpg", import.meta.url).href;

const sections = [
  {
    title: "Merchandising",
    image: camisetaUrl,
    isImage: true,
    path: "/merchandising",
  },
  {
    title: "Eventos",
    image: imagenEvento,
    isImage: true,
    path: "/eventos",
  },
  {
    title: "Releases",
    image: tadeo,
    isImage: true,
    path: "/releases",
  },
  {
    title: "Podcasts",
    image: ycoxxx,
    isImage: true,
    path: "/podcasts",
  },
  {
    title: "Sobre",
    image: oss,
    isImage: true,
    path: "/sobre",
  },
];
</script>

<template>
  <div class="home-shell">
    <main class="contenidoPrincipal">
      <section class="videoSection" aria-label="Presentacion principal">
        <video class="video" autoplay muted loop playsinline preload="auto">
          <source src="/videoInicio.mp4" type="video/mp4" />
        </video>

        <button
          class="scroll-arrow"
          @click="scrollToCards"
          aria-label="Ver secciones"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round"
          >
            <polyline points="6 9 12 15 18 9" />
          </svg>
        </button>
      </section>

      <section class="sectionCards" ref="cardsSection">
        <router-link
          v-for="(section, i) in sections"
          :key="section.title"
          :to="section.path"
          class="section-card"
          :style="{
            '--card-image': section.isImage
              ? `url('${section.image}')`
              : section.image,
          }"
        >
          <div class="section-card__backdrop"></div>
          <div class="section-card__caption">
            <span class="section-card__index">0{{ i + 1 }}</span>
            <h2>{{ section.title }}</h2>
            <span class="section-card__arrow">→</span>
          </div>
        </router-link>
      </section>
    </main>
  </div>
</template>
<style scoped>
.home-shell {
  background: black;
  min-height: 100vh;
  font-family: "Space Grotesk", "Avenir Next", "Trebuchet MS", sans-serif;
}

.contenidoPrincipal {
  display: grid;
  gap: 0;
}

.videoSection {
  position: relative;
  width: min(100%, 920px);
  min-height: 900px;
  margin-inline: auto;
  overflow: hidden;
  background: #121212;
}
.video {
  position: absolute;
  width: 100%;
  height: 100%;
  object-fit: cover;
}
.scroll-arrow {
  position: absolute;
  bottom: 6rem;
  left: 50%;
  transform: translateX(-50%);
  z-index: 2;
  background: transparent;
  border: none;
  cursor: pointer;
  color: #f7f1e8;
  opacity: 0.6;
  transition: opacity 0.3s ease;
  animation: bounce 2s infinite;
}
.scroll-arrow:hover {
  opacity: 1;
}
.scroll-arrow svg {
  width: 2.5rem;
  height: 2.5rem;
}

@keyframes bounce {
  0%,
  100% {
    transform: translateX(-50%) translateY(0);
  }
  50% {
    transform: translateX(-50%) translateY(8px);
  }
}

/* ── GRID DE CARDS ── */
.sectionCards {
  display: grid;
  grid-template-columns: 1fr 1fr;
  width: 100%;
  gap: 0;
  padding-bottom: 0;
}

/* Primera card ocupa todo el ancho */
.section-card:first-child {
  grid-column: 1 / -1;
  min-height: 420px;
}
.section-card:first-child .section-card__body {
  min-height: 420px;
}
.section-card:first-child .section-card__caption h2 {
  font-size: clamp(3rem, 8vw, 6rem);
}

.section-card {
  position: relative;
  min-height: 300px;
  overflow: hidden;
  background: #111;
  cursor: pointer;
  text-decoration: none;
  display: flex;
  flex-direction: column;
  border: 1px solid #111;
}

/* Separador entre cards */
.section-card + .section-card {
  border-left: 1px solid #1a1a1a;
}

.section-card__backdrop {
  position: absolute;
  inset: 0;
  background: var(--card-image);
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  filter: brightness(0.45);
  transition:
    transform 0.6s ease,
    filter 0.6s ease;
}

.section-card:hover .section-card__backdrop {
  transform: scale(1.04);
  filter: brightness(0.3);
}

/* Número índice */
.section-card__index {
  position: absolute;
  top: 1.5rem;
  left: 2rem;
  z-index: 2;
  font-size: 0.65rem;
  letter-spacing: 0.3em;
  color: #444;
}

.section-card__caption {
  position: relative;
  z-index: 1;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  height: 100%;
  min-height: 300px;
  padding: 2rem;
}

.section-card__caption h2 {
  margin: 0;
  font-size: clamp(1.8rem, 4vw, 3.5rem);
  font-weight: 700;
  line-height: 1;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: #f7f1e8;
  transition: letter-spacing 0.4s ease;
}

.section-card:hover .section-card__caption h2 {
  letter-spacing: 0.12em;
}

/* Flecha que aparece en hover */
.section-card__arrow {
  display: block;
  margin-top: 1rem;
  font-size: 1.5rem;
  color: #f7f1e8;
  opacity: 0;
  transform: translateX(-8px);
  transition:
    opacity 0.4s ease,
    transform 0.4s ease;
}

.section-card:hover .section-card__arrow {
  opacity: 1;
  transform: translateX(0);
}

/* Oculta el content antiguo */
.section-card__content {
  display: none;
}

@media (max-width: 700px) {
  .sectionCards {
    grid-template-columns: 1fr;
  }
  .section-card:first-child {
    grid-column: 1;
    min-height: 280px;
  }
  .section-card:first-child .section-card__body,
  .section-card__caption {
    min-height: 220px;
  }
  .section-card + .section-card {
    border-left: none;
    border-top: 1px solid #1a1a1a;
  }
}
</style>
