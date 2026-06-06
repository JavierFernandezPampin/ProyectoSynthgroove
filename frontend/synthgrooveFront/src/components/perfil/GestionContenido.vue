<script setup lang="ts">
import { ref, onMounted } from "vue";
import { useAuthStore } from "@/stores/auth";
import {
  getProductos, createProducto, updateProducto, deleteProducto,
  getEventos, createEvento, updateEvento, deleteEvento,
} from "@/services/contentService";
import type { GestionProducto, GestionEvento } from "@/services/contentService";

const auth = useAuthStore();

const gestionTab = ref<"productos" | "eventos">("productos");
const gestionProductos = ref<GestionProducto[]>([]);
const gestionEventos = ref<GestionEvento[]>([]);
const gestionError = ref("");

const showProductoForm = ref(false);
const editingProductoId = ref<number | null>(null);
const productoForm = ref({ nombre: "", precio: "", categoria: "otro", imagenUrl: "" });
const productoImageFile = ref<File | null>(null);
const savingProducto = ref(false);
const deletingProductoId = ref<number | null>(null);

const showEventoForm = ref(false);
const editingEventoId = ref<number | null>(null);
const eventoForm = ref({ nombre: "", localizacion: "", fecha_release: "", precio: "", imagenUrl: "" });
const eventoImageFile = ref<File | null>(null);
const savingEvento = ref(false);
const deletingEventoId = ref<number | null>(null);

async function load() {
  if (!auth.access) return;
  try {
    [gestionProductos.value, gestionEventos.value] = await Promise.all([
      getProductos(auth.access),
      getEventos(auth.access),
    ]);
  } catch {
    gestionError.value = "Error al cargar el contenido";
  }
}

function openProductoForm() {
  editingProductoId.value = null;
  productoForm.value = { nombre: "", precio: "", categoria: "otro", imagenUrl: "" };
  productoImageFile.value = null;
  gestionError.value = "";
  showProductoForm.value = true;
}

function startEditProducto(p: GestionProducto) {
  editingProductoId.value = p.id;
  productoForm.value = { nombre: p.nombre, precio: String(p.precio), categoria: p.categoria, imagenUrl: p.imagen ?? "" };
  productoImageFile.value = null;
  gestionError.value = "";
  showProductoForm.value = true;
}

function resetProductoForm() {
  showProductoForm.value = false;
  editingProductoId.value = null;
  productoImageFile.value = null;
  gestionError.value = "";
}

async function handleSaveProducto() {
  if (!auth.access) return;
  savingProducto.value = true;
  gestionError.value = "";
  try {
    const fd = new FormData();
    fd.append("nombre", productoForm.value.nombre);
    fd.append("precio", productoForm.value.precio);
    fd.append("categoria", productoForm.value.categoria);
    if (productoImageFile.value) fd.append("imagen", productoImageFile.value);
    if (editingProductoId.value !== null) {
      const updated = await updateProducto(auth.access, editingProductoId.value, fd);
      const idx = gestionProductos.value.findIndex((p) => p.id === editingProductoId.value);
      if (idx !== -1) gestionProductos.value[idx] = updated;
    } else {
      gestionProductos.value.push(await createProducto(auth.access, fd));
    }
    resetProductoForm();
  } catch {
    gestionError.value = "Error al guardar el producto";
  } finally {
    savingProducto.value = false;
  }
}

async function handleDeleteProducto(id: number) {
  if (!auth.access) return;
  deletingProductoId.value = id;
  try {
    await deleteProducto(auth.access, id);
    gestionProductos.value = gestionProductos.value.filter((p) => p.id !== id);
  } catch {
    gestionError.value = "Error al eliminar el producto";
  } finally {
    deletingProductoId.value = null;
  }
}

function openEventoForm() {
  editingEventoId.value = null;
  eventoForm.value = { nombre: "", localizacion: "", fecha_release: "", precio: "", imagenUrl: "" };
  eventoImageFile.value = null;
  gestionError.value = "";
  showEventoForm.value = true;
}

