<script setup lang="ts">
import { ref, computed, onMounted } from "vue";
import { getEventos } from "@/services/eventosService";
import { useAuthStore } from "@/stores/auth";
import { iniciarPago } from "@/services/pagoService";

interface Evento {
  id: number;
  nombre: string;
  localizacion: string;
  fecha_release: string | null;
  imagen: string | null;
  precio: number | string;
  usuario: number | null;
}

const eventos = ref<Evento[]>([]);
const loading = ref(true);
const seccionActiva = ref<"proximos" | "pasados">("proximos");
const authStore = useAuthStore();
const euroFormatter = new Intl.NumberFormat("es-ES", {
  style: "currency",
  currency: "EUR",
});

function normalizarPrecio(precio: number | string): number {
  const valor = Number(precio);
  return Number.isFinite(valor) ? valor : 0;
}

function formatearPrecio(precio: number | string): string {
  const valor = normalizarPrecio(precio);
  return valor === 0 ? "Gratis" : euroFormatter.format(valor);
}

function parseFecha(fechaStr: string | null): Date {
  if (!fechaStr) return new Date(NaN);
  const partes = fechaStr.split("-").map(Number);
  if (partes.length < 3) return new Date(NaN);
  const y = partes[0]!;
  const m = partes[1]!;
  const d = partes[2]!;
  return new Date(y, m - 1, d);
}

const ahora = new Date();

const eventosFuturos = computed(() =>
  eventos.value.filter((e) => parseFecha(e.fecha_release) >= ahora),
);

const eventosPasados = computed(() =>
  [...eventos.value]
    .filter((e) => parseFecha(e.fecha_release) < ahora)
    .reverse(),
);

const eventosMostrados = computed(() =>
  seccionActiva.value === "proximos"
    ? eventosFuturos.value
    : eventosPasados.value,
);

function agruparPorMes(lista: Evento[]) {
  const grupos: Record<string, Evento[]> = {};
  for (const evento of lista) {
    const fecha = parseFecha(evento.fecha_release);
    const clave = isNaN(fecha.getTime())
      ? "Sin fecha"
      : fecha.toLocaleDateString("es-ES", { month: "long", year: "numeric" });
    if (!grupos[clave]) grupos[clave] = [];
    grupos[clave].push(evento);
  }
  return grupos;
}

const eventosPorMes = computed(() => agruparPorMes(eventosMostrados.value));

function getDia(fechaStr: string | null) {
  const f = parseFecha(fechaStr);
  return isNaN(f.getTime())
    ? "--"
    : f.toLocaleDateString("es-ES", { day: "2-digit" });
}
function getDiaNombre(fechaStr: string | null) {
  const f = parseFecha(fechaStr);
  return isNaN(f.getTime())
    ? "---"
    : f.toLocaleDateString("es-ES", { weekday: "short" });
}

onMounted(async () => {
  try {
    eventos.value = await getEventos();
  } catch (error) {
    console.error(error);
  } finally {
    loading.value = false;
  }
});

const pagandoId = ref<number | null>(null);

async function reservarEvento(evento: Evento) {
  pagandoId.value = evento.id;
  try {
    await iniciarPago("evento", evento.id, 1);
  } catch (err) {
    console.error(err);
    alert("Error al iniciar el pago.");
  } finally {
    pagandoId.value = null;
  }
}
</script>

