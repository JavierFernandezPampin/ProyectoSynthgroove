<script setup lang="ts">
import { ref, computed, onMounted } from "vue";
import { getReleases } from "@/services/releasesService";
import { getArtistas } from "@/services/artistService";

interface Release {
  id: number;
  titulo: string;
  url: string;
  artista: number;
}

interface Artista {
  id: number;
  nombre: string;
  imagen: string;
}

const releases = ref<Release[]>([]);
const artistas = ref<Artista[]>([]);
const loading = ref(true);

const releasesPorArtista = computed(() => {
  const grupos: Record<number, { artista: Artista; releases: Release[] }> = {};

  artistas.value.forEach((artista) => {
    grupos[artista.id] = { artista, releases: [] };
  });

  releases.value.forEach((release) => {
    if (grupos[release.artista]) {
      grupos[release.artista].releases.push(release);
    }
  });

  return Object.values(grupos).filter((g) => g.releases.length > 0);
});

onMounted(async () => {
  try {
    const [releasesData, artistasData] = await Promise.all([
      getReleases(),
      getArtistas(),
    ]);
    releases.value = releasesData;
    artistas.value = artistasData;
  } catch (error) {
    console.error(error);
  } finally {
    loading.value = false;
  }
});
</script>

<template>
  <div class="podcasts-wrapper">
    <h1 class="titulo">LATEST RELEASES</h1>
    <div v-if="loading" class="spinner-wrapper">
      <div class="spinner"></div>
    </div>
    <div v-else>
      <div
        v-for="grupo in releasesPorArtista"
        :key="grupo.artista.id"
        class="artista-bloque"
      >
        <template v-if="grupo.releases.length">
          <div class="artista-header">
            <h2 class="nombre">{{ grupo.artista.nombre }}</h2>
            <span class="count">{{ grupo.releases.length }} releases</span>
          </div>
          <div class="separador"></div>
        </template>

        <div
          v-for="release in grupo.releases"
          :key="release.id"
          class="podcast-item"
        >
          <p>{{ release.titulo }}</p>
          <iframe
            width="100%"
            height="100"
            scrolling="no"
            frameborder="no"
            :src="`https://w.soundcloud.com/player/?url=${release.url}&color=%23002363&auto_play=false`"
          ></iframe>
        </div>

        <div class="separador"></div>
      </div>
    </div>
  </div>
</template>

<style>
.podcasts-wrapper {
  max-width: 760px;
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
  margin: 1.5rem 0;
}

.artista-bloque {
  margin-bottom: 2rem;
}

.artista-header {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  gap: 1rem;
}

.nombre {
  font-size: 2rem;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: #f7f1e8;
  margin: 0;
}

.count {
  font-size: 0.75rem;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: #444;
}

.podcast-item {
  margin-bottom: 0.75rem;
}

.podcast-item p {
  margin: 0 0 0.65rem;
  color: #f7f1e8;
  line-height: 1.5;
}

.podcast-item iframe {
  border: 0;
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

@media (max-width: 640px) {
  .podcasts-wrapper {
    padding: 2rem 1rem 3rem;
  }

  .artista-header {
    flex-direction: column;
    align-items: flex-start;
  }

  .nombre {
    font-size: 1.4rem;
  }

  .count {
    font-size: 0.68rem;
  }
}
</style>
