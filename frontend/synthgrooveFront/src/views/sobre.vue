<script setup lang="ts">
import { ref, onMounted } from "vue";
import { getArtistas } from "@/services/artistService";

interface Artista {
  id: number;
  nombre: string;
  descripcion: string;
  instagram: string;
  soundcloud: string;
  imagen: string;
}

const artistas = ref<Artista[]>([]);
const loading = ref(true);

onMounted(async () => {
  try {
    artistas.value = await getArtistas();
  } catch (error) {
    console.error(error);
  } finally {
    loading.value = false;
  }
});

// Cogemos la URL base de las variables de entorno, si no existe usamos cadena vacía
const BASE_URL = import.meta.env.VITE_API_URL || "";

// El backend devuelve las imágenes con una URL interna de Docker (backend:8000)
// que el navegador no entiende, así que la cambiamos por localhost:8000
function fixImageUrl(url: string | null): string {
  if (!url) return "";
  return url.replace("http://backend:8000", BASE_URL);
}
</script>

<template>
  <div class="sobre-wrapper">
    <h1 class="titulo-sobre">SOBRE NOSOTROS</h1>
    <div class="separador"></div>

    <div class="sobre-content">
      <p class="descripcion">
        SYNTHGROOVE nace con la finalidad de mostrar su visión particular del
        techno dentro de la escena electrónica actual. Destacando y promoviendo
        la calidad de los artistas de la escena nacional y comunitaria en
        conjunto con artistas de la escena global. Todo ello en un espacio libre
        de prejuicios y estereotipos, donde el respeto hacia esta visión y su
        comunidad favorezca el enriquecimiento de la cultura techno.
        <br />
        Bienvenidos a la experiencia SYNTHGROOVE.
      </p>
      <div class="separador"></div>
    </div>
    <div v-if="loading" class="spinner-wrapper">
      <div class="spinner"></div>
    </div>
    <div v-else class="row g-0">
      <h2 class="titulo-artistas">ARTISTAS</h2>
      <div class="separador"></div>

      <div
        class="artista-card"
        v-for="artista in artistas"
        :key="artista.nombre"
      >
        <img :src="artista.imagen" class="artista-img" />
        <div class="artista-info">
          <h3 class="artista-nombre">{{ artista.nombre }}</h3>
          <p class="artista-bio">{{ artista.descripcion }}</p>
          <div class="artista-links">
            <a
              v-if="artista.instagram"
              :href="artista.instagram"
              target="_blank"
              class="artista-link"
            >
              <svg
                width="14"
                height="14"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="1.5"
              >
                <rect x="2" y="2" width="20" height="20" rx="5" />
                <circle cx="12" cy="12" r="4" />
                <circle
                  cx="17.5"
                  cy="6.5"
                  r="1"
                  fill="currentColor"
                  stroke="none"
                />
              </svg>
              instagram
            </a>
            <a
              v-if="artista.soundcloud"
              :href="artista.soundcloud"
              target="_blank"
              class="artista-link"
            >
              <svg
                width="14"
                height="14"
                viewBox="0 0 24 24"
                fill="currentColor"
              >
                <path
                  d="M1.175 12.225c-.042 0-.08.03-.083.072l-.445 3.902.445 3.77c.003.04.041.072.083.072.04 0 .077-.03.08-.072l.504-3.77-.504-3.902c-.003-.042-.04-.072-.08-.072zm1.57-.9c-.05 0-.09.037-.094.085l-.38 4.787.38 4.6c.004.05.044.085.094.085.048 0 .088-.036.092-.085l.43-4.6-.43-4.787c-.004-.048-.044-.085-.092-.085zm1.59-.4c-.057 0-.104.045-.107.1l-.32 5.187.32 4.43c.003.057.05.1.107.1.056 0 .102-.043.106-.1l.362-4.43-.362-5.187c-.004-.055-.05-.1-.106-.1zm4.17-3.8c-.23-.087-.476-.134-.732-.134-1.173 0-2.13.87-2.248 1.99-.06.003-.118.01-.175.018v9.337c.057.006.114.01.175.01h6.79c.9 0 1.63-.73 1.63-1.63 0-.9-.73-1.63-1.63-1.63-.09 0-.177.008-.263.022.04-.178.062-.363.062-.553 0-1.46-1.183-2.643-2.643-2.643-.36 0-.703.072-1.016.203z"
                />
              </svg>
              soundcloud
            </a>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style>
.sobre-wrapper {
  max-width: 900px;
  margin: 0 auto;
  padding: 3rem 1.5rem;
}

.titulo-sobre,
.titulo-artistas {
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
  margin: 1rem 0;
}

.sobre-content {
  padding-top: 1rem;
}

.descripcion {
  font-size: 20px;
  color: #f7f1e8;
  line-height: 1.8;
  margin: 0;
  text-align: center;
}

.artista-card {
  display: flex;
  gap: 3rem;
  align-items: flex-start;
  padding: 2rem 0;
  border-bottom: 1px solid #222;
}

.artista-img {
  width: 260px;
  height: 260px;
  object-fit: cover;
  flex-shrink: 0;
}

.artista-info {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  padding-top: 0.5rem;
}

.artista-nombre {
  font-size: 1.5rem;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: #f7f1e8;
  margin: 0;
}

.artista-bio {
  font-size: 0.9rem;
  color: #888;
  line-height: 1.7;
  margin: 0;
}

.artista-links {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  margin-top: auto;
}

.artista-link {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  color: #555;
  text-decoration: none;
  font-size: 0.75rem;
  letter-spacing: 0.1em;
  transition: color 0.2s;
}

.artista-link:hover {
  color: #f7f1e8;
}

@media (max-width: 600px) {
  .artista-card {
    flex-direction: column;
  }
  .artista-img {
    width: 100%;
    height: 240px;
  }
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
</style>
