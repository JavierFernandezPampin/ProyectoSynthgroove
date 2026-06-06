<script setup lang="ts">
import { ref, onMounted } from "vue";
import { useAuthStore } from "@/stores/auth";
import { getAllPedidos } from "@/services/userService";
import type { Pedido } from "@/services/userService";

const auth = useAuthStore();
const pedidos = ref<Pedido[]>([]);
const error = ref("");

const euroFormatter = new Intl.NumberFormat("es-ES", {
  style: "currency",
  currency: "EUR",
});

function formatDate(dateStr: string): string {
  return new Date(dateStr).toLocaleString("es-ES", {
    year: "numeric",
    month: "long",
    day: "numeric",
    hour: "2-digit",
    minute: "2-digit",
  });
}

onMounted(async () => {
  if (!auth.access) return;
  try {
    pedidos.value = await getAllPedidos(auth.access);
  } catch {
    error.value = "Error al cargar los pedidos";
  }
});
</script>

<template>
  <p v-if="error" class="error-message">{{ error }}</p>

  <div v-if="pedidos.length === 0" class="empty-state">
    <p>No hay pedidos aún</p>
  </div>

  <div v-else>
    <div class="historial-resumen">
      <div class="resumen-item">
        <span class="resumen-label">Total pedidos</span>
        <span class="resumen-valor">{{ pedidos.length }}</span>
      </div>
      <div class="resumen-item">
        <span class="resumen-label">Ingresos totales</span>
        <span class="resumen-valor">{{
          euroFormatter.format(
            pedidos.reduce((acc, p) => acc + p.precio_unitario * p.cantidad, 0)
          )
        }}</span>
      </div>
    </div>

    <div class="historial-table">
      <div class="historial-header">
        <span>Usuario</span>
        <span>Producto</span>
        <span>Cant.</span>
        <span>Total</span>
        <span>Fecha</span>
      </div>
      <div v-for="p in pedidos" :key="p.id" class="historial-row">
        <span class="historial-cell">{{ p.usuario_nombre }}</span>
        <span class="historial-cell">{{ p.producto_nombre }}</span>
        <span class="historial-cell historial-center">{{ p.cantidad }}</span>
        <span class="historial-cell">{{ euroFormatter.format(p.precio_unitario * p.cantidad) }}</span>
        <span class="historial-cell historial-date">{{ formatDate(p.fecha) }}</span>
      </div>
    </div>
  </div>
</template>

<style scoped>
.error-message {
  color: #e05252;
  font-size: 0.85rem;
  margin: 0 0 1rem;
}

.empty-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 2rem 0;
  color: #999;
  text-align: center;
}

.empty-state p {
  margin: 0;
  font-size: 1rem;
}

.historial-resumen {
  display: flex;
  gap: 2rem;
  margin-bottom: 1.5rem;
}

.resumen-item {
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
}

.resumen-label {
  color: #999;
  font-size: 0.75rem;
  text-transform: uppercase;
  letter-spacing: 0.06em;
}

.resumen-valor {
  color: #f7f1e8;
  font-size: 1.3rem;
  font-weight: 600;
}

.historial-table {
  border: 1px solid #333;
  border-radius: 0;
  overflow: hidden;
}

.historial-header {
  display: grid;
  grid-template-columns: 1fr 1.2fr 0.4fr 0.8fr 1.4fr;
  padding: 0.7rem 1rem;
  background: #111;
  color: #999;
  font-size: 0.75rem;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  border-bottom: 1px solid #333;
}

.historial-row {
  display: grid;
  grid-template-columns: 1fr 1.2fr 0.4fr 0.8fr 1.4fr;
  padding: 0.8rem 1rem;
  border-bottom: 1px solid #222;
  align-items: center;
  transition: background 0.15s;
}

.historial-row:last-child {
  border-bottom: none;
}

.historial-row:hover {
  background: #111;
}

.historial-cell {
  color: #f7f1e8;
  font-size: 0.88rem;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.historial-center {
  text-align: center;
}

.historial-date {
  color: #666;
  font-size: 0.8rem;
}

@media (max-width: 720px) {
  .historial-header,
  .historial-row {
    grid-template-columns: 1fr 1fr 0.5fr 0.8fr;
  }

  .historial-cell:last-child,
  .historial-header span:last-child {
    display: none;
  }

  .historial-resumen {
    gap: 1.5rem;
  }
}
</style>
