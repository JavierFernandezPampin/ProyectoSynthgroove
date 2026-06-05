<script setup lang="ts">
import { ref, computed, onMounted } from "vue";
import { getArtistas } from "@/services/artistService";

interface Release {
  id: number;
  titulo: string;
  url: string;
}

interface Artista {
  id: number;
  nombre: string;
  releases: Release[];
}

const artistas = ref<Artista[]>([]);
const loading = ref(true);

const allReleases = computed(() =>
  artistas.value.flatMap((a) => a.releases ?? [])
);

onMounted(async () => {
  try {
    artistas.value = await getArtistas();
  } finally {
    loading.value = false;
  }
});
</script>

<template>
  <div class="releases-wrapper">
    <h1 class="titulo">LATEST RELEASES</h1>
    <div class="separador"></div>

    <div v-if="loading" class="spinner-wrapper">
      <div class="spinner"></div>
    </div>

    <div v-else-if="allReleases.length === 0" class="empty">
      <p>No hay releases disponibles</p>
    </div>

    <div v-else class="releases-grid">
      <div v-for="release in allReleases" :key="release.id" class="release-item">
        <iframe
          width="100%"
          height="300"
          scrolling="no"
          frameborder="no"
          allow="autoplay; encrypted-media"
          :src="`https://w.soundcloud.com/player/?url=${encodeURIComponent(release.url)}&color=%23002363&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true&visual=true`"
        ></iframe>
        <p class="item-titulo">{{ release.titulo }}</p>
      </div>
    </div>
  </div>
</template>

<style scoped>
.releases-wrapper {
  max-width: 1200px;
  margin: 0 auto;
  padding: 3rem 1.5rem;
  background: #000;
}

.titulo {
  text-align: left;
  font-size: 0.75rem;
  letter-spacing: 0.3em;
  text-transform: uppercase;
  color: #666;
  margin-bottom: 1rem;
}

.separador {
  width: 100%;
  height: 1px;
  background-color: #222;
  margin-bottom: 2rem;
}

.releases-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  column-gap: 0;
  row-gap: 4rem;
}

.release-item {
  padding: 0 2rem;
}

.release-item:nth-child(odd) {
  border-right: 1px solid #222;
  padding-left: 0;
}

.release-item:nth-child(even) {
  padding-right: 0;
}

.release-item iframe {
  border: 0;
  display: block;
}

.item-titulo {
  margin: 1rem 0 0;
  color: #f7f1e8;
  font-size: 1.1rem;
  font-weight: 600;
  letter-spacing: 0.03em;
}

.empty {
  color: #555;
  font-size: 0.9rem;
  padding: 3rem 0;
}

.spinner-wrapper {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 300px;
}

.spinner {
  width: 36px;
  height: 36px;
  border: 2px solid #333;
  border-top-color: #f7f1e8;
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
}

@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}

@media (max-width: 720px) {
  .releases-wrapper {
    padding: 2rem 1rem 3rem;
  }

  .releases-grid {
    grid-template-columns: 1fr;
    row-gap: 2rem;
  }

  .release-item,
  .release-item:nth-child(odd),
  .release-item:nth-child(even) {
    padding: 0;
    border-right: none;
  }
}
</style>
