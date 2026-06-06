<script setup lang="ts">
import { ref, onMounted } from "vue";
import { useAuthStore } from "@/stores/auth";
import { getUsuarios, deleteUsuario, changeUserRole } from "@/services/userService";
import type { UserProfile } from "@/services/userService";

const auth = useAuthStore();
const usuarios = ref<UserProfile[]>([]);
const deletingId = ref<number | null>(null);
const changingRoleId = ref<number | null>(null);
const error = ref("");

async function load() {
  if (!auth.access) return;
  try {
    usuarios.value = await getUsuarios(auth.access);
  } catch {
    error.value = "Error al cargar los usuarios";
  }
}

async function handleChangeRole(id: number, rolActual: string) {
  if (!auth.access) return;
  const nuevoRol = rolActual === "suscriptor" ? "gestor" : "suscriptor";
  changingRoleId.value = id;
  try {
    const updated = await changeUserRole(auth.access, id, nuevoRol);
    const idx = usuarios.value.findIndex((u) => u.id === id);
    if (idx !== -1) usuarios.value[idx] = updated;
  } catch {
    error.value = "Error al cambiar el rol";
  } finally {
    changingRoleId.value = null;
  }
}

async function handleDelete(id: number) {
  if (!auth.access) return;
  deletingId.value = id;
  try {
    await deleteUsuario(auth.access, id);
    usuarios.value = usuarios.value.filter((u) => u.id !== id);
  } catch {
    error.value = "Error al eliminar el usuario";
  } finally {
    deletingId.value = null;
  }
}

onMounted(load);
</script>

<template>
  <p v-if="error" class="error-message">{{ error }}</p>

  <div v-if="usuarios.length === 0" class="empty-state">
    <p>No hay usuarios registrados</p>
  </div>

  <div v-else class="admin-users-table">
    <div class="admin-table-header">
      <span>Usuario</span>
      <span>Email</span>
      <span>Rol</span>
      <span></span>
    </div>
    <div v-for="u in usuarios" :key="u.id" class="admin-table-row">
      <span class="admin-cell">{{ u.usuario }}</span>
      <span class="admin-cell admin-cell-email">{{ u.mail }}</span>
      <span class="admin-cell">
        <span class="rol-badge">{{ u.rol }}</span>
      </span>
      <span class="admin-cell admin-cell-action">
        <button
          class="btn-role"
          :disabled="changingRoleId === u.id"
          @click="handleChangeRole(u.id, u.rol)"
        >
          {{ changingRoleId === u.id ? "..." : u.rol === "suscriptor" ? "→ Gestor" : "→ Suscriptor" }}
        </button>
        <button
          class="btn-delete"
          :disabled="deletingId === u.id"
          @click="handleDelete(u.id)"
        >
          {{ deletingId === u.id ? "..." : "Eliminar" }}
        </button>
      </span>
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

.admin-users-table {
  display: flex;
  flex-direction: column;
  border: 1px solid #333;
  border-radius: 8px;
  overflow: hidden;
}

.admin-table-header {
  display: grid;
  grid-template-columns: 1fr 1.5fr 0.7fr 200px;
  padding: 0.75rem 1rem;
  background: #111;
  color: #999;
  font-size: 0.75rem;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  border-bottom: 1px solid #333;
}

.admin-table-row {
  display: grid;
  grid-template-columns: 1fr 1.5fr 0.7fr 200px;
  padding: 0.85rem 1rem;
  border-bottom: 1px solid #222;
  align-items: center;
  transition: background 0.15s;
}

.admin-table-row:last-child {
  border-bottom: none;
}

.admin-table-row:hover {
  background: #111;
}

.admin-cell {
  color: #f7f1e8;
  font-size: 0.9rem;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.admin-cell-email {
  color: #999;
  font-size: 0.85rem;
}

.admin-cell-action {
  display: flex;
  justify-content: flex-end;
  gap: 0.5rem;
}

.rol-badge {
  background: rgba(247, 241, 232, 0.08);
  border: 1px solid #444;
  border-radius: 4px;
  padding: 0.2rem 0.5rem;
  font-size: 0.75rem;
  color: #aaa;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.btn-role {
  background: transparent;
  border: 1px solid #555;
  color: #aaa;
  padding: 0.4rem 0.75rem;
  font-size: 0.8rem;
  border-radius: 4px;
  cursor: pointer;
  font-family: inherit;
  transition: all 0.2s;
  white-space: nowrap;
}

.btn-role:hover:not(:disabled) {
  border-color: #f7f1e8;
  color: #f7f1e8;
}

.btn-role:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.btn-delete {
  background: transparent;
  border: 1px solid #e05252;
  color: #e05252;
  padding: 0.4rem 0.85rem;
  font-size: 0.8rem;
  border-radius: 4px;
  cursor: pointer;
  font-family: inherit;
  transition: all 0.2s;
  white-space: nowrap;
}

.btn-delete:hover:not(:disabled) {
  background: rgba(224, 82, 82, 0.1);
}

.btn-delete:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

@media (max-width: 600px) {
  .admin-table-header,
  .admin-table-row {
    grid-template-columns: 1fr 0.7fr 100px;
  }

  .admin-cell-email {
    display: none;
  }
}
</style>