function startEditEvento(e: GestionEvento) {
  editingEventoId.value = e.id;
  eventoForm.value = { nombre: e.nombre, localizacion: e.localizacion, fecha_release: e.fecha_release ?? "", precio: String(e.precio), imagenUrl: e.imagen ?? "" };
  eventoImageFile.value = null;
  gestionError.value = "";
  showEventoForm.value = true;
}

function resetEventoForm() {
  showEventoForm.value = false;
  editingEventoId.value = null;
  eventoImageFile.value = null;
  gestionError.value = "";
}

async function handleSaveEvento() {
  if (!auth.access) return;
  savingEvento.value = true;
  gestionError.value = "";
  try {
    const fd = new FormData();
    fd.append("nombre", eventoForm.value.nombre);
    fd.append("localizacion", eventoForm.value.localizacion);
    if (eventoForm.value.fecha_release) fd.append("fecha_release", eventoForm.value.fecha_release);
    fd.append("precio", eventoForm.value.precio);
    if (eventoImageFile.value) fd.append("imagen", eventoImageFile.value);
    if (editingEventoId.value !== null) {
      const updated = await updateEvento(auth.access, editingEventoId.value, fd);
      const idx = gestionEventos.value.findIndex((e) => e.id === editingEventoId.value);
      if (idx !== -1) gestionEventos.value[idx] = updated;
    } else {
      gestionEventos.value.push(await createEvento(auth.access, fd));
    }
    resetEventoForm();
  } catch {
    gestionError.value = "Error al guardar el evento";
  } finally {
    savingEvento.value = false;
  }
}

async function handleDeleteEvento(id: number) {
  if (!auth.access) return;
  deletingEventoId.value = id;
  try {
    await deleteEvento(auth.access, id);
    gestionEventos.value = gestionEventos.value.filter((e) => e.id !== id);
  } catch {
    gestionError.value = "Error al eliminar el evento";
  } finally {
    deletingEventoId.value = null;
  }
}

onMounted(load);
</script>

