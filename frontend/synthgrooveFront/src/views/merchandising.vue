<script setup lang="ts">
import { ref, onMounted } from "vue";
import { getProductos } from "@/services/productoService";
import { useAuthStore } from "@/stores/auth";
import { iniciarPago } from "@/services/pagoService";

interface Producto {
  id: number;
  nombre: string;
  descripcion: string;
  precio: number;
  imagen: string;
}

const productos = ref<Producto[]>([]);
const loading = ref(true);
const authStore = useAuthStore();

onMounted(async () => {
  try {
    productos.value = await getProductos();
  } catch (error) {
    console.error(error);
  } finally {
    loading.value = false;
  }
});

const pagandoId = ref<number | null>(null);

async function comprar(producto: Producto) {
  pagandoId.value = producto.id;
  try {
    await iniciarPago("producto", producto.id, 1);
  } catch (err) {
    console.error(err);
    alert("Error al iniciar el pago. Inténtalo de nuevo.");
  } finally {
    pagandoId.value = null;
  }
}
</script>

<template>
  <div class="merch-wrapper">
    <h1 class="titulo-merch">MERCHANDISING</h1>
    <div class="separador"></div>

    <div v-if="loading" class="spinner-wrapper">
      <div class="spinner"></div>
      <p>Cargando merchandising...</p>
    </div>
    <div v-else class="productos-lista">
      <div class="producto-col" v-for="producto in productos" :key="producto.id">
        <div class="producto-card">
          <img :src="producto.imagen" class="producto-img" />
          <div class="producto-info">
            <h5 class="producto-nombre">{{ producto.nombre }}</h5>
            <p class="producto-descripcion">{{ producto.descripcion }}</p>
            <div class="producto-footer">
              <span class="producto-precio">{{ producto.precio }} €</span>
              <button
                v-if="authStore.isAuthenticated"
                class="btn-reservar"
                :disabled="pagandoId === producto.id"
                @click="comprar(producto)"
              >
                {{ pagandoId === producto.id ? "Redirigiendo..." : "Comprar →" }}
              </button>
              <router-link v-else to="/login" class="btn-login-hint">
                Inicia sesión para comprar
              </router-link>
            </div>
          </div>
        </div>
        <div class="separador"></div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.merch-wrapper {
  max-width: 960px;
  margin: 0 auto;
  padding: 3rem 1.5rem;
  background: #000;
}

.productos-lista {
  display: grid;
  grid-template-columns: 1fr 1fr;
}

@media (max-width: 768px) {
  .productos-lista {
    grid-template-columns: 1fr;
  }
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
  min-width: 0;
  height: 180px;
}

.producto-nombre {
  font-size: 1.25rem;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: #f7f1e8;
  margin: 0;
  overflow-wrap: anywhere;
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

.producto-precios {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 0.15rem;
}

.producto-precio {
  font-size: 1.25rem;
  font-weight: 700;
  color: #f7f1e8;
  letter-spacing: 0.05em;
}

.btn-login-hint {
  font-size: 0.7rem;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: #555;
  text-decoration: none;
  border-bottom: 1px solid #333;
  padding-bottom: 1px;
  transition: color 0.2s, border-color 0.2s;
  white-space: nowrap;
}

.btn-login-hint:hover {
  color: #f7f1e8;
  border-bottom-color: #f7f1e8;
}

.btn-reservar {
  display: inline-flex;
  align-items: center;
  justify-content: center;
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

  background: none;
  border: none;
  cursor: pointer;
  font-family: inherit;
}

.btn-reservar:hover {
  color: #666;
  border-color: #666;
}

.spinner-wrapper {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  min-height: 300px;
  gap: 1rem;
}

.spinner-wrapper p {
  color: #f7f1e8;
  font-size: 0.95rem;
  margin: 0;
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

@media (max-width: 900px) {
  .producto-card {
    gap: 1.25rem;
  }

  .producto-info {
    height: auto;
    min-height: 180px;
  }
}

@media (max-width: 680px) {
  .merch-wrapper {
    padding: 2rem 1rem 3rem;
  }

  .producto-card {
    flex-direction: column;
    gap: 1rem;
    padding: 1.25rem 0;
  }

  .producto-img {
    width: 100%;
    height: auto;
    aspect-ratio: 1 / 1;
  }

  .producto-info {
    gap: 1rem;
    min-height: 0;
  }

  .producto-footer {
    flex-direction: column;
    align-items: flex-start;
    gap: 1rem;
  }

  .precio-fila {
    flex-wrap: wrap;
  }

  .btn-reservar {
    width: 100%;
    padding: 0.85rem 1rem;
    border: 1px solid #f7f1e8;
    border-bottom-width: 1px;
  }
}
</style>
