<script setup lang="ts">
import { ref, onMounted } from "vue";
import { getProductos } from "@/services/productoService";

interface Producto {
  id: number;
  nombre: string;
  descripcion: string;
  precio: number;
  imagen: string;
}

const productos = ref<Producto[]>([]);

onMounted(async () => {
  try {
    productos.value = await getProductos();
    console.log("imagen:", productos.value[0]?.imagen);
  } catch (error) {
    console.error(error);
  }
});

const loading = ref(true);

onMounted(async () => {
  try {
    productos.value = await getProductos();
  } catch (error) {
    console.error(error);
  } finally {
    loading.value = false;
  }
});
</script>
<template>
  <div class="merch-wrapper">
    <h1 class="titulo-merch">MERCHANDISING</h1>
    <div class="separador"></div>

    <div v-if="loading" class="spinner-wrapper">
      <div class="spinner"></div>
    </div>
    <div v-else class="row g-0">
      <div class="col-md-6" v-for="producto in productos" :key="producto.id">
        <div class="producto-card">
          <img :src="producto.imagen" class="producto-img" />
          <div class="producto-info">
            <h5 class="producto-nombre">{{ producto.nombre }}</h5>
            <p class="producto-descripcion">{{ producto.descripcion }}</p>
            <div class="producto-footer">
              <span class="producto-precio">{{ producto.precio }} €</span>
              <a
                :href="`https://wa.me/34618632738?text=${encodeURIComponent(`Hola! Me gustaria hacer la compra de: ${producto.nombre} (${producto.precio} €)`)}`"
                target="_blank"
                class="btn-reservar"
              >
                Reservar →
              </a>
            </div>
          </div>
        </div>
        <div class="separador"></div>
      </div>
    </div>
  </div>
</template>

<style>
.merch-wrapper {
  max-width: 960px;
  margin: 0 auto;
  padding: 3rem 1.5rem;
}

.titulo-merch {
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

.producto-card {
  display: flex;
  gap: 2rem;
  align-items: flex-start;
  padding: 1.5rem 0;
}

.producto-img {
  width: 180px;
  height: 180px;
  object-fit: cover;
  flex-shrink: 0;
}

.producto-info {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  flex: 1;
  height: 180px;
}

.producto-nombre {
  font-size: 1.25rem;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: #f7f1e8;
  margin: 0;
}

.producto-descripcion {
  font-size: 0.875rem;
  color: #888;
  margin: 0.5rem 0 0;
  line-height: 1.6;
}

.producto-footer {
  display: flex;
  align-items: center;
  gap: 2rem;
  margin-top: auto;
}

.producto-precio {
  font-size: 1.25rem;
  font-weight: 700;
  color: #f7f1e8;
  letter-spacing: 0.05em;
}

.btn-reservar {
  font-size: 0.75rem;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: #f7f1e8;
  text-decoration: none;
  border-bottom: 1px solid #f7f1e8;
  padding-bottom: 2px;
  transition:
    color 0.2s,
    border-color 0.2s;
}

.btn-reservar:hover {
  color: #666;
  border-color: #666;
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