<template>
  <div class="gestion-inner">
    <div class="gestion-tabs">
      <button
        :class="['gestion-tab', { active: gestionTab === 'productos' }]"
        @click="gestionTab = 'productos'"
      >Productos</button>
      <button
        :class="['gestion-tab', { active: gestionTab === 'eventos' }]"
        @click="gestionTab = 'eventos'"
      >Eventos</button>
    </div>

    <p v-if="gestionError" class="error-message">{{ gestionError }}</p>

    <!-- PRODUCTOS -->
    <div v-if="gestionTab === 'productos'">
      <div class="gestion-actions">
        <button
          class="btn-secondary"
          @click="showProductoForm && !editingProductoId ? resetProductoForm() : openProductoForm()"
        >
          {{ showProductoForm && !editingProductoId ? "Cancelar" : "+ Añadir producto" }}
        </button>
      </div>

      <form v-if="showProductoForm" class="gestion-form" @submit.prevent="handleSaveProducto">
        <div class="form-row">
          <div class="form-group">
            <label>Nombre</label>
            <input v-model="productoForm.nombre" type="text" required />
          </div>
          <div class="form-group">
            <label>Precio (€)</label>
            <input v-model="productoForm.precio" type="number" step="0.01" min="0" required />
          </div>
        </div>
        <div class="form-row">
          <div class="form-group">
            <label>Categoría</label>
            <select v-model="productoForm.categoria">
              <option value="camiseta">Camiseta</option>
              <option value="sudadera">Sudadera</option>
              <option value="accesorio">Accesorio</option>
              <option value="otro">Otro</option>
            </select>
          </div>
          <div class="form-group">
            <label>Imagen</label>
            <input
              type="file"
              accept="image/*"
              @change="(e) => { productoImageFile = (e.target as HTMLInputElement).files?.[0] ?? null }"
            />
            <img
              v-if="productoForm.imagenUrl && !productoImageFile"
              :src="productoForm.imagenUrl"
              class="form-preview"
            />
          </div>
        </div>
        <div class="form-buttons">
          <button type="submit" class="btn-primary" :disabled="savingProducto">
            {{ savingProducto ? "Guardando..." : editingProductoId ? "Actualizar" : "Crear" }}
          </button>
          <button type="button" class="btn-cancel" @click="resetProductoForm">Cancelar</button>
        </div>
      </form>

      <div v-if="gestionProductos.length === 0 && !showProductoForm" class="empty-state">
        <p>No hay productos</p>
      </div>
      <div v-else-if="gestionProductos.length > 0" class="gestion-list">
        <div v-for="p in gestionProductos" :key="p.id" class="gestion-item">
          <img v-if="p.imagen" :src="p.imagen" class="gestion-thumb" :alt="p.nombre" />
          <div v-else class="gestion-thumb gestion-thumb-empty"></div>
          <div class="gestion-item-info">
            <span class="gestion-item-name">{{ p.nombre }}</span>
            <span class="gestion-item-meta">{{ p.categoria }} · {{ p.precio }}€</span>
          </div>
          <div class="gestion-item-actions">
            <button class="btn-edit" @click="startEditProducto(p)">Editar</button>
            <button
              class="btn-delete"
              :disabled="deletingProductoId === p.id"
              @click="handleDeleteProducto(p.id)"
            >{{ deletingProductoId === p.id ? "..." : "Eliminar" }}</button>
          </div>
        </div>
      </div>
    </div>

    <!-- EVENTOS -->
    <div v-if="gestionTab === 'eventos'">
      <div class="gestion-actions">
        <button
          class="btn-secondary"
          @click="showEventoForm && !editingEventoId ? resetEventoForm() : openEventoForm()"
        >
          {{ showEventoForm && !editingEventoId ? "Cancelar" : "+ Añadir evento" }}
        </button>
      </div>

      <form v-if="showEventoForm" class="gestion-form" @submit.prevent="handleSaveEvento">
        <div class="form-row">
          <div class="form-group">
            <label>Nombre</label>
            <input v-model="eventoForm.nombre" type="text" required />
          </div>
          <div class="form-group">
            <label>Localización</label>
            <input v-model="eventoForm.localizacion" type="text" required />
          </div>
        </div>
        <div class="form-row">
          <div class="form-group">
            <label>Fecha</label>
            <input v-model="eventoForm.fecha_release" type="date" />
          </div>
          <div class="form-group">
            <label>Precio (€)</label>
            <input v-model="eventoForm.precio" type="number" step="0.01" min="0" required />
          </div>
        </div>
        <div class="form-row">
          <div class="form-group">
            <label>Imagen</label>
            <input
              type="file"
              accept="image/*"
              @change="(e) => { eventoImageFile = (e.target as HTMLInputElement).files?.[0] ?? null }"
            />
            <img
              v-if="eventoForm.imagenUrl && !eventoImageFile"
              :src="eventoForm.imagenUrl"
              class="form-preview"
            />
          </div>
        </div>
        <div class="form-buttons">
          <button type="submit" class="btn-primary" :disabled="savingEvento">
            {{ savingEvento ? "Guardando..." : editingEventoId ? "Actualizar" : "Crear" }}
          </button>
          <button type="button" class="btn-cancel" @click="resetEventoForm">Cancelar</button>
        </div>
      </form>

      <div v-if="gestionEventos.length === 0 && !showEventoForm" class="empty-state">
        <p>No hay eventos</p>
      </div>
      <div v-else-if="gestionEventos.length > 0" class="gestion-list">
        <div v-for="e in gestionEventos" :key="e.id" class="gestion-item">
          <img v-if="e.imagen" :src="e.imagen" class="gestion-thumb" :alt="e.nombre" />
          <div v-else class="gestion-thumb gestion-thumb-empty"></div>
          <div class="gestion-item-info">
            <span class="gestion-item-name">{{ e.nombre }}</span>
            <span class="gestion-item-meta">{{ e.localizacion }}{{ e.fecha_release ? ' · ' + e.fecha_release : '' }}</span>
          </div>
          <div class="gestion-item-actions">
            <button class="btn-edit" @click="startEditEvento(e)">Editar</button>
            <button
              class="btn-delete"
              :disabled="deletingEventoId === e.id"
              @click="handleDeleteEvento(e.id)"
            >{{ deletingEventoId === e.id ? "..." : "Eliminar" }}</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.gestion-inner {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.error-message {
  color: #e05252;
  font-size: 0.85rem;
  margin: 0;
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

.gestion-tabs {
  display: flex;
  border: 1px solid #333;
  border-radius: 0;
  overflow: hidden;
  width: fit-content;
}

.gestion-tab {
  background: transparent;
  border: none;
  color: #999;
  padding: 0.55rem 1.25rem;
  font-size: 0.85rem;
  cursor: pointer;
  font-family: inherit;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  transition: all 0.2s;
}

.gestion-tab + .gestion-tab {
  border-left: 1px solid #333;
}

.gestion-tab.active {
  background: #f7f1e8;
  color: #111;
}

.gestion-tab:not(.active):hover {
  background: rgba(247, 241, 232, 0.07);
  color: #f7f1e8;
}

.gestion-actions {
  display: flex;
  justify-content: flex-end;
  margin-bottom: 1rem;
}

.gestion-form {
  background: #111;
  border: 1px solid #333;
  border-radius: 0;
  padding: 1.5rem;
  display: flex;
  flex-direction: column;
  gap: 1rem;
  margin-bottom: 1rem;
}

.form-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 0.4rem;
}

.form-group label {
  color: #f7f1e8;
  font-size: 0.85rem;
}

.form-group input,
.form-group select {
  background: #111;
  border: 1px solid #444;
  color: #f7f1e8;
  padding: 0.6rem 0.8rem;
  font-size: 0.95rem;
  border-radius: 0;
  font-family: inherit;
}

.form-group input:focus,
.form-group select:focus {
  outline: none;
  border-color: #f7f1e8;
}

.form-preview {
  margin-top: 0.5rem;
  width: 80px;
  height: 80px;
  object-fit: cover;
  border-radius: 0;
  border: 1px solid #333;
}

.form-buttons {
  display: flex;
  gap: 1rem;
  margin-top: 0.5rem;
}

.btn-primary,
.btn-secondary,
.btn-cancel {
  padding: 0.7rem 1.5rem;
  font-size: 0.95rem;
  border-radius: 0;
  cursor: pointer;
  transition: all 0.2s;
  font-family: inherit;
}

.btn-primary,
.btn-secondary {
  background: transparent;
  border: 1px solid #f7f1e8;
  color: #f7f1e8;
}

.btn-primary:hover:not(:disabled),
.btn-secondary:hover {
  background: rgba(247, 241, 232, 0.1);
}

.btn-primary:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.btn-cancel {
  background: transparent;
  border: 1px solid #555;
  color: #999;
}

.btn-cancel:hover {
  border-color: #f7f1e8;
  color: #f7f1e8;
}

.gestion-list {
  display: flex;
  flex-direction: column;
  border: 1px solid #333;
  border-radius: 0;
  overflow: hidden;
}

.gestion-item {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 0.85rem 1rem;
  border-bottom: 1px solid #222;
  transition: background 0.15s;
}

.gestion-item:last-child {
  border-bottom: none;
}

.gestion-item:hover {
  background: #111;
}

.gestion-thumb {
  width: 52px;
  height: 52px;
  object-fit: cover;
  border-radius: 0;
  border: 1px solid #333;
  flex-shrink: 0;
}

.gestion-thumb-empty {
  background: #222;
}

.gestion-item-info {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
  min-width: 0;
}

.gestion-item-name {
  color: #f7f1e8;
  font-size: 0.9rem;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.gestion-item-meta {
  color: #666;
  font-size: 0.8rem;
}

.gestion-item-actions {
  display: flex;
  gap: 0.5rem;
  flex-shrink: 0;
}

.btn-edit {
  background: transparent;
  border: 1px solid #555;
  color: #aaa;
  padding: 0.35rem 0.75rem;
  font-size: 0.8rem;
  border-radius: 0;
  cursor: pointer;
  font-family: inherit;
  transition: all 0.2s;
}

.btn-edit:hover {
  border-color: #f7f1e8;
  color: #f7f1e8;
}

.btn-delete {
  background: transparent;
  border: 1px solid #e05252;
  color: #e05252;
  padding: 0.4rem 0.85rem;
  font-size: 0.8rem;
  border-radius: 0;
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
  .form-row {
    grid-template-columns: 1fr;
  }

  .gestion-item-meta {
    display: none;
  }
}
</style>
