<script setup lang="ts">
import { ref } from 'vue'
import logoBlanco from "./assets/img/logoBlanco.png";
import synthgrooveCamiseta from "./assets/img/synthgrooveCamiseta.jpg"
import imagenEvento from "./assets/img/imagenEvento.jpg"

const cardsSection = ref<HTMLElement | null>(null)

function scrollToCards() {
  cardsSection.value?.scrollIntoView({ behavior: 'smooth' })
}

const sections = [
  {
    title: "Merchandising",
    image: synthgrooveCamiseta,
    isImage: true 
  },
  {
    title: "Eventos",
    image: imagenEvento,
    isImage:true
  },
  {
    title: "Releases",
    image:
      "linear-gradient(180deg, rgba(27,39,50,.15), rgba(15,19,24,.88)), radial-gradient(circle at 32% 24%, rgba(191,227,255,.6), transparent 24%), linear-gradient(135deg, #7b97a8, #243342 72%)",
  },
  {
    title: "Podcasts",
    image:
      "linear-gradient(180deg, rgba(17,39,53,.18), rgba(10,18,25,.88)), radial-gradient(circle at 65% 18%, rgba(151,255,236,.58), transparent 24%), linear-gradient(135deg, #2d7985, #1e2a3f 72%)",
  },
  {
    title: "Sobre",
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

    <main class="contenidoPrincipal">
      <section class="videoSection" aria-label="Presentacion principal">
        <video
          class="video"
          autoplay
          muted
          loop
          playsinline
          preload="auto"
        >
          <source src="/videoInicio.mp4" type="video/mp4" />
        </video>

        <button class="scroll-arrow" @click="scrollToCards" aria-label="Ver secciones">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <polyline points="6 9 12 15 18 9" />
          </svg>
        </button>
      </section>

      <section class="sectionCards" ref="cardsSection" aria-label="Secciones principales">
        <article
          v-for="section in sections"
          :key="section.title"
          class="section-card"
          :style="section.isImage 
            ? { '--card-image': `url(${section.image})` } 
            : { '--card-image': section.image }"
        >
          <div class="section-card__backdrop"></div>
          <div class="section-card__caption">
            <h2>{{ section.title }}</h2>
          </div>
          <div class="section-card__content">
            <h3>{{ section.title }}</h3>
          </div>
        </article>
      </section>
    </main>
  </div>
</template>

<style scoped>

/* HEADER */
.brand-header {
  display: flex;
  justify-content: center;
  padding-bottom: 10px;
  padding-top: 10px;
}
.brand-logo {
  width: 70px;
  height: auto;
  object-fit: contain;
}

/* MAIN */

/* VIDEO */
.contenidoPrincipal {
  display: grid;
  gap: 1.5rem;
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

/* FLECHA */
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
  0%, 100% { transform: translateX(-50%) translateY(0); }
  50%       { transform: translateX(-50%) translateY(8px); }
}

/* SECCION PANELES */
.sectionCards {
  display: flex;
  width: min(100%, 1000px);
  min-height: 500px;
  margin-inline: auto;
  gap: 50px;
  padding-bottom: 100px;
}

.section-card {
  position: relative;
  flex: 1 1 0;
  min-width: 0;
  overflow: hidden;
  background: #111;
  border-radius: 1px;
  cursor: pointer;
  transition: flex 0.7s ease;
}

.section-card + .section-card::before {
  content: '';
  position: absolute;
  left: -26px;
  top: 8%;
  height: 84%;
  width: 1px;
  background: #5C5C5C;
  z-index: 2;
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

.section-card__caption h2 {
  margin: 0;
  font-size: 1.2rem;
  font-weight: 700;
  line-height: 1.05;
  text-transform: uppercase;
  text-shadow: 0 4px 20px rgba(0, 0, 0, 0.24);
}

.section-card__content p {
  margin: 0;
  font-size: 0.9rem;
  line-height: 1.45;
  color: rgba(17, 17, 17, 0.78);
}

.section-card__backdrop {
  position: absolute;
  inset: 0;
  background-image: var(--card-image);
  background-size: cover;
  background-position: center;
  transition: transform 0.7s ease, filter 0.7s ease;
}

.sectionCards:hover .section-card:hover {
  flex: 4.6 1 0;
}
.sectionCards:hover .section-card:not(:hover) .section-card__backdrop {
  filter: saturate(0.82) brightness(0.82);
}
.sectionCards:hover .section-card:hover .section-card__backdrop {
  transform: scale(1.06);
  filter: brightness(0.7);
}
.sectionCards:hover .section-card:hover .section-card__content {
  transform: translate(-50%, -50%) scale(1);
  opacity: 1;
}
.sectionCards:hover .section-card:hover .section-card__caption {
  align-items: center;
  text-align: center;
}
.sectionCards:hover .section-card:hover .section-card__caption h2 {
  font-size: 2rem;
  transition: font-size 0.5s ease, transform 0.5s ease-in-out;
}

@media (max-width: 1040px) {
  .sectionCards {
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
  .videoSection {
    min-height: 280px;
  }
  .sectionCards {
    display: grid;
    width: 100%;
    min-height: auto;
    gap: 0;
  }
  .section-card {
    min-height: 220px;
  }
  .section-card + .section-card::before {
    left: 8%;
    top: 0;
    width: 84%;
    height: 1px;
  }
  .section-card__content {
    width: min(78%, 22rem);
    transform: translate(-50%, -50%) scale(1);
    opacity: 1;
  }
  .sectionCards:hover .section-card,
  .sectionCards:hover .section-card:hover {
    flex: 1;
  }
  .sectionCards:hover .section-card__backdrop {
    transform: none;
    filter: brightness(0.7);
  }
}
</style>