<template>
  <div class="eventos-wrapper">
    <h1 class="titulo-eventos">EVENTOS</h1>
    <div class="separador"></div>

    <!-- Tabs próximos / pasados -->
    <div class="tabs-bar">
      <button
        class="tab-btn"
        :class="{ activo: seccionActiva === 'proximos' }"
        @click="seccionActiva = 'proximos'"
      >
        Próximos
        <span v-if="!loading" class="tab-count">{{
          eventosFuturos.length
        }}</span>
      </button>
      <button
        class="tab-btn"
        :class="{ activo: seccionActiva === 'pasados' }"
        @click="seccionActiva = 'pasados'"
      >
        Pasados
        <span v-if="!loading" class="tab-count">{{
          eventosPasados.length
        }}</span>
      </button>
    </div>

    <!-- Spinner -->
    <div v-if="loading" class="spinner-wrapper">
      <div class="spinner"></div>
      <p>Cargando eventos...</p>
    </div>

    <!-- Sin resultados -->
    <div v-else-if="eventosMostrados.length === 0" class="sin-resultados">
      <p>
        {{
          seccionActiva === "proximos"
            ? "No hay eventos próximos."
            : "No hay eventos pasados."
        }}
      </p>
    </div>

    <!-- Lista agrupada por mes -->
    <template v-else>
      <div
        v-for="(eventosDelMes, mes) in eventosPorMes"
        :key="mes"
        class="mes-grupo"
      >
        <div class="mes-header">
          <span class="mes-label">{{ mes }}</span>
          <div class="mes-linea"></div>
        </div>

        <div
          v-for="evento in eventosDelMes"
          :key="evento.id"
          class="evento-fila"
          :class="{ pasado: seccionActiva === 'pasados' }"
        >
          <!-- Imagen -->
          <div class="evento-img-wrapper">
            <img
              v-if="evento.imagen"
              :src="evento.imagen"
              :alt="evento.nombre"
              class="evento-img"
            />
            <div v-else class="evento-img-placeholder"></div>
          </div>

          <!-- Fecha -->
          <div class="evento-fecha">
            <span class="evento-dia-num">{{
              getDia(evento.fecha_release)
            }}</span>
            <span class="evento-dia-nombre">{{
              getDiaNombre(evento.fecha_release)
            }}</span>
          </div>

          <!-- Info -->
          <div class="evento-info">
            <h2 class="evento-titulo">{{ evento.nombre }}</h2>
            <p class="evento-lugar">{{ evento.localizacion }}</p>
          </div>

          <!-- Reserva -->
          <div class="evento-actions">
            <div class="evento-compra">
              <div class="evento-precios">
                <span class="evento-precio">{{ formatearPrecio(evento.precio) }}</span>
              </div>

              <template v-if="seccionActiva === 'proximos'">
                <button
                  v-if="authStore.isAuthenticated"
                  class="btn-reservar"
                  :disabled="pagandoId === evento.id"
                  @click="reservarEvento(evento)"
                >
                  {{ pagandoId === evento.id ? "..." : "Reservar" }}
                </button>
                <router-link v-else to="/login" class="btn-login-hint">
                  Inicia sesión para reservar
                </router-link>
              </template>
            </div>
          </div>
        </div>

        <div class="separador"></div>
      </div>
    </template>
  </div>
</template>

<style scoped>
.eventos-wrapper {
  max-width: 960px;
  margin: 0 auto;
  padding: 3rem 1.5rem;
  background: #000;
}

.titulo-eventos {
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

/* Tabs */
.tabs-bar {
  display: flex;
  flex-wrap: wrap;
  border-bottom: 1px solid #222;
  margin-bottom: 0.5rem;
}

.tab-btn {
  background: none;
  border: none;
  border-bottom: 2px solid transparent;
  color: #555;
  font-size: 0.7rem;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  cursor: pointer;
  padding: 12px 20px;
  white-space: nowrap;
  transition:
    color 0.2s,
    border-color 0.2s;
  font-family: inherit;
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: -1px;
}
.tab-btn:hover {
  color: #f7f1e8;
}
.tab-btn.activo {
  color: #f7f1e8;
  border-bottom-color: #f7f1e8;
}

.tab-count {
  font-size: 0.6rem;
  color: #444;
  background: #1a1a1a;
  padding: 1px 6px;
  letter-spacing: 0.05em;
}
.tab-btn.activo .tab-count {
  color: #666;
}

/* Mes */
.mes-grupo {
  margin-top: 2rem;
}

.mes-header {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 1rem 0 0.75rem;
}
.mes-label {
  font-size: 0.7rem;
  letter-spacing: 0.3em;
  text-transform: capitalize;
  color: #555;
  white-space: nowrap;
}
.mes-linea {
  flex: 1;
  height: 1px;
  background: #222;
}

/* Fila evento */
.evento-fila {
  display: grid;
  grid-template-columns: 120px 80px 1fr auto;
  align-items: center;
  gap: 2rem;
  padding: 1.5rem 0;
  border-top: 1px solid #1a1a1a;
  transition: background 0.15s;
}
.evento-fila:hover {
  background: rgba(255, 255, 255, 0.015);
}
.evento-fila:hover .evento-titulo {
  color: #fff;
}

.evento-fila.pasado .evento-dia-num,
.evento-fila.pasado .evento-titulo {
  color: #444;
}

/* Imagen */
.evento-img-wrapper {
  width: 120px;
  height: 120px;
  flex-shrink: 0;
  overflow: hidden;
}
.evento-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  filter: grayscale(20%);
  transition: filter 0.2s;
}
.evento-fila:hover .evento-img {
  filter: grayscale(0%);
}
.evento-img-placeholder {
  width: 100%;
  height: 100%;
  background: #1a1a1a;
}

