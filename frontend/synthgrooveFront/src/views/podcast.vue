<script setup lang="ts">
import { ref, computed, onMounted } from "vue";
import { getArtistas } from "@/services/artistService";

interface Podcast {
  id: number;
  title: string;
  url: string;
}

interface Artista {
  id: number;
  nombre: string;
  podcasts: Podcast[];
}

const artistas = ref<Artista[]>([]);
const loading = ref(true);

const allPodcasts = computed(() =>
  artistas.value.flatMap((a) => a.podcasts ?? [])
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
  <div class="podcasts-wrapper">
    <h1 class="titulo">LATEST PODCASTS</h1>
    <div class="separador"></div>

    <div v-if="loading" class="spinner-wrapper">
      <div class="spinner"></div>
    </div>

    <div v-else-if="allPodcasts.length === 0" class="empty">
      <p>No hay podcasts disponibles</p>
    </div>

    <div v-else class="podcasts-grid">
      <div v-for="podcast in allPodcasts" :key="podcast.id" class="podcast-item">
        <iframe
          width="100%"
          height="300"
          scrolling="no"
          frameborder="no"
          allow="autoplay; encrypted-media"
          :src="`https://w.soundcloud.com/player/?url=${encodeURIComponent(podcast.url)}&color=%23002363&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true&visual=true`"
        ></iframe>
        <p class="item-titulo">{{ podcast.title }}</p>
      </div>
    </div>
  </div>
</template>

<style scoped>
.podcasts-wrapper {
  width: 100%;
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

.podcasts-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  column-gap: 0;
  row-gap: 4rem;
}

.podcast-item {
  padding: 0 2rem;
}

.podcast-item:nth-child(odd) {
  border-right: 1px solid #222;
  padding-left: 0;
}

.podcast-item:nth-child(even) {
  padding-right: 0;
}

.podcast-item iframe {
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
  .podcasts-wrapper {
    padding: 2rem 1rem 3rem;
  }

  .podcasts-grid {
    grid-template-columns: 1fr;
    row-gap: 2rem;
  }

  .podcast-item,
  .podcast-item:nth-child(odd),
  .podcast-item:nth-child(even) {
    padding: 0;
    border-right: none;
  }
}
</style>