/* Fecha */
.evento-fecha {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
}
.evento-dia-num {
  font-size: 2.75rem;
  font-weight: 700;
  line-height: 1;
  color: #f7f1e8;
  letter-spacing: -0.02em;
  transition: color 0.2s;
}
.evento-dia-nombre {
  font-size: 0.7rem;
  letter-spacing: 0.15em;
  text-transform: uppercase;
  color: #555;
  margin-top: 4px;
}

/* Info */
.evento-info {
  min-width: 0;
}

.evento-actions {
  display: flex;
  justify-content: flex-end;
}

.evento-compra {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  gap: 0.75rem;
  min-width: 150px;
}

.evento-actions:empty {
  display: none;
}

.evento-precios {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  gap: 0.15rem;
}

.evento-precio {
  font-size: 1rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  color: #f7f1e8;
}

.btn-reservar {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 0.65rem 1rem;
  background: #f7f1e8;
  color: #111;
  text-transform: uppercase;
  font-size: 0.75rem;
  letter-spacing: 0.12em;
  border-radius: 0;
  text-decoration: none;
  transition:
    background 0.2s,
    transform 0.2s;
}

.btn-reservar:hover {
  background: #e1d7c6;
  transform: translateY(-1px);
}

/* Enlace login hint (no autenticado) */
.btn-login-hint {
  font-size: 0.7rem;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: #555;
  text-decoration: none;
  white-space: nowrap;
  border-bottom: 1px solid #333;
  padding-bottom: 1px;
  transition:
    color 0.2s,
    border-color 0.2s;
}
.btn-login-hint:hover {
  color: #f7f1e8;
  border-bottom-color: #f7f1e8;
}

.evento-titulo {
  font-size: 1.25rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: #f7f1e8;
  margin: 0 0 0.4rem;
  transition: color 0.2s;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.evento-lugar {
  font-size: 0.85rem;
  color: #555;
  margin: 0;
  letter-spacing: 0.05em;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

/* Spinner */
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
  border-radius: 0;
  animation: spin 0.8s linear infinite;
}
@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}

/* Sin resultados */
.sin-resultados {
  text-align: center;
  padding: 5rem 0;
  font-size: 0.8rem;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: #444;
}

/* Responsive */
@media (max-width: 600px) {
  .eventos-wrapper {
    padding: 2rem 1rem 3rem;
  }

  .tabs-bar {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }

  .tab-btn {
    justify-content: center;
    padding: 0.9rem 0.75rem;
  }

  .evento-fila {
    grid-template-columns: 88px minmax(0, 1fr);
    grid-template-areas:
      "image date"
      "image info"
      "actions actions";
    gap: 1rem;
    padding: 1.25rem 0;
    align-items: start;
  }

  .evento-img-wrapper {
    grid-area: image;
    width: 88px;
    height: 88px;
  }

  .evento-fecha {
    grid-area: date;
    flex-direction: row;
    align-items: baseline;
    gap: 0.5rem;
  }

  .evento-info {
    grid-area: info;
  }

  .evento-actions {
    grid-area: actions;
    justify-content: flex-start;
    padding-top: 0.25rem;
  }

  .evento-compra,
  .evento-precios {
    align-items: flex-start;
  }

  .evento-dia-num {
    font-size: 2rem;
  }

  .evento-titulo {
    font-size: 1rem;
    white-space: normal;
  }

  .evento-lugar,
  .btn-login-hint {
    white-space: normal;
  }

  .btn-reservar {
    width: 100%;
  }
}

@media (max-width: 420px) {
  .tabs-bar {
    grid-template-columns: 1fr;
  }
}
</style>
