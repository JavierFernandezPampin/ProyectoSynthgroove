<script setup lang="ts">
import { ref, onMounted } from "vue";
import { useAuthStore } from "@/stores/auth";
import {
  getUserProfile,
  getPedidos,
  changePassword,
  getUsuarios,
  deleteUsuario,
  changeUserRole,
  getAllPedidos,
} from "@/services/userService";
import type { UserProfile, Pedido } from "@/services/userService";
import {
  getProductos,
  createProducto,
  updateProducto,
  deleteProducto,
  getEventos,
  createEvento,
  updateEvento,
  deleteEvento,
} from "@/services/contentService";
import type { GestionProducto, GestionEvento } from "@/services/contentService";

const auth = useAuthStore();
const userProfile = ref<UserProfile | null>(null);
const pedidos = ref<Pedido[]>([]);
const loading = ref(true);
const error = ref("");

// Admin
const usuarios = ref<UserProfile[]>([]);
const deletingId = ref<number | null>(null);
const todosLosPedidos = ref<Pedido[]>([]);
const changingRoleId = ref<number | null>(null);

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

async function loadUsuarios() {
  if (!auth.access) return;
  try {
    usuarios.value = await getUsuarios(auth.access);
  } catch {
    error.value = "Error al cargar los usuarios";
  }
}

async function handleDeleteUsuario(id: number) {
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

// Gestión de contenido (admin + gestor)
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

async function loadGestion() {
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

// Form states
const showChangePasswordForm = ref(false);
const oldPassword = ref("");
const newPassword = ref("");
const confirmPassword = ref("");
const changingPassword = ref(false);
const passwordError = ref("");
const passwordSuccess = ref("");

// Euro formatter
const euroFormatter = new Intl.NumberFormat("es-ES", {
  style: "currency",
  currency: "EUR",
});

async function loadUserData() {
  if (!auth.access) {
    loading.value = false;
    return;
  }

  try {
    userProfile.value = await getUserProfile(auth.access);
    const rol = userProfile.value?.rol;
    if (rol === "admin") {
      await Promise.all([loadUsuarios(), loadGestion(), getAllPedidos(auth.access).then(p => { todosLosPedidos.value = p; })]);
    } else if (rol === "gestor") {
      await loadGestion();
    } else {
      pedidos.value = await getPedidos(auth.access);
    }
  } catch (err: any) {
    error.value = err.message || "Error al cargar los datos del perfil";
  } finally {
    loading.value = false;
  }
}

async function handleChangePassword() {
  passwordError.value = "";
  passwordSuccess.value = "";

  if (!oldPassword.value || !newPassword.value || !confirmPassword.value) {
    passwordError.value = "Por favor completa todos los campos";
    return;
  }

  if (newPassword.value !== confirmPassword.value) {
    passwordError.value = "Las contraseñas no coinciden";
    return;
  }

  changingPassword.value = true;
  try {
    await changePassword(auth.access!, oldPassword.value, newPassword.value);
    passwordSuccess.value = "Contraseña cambiada exitosamente";
    oldPassword.value = "";
    newPassword.value = "";
    confirmPassword.value = "";
    showChangePasswordForm.value = false;
  } catch (err: any) {
    passwordError.value = err.message || "Error al cambiar la contraseña";
  } finally {
    changingPassword.value = false;
  }
}

function formatDate(dateStr: string): string {
  const date = new Date(dateStr);
  return date.toLocaleString("es-ES", {
    year: "numeric",
    month: "long",
    day: "numeric",
    hour: "2-digit",
    minute: "2-digit",
  });
}

onMounted(() => {
  loadUserData();
});
</script>

<template>
  <div class="perfil-wrapper">
    <div class="perfil-container">
      <!-- No autenticado -->
      <div v-if="!auth.isAuthenticated && !loading" class="no-auth">
        <div class="no-auth-content">
          <h1 class="no-auth-title">Inicia sesión para entrar en tu perfil</h1>
          <p class="no-auth-subtitle">
            Accede a tu perfil para ver tus pedidos y gestionar tu cuenta
          </p>
          <router-link to="/login" class="btn-primary">
            Ir a iniciar sesión
          </router-link>
        </div>
      </div>

      <!-- Loading -->
      <div v-else-if="loading" class="loading">
        <div class="loading-spinner"></div>
        <p>Cargando perfil...</p>
      </div>

      <!-- Autenticado -->
      <div
        v-else-if="auth.isAuthenticated && userProfile"
        class="perfil-content"
      >
        <!-- Sección de información del usuario -->
        <section class="user-section">
          <h2 class="section-title">Mi Perfil</h2>

          <div class="user-info">
            <div class="info-item">
              <label class="info-label">Usuario</label>
              <p class="info-value">{{ userProfile.usuario }}</p>
            </div>

            <div class="info-item">
              <label class="info-label">Email</label>
              <p class="info-value">{{ userProfile.mail }}</p>
            </div>

            <div v-if="userProfile.nombre" class="info-item">
              <label class="info-label">Nombre</label>
              <p class="info-value">{{ userProfile.nombre }}</p>
            </div>

            <div v-if="userProfile.apellido" class="info-item">
              <label class="info-label">Apellido</label>
              <p class="info-value">{{ userProfile.apellido }}</p>
            </div>

            <div class="info-item">
              <label class="info-label">Rol</label>
              <p class="info-value">{{ userProfile.rol }}</p>
            </div>
          </div>

          <!-- Cambiar contraseña -->
          <div class="change-password-section">
            <button
              v-if="!showChangePasswordForm"
              class="btn-secondary"
              @click="showChangePasswordForm = true"
            >
              Cambiar Contraseña
            </button>

            <form
              v-else
              class="change-password-form"
              @submit.prevent="handleChangePassword"
            >
              <div class="form-group">
                <label for="old-password">Contraseña Actual</label>
                <input
                  id="old-password"
                  v-model="oldPassword"
                  type="password"
                  placeholder="••••••••"
                  required
                />
              </div>

              <div class="form-group">
                <label for="new-password">Nueva Contraseña</label>
                <input
                  id="new-password"
                  v-model="newPassword"
                  type="password"
                  placeholder="••••••••"
                  required
                />
              </div>

              <div class="form-group">
                <label for="confirm-password">Confirmar Nueva Contraseña</label>
                <input
                  id="confirm-password"
                  v-model="confirmPassword"
                  type="password"
                  placeholder="••••••••"
                  required
                />
              </div>

              <p v-if="passwordError" class="error-message">
                {{ passwordError }}
              </p>
              <p v-if="passwordSuccess" class="success-message">
                {{ passwordSuccess }}
              </p>

              <div class="form-buttons">
                <button
                  type="submit"
                  :disabled="changingPassword"
                  class="btn-primary"
                >
                  {{ changingPassword ? "Cambiando..." : "Cambiar Contraseña" }}
                </button>
                <button
                  type="button"
                  class="btn-cancel"
                  @click="showChangePasswordForm = false"
                >
                  Cancelar
                </button>
              </div>
            </form>
          </div>
        </section>

        <!-- Panel admin: lista de usuarios -->
        <section v-if="userProfile.rol === 'admin'" class="orders-section">
          <h2 class="section-title">Gestión de Usuarios</h2>

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
            <div
              v-for="u in usuarios"
              :key="u.id"
              class="admin-table-row"
            >
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
                  @click="handleDeleteUsuario(u.id)"
                >
                  {{ deletingId === u.id ? "..." : "Eliminar" }}
                </button>
              </span>
            </div>
          </div>
        </section>

        <!-- Historial de pedidos (solo admin) -->
        <section v-if="userProfile.rol === 'admin'" class="orders-section">
          <h2 class="section-title">Historial de Pedidos</h2>

          <div v-if="todosLosPedidos.length === 0" class="empty-state">
            <p>No hay pedidos aún</p>
          </div>

          <div v-else>
            <div class="historial-resumen">
              <div class="resumen-item">
                <span class="resumen-label">Total pedidos</span>
                <span class="resumen-valor">{{ todosLosPedidos.length }}</span>
              </div>
              <div class="resumen-item">
                <span class="resumen-label">Ingresos totales</span>
                <span class="resumen-valor">{{
                  euroFormatter.format(
                    todosLosPedidos.reduce((acc, p) => acc + p.precio_unitario * p.cantidad, 0)
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
              <div v-for="p in todosLosPedidos" :key="p.id" class="historial-row">
                <span class="historial-cell">{{ p.usuario_nombre }}</span>
                <span class="historial-cell">{{ p.producto_nombre }}</span>
                <span class="historial-cell historial-center">{{ p.cantidad }}</span>
                <span class="historial-cell">{{ euroFormatter.format(p.precio_unitario * p.cantidad) }}</span>
                <span class="historial-cell historial-date">{{ formatDate(p.fecha) }}</span>
              </div>
            </div>
          </div>
        </section>

        <!-- Gestión de contenido (admin + gestor) -->
        <section
          v-if="userProfile.rol === 'admin' || userProfile.rol === 'gestor'"
          class="gestion-section"
        >
          <h2 class="section-title">Gestión de Contenido</h2>

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

          <p v-if="gestionError" class="error-message gestion-error">{{ gestionError }}</p>

          <!-- ── PRODUCTOS ── -->
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

          <!-- ── EVENTOS ── -->
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
        </section>

        <!-- Sección de pedidos (suscriptores) -->
        <section v-if="userProfile.rol === 'suscriptor'" class="orders-section">
          <h2 class="section-title">Mis Pedidos</h2>

          <div v-if="pedidos.length === 0" class="empty-state">
            <p>No tienes pedidos aún</p>
            <router-link to="/merchandising" class="btn-secondary">
              Explorar Merchandising
            </router-link>
          </div>

          <div v-else class="orders-grid">
            <div v-for="pedido in pedidos" :key="pedido.id" class="order-card">
              <div class="order-header">
                <h3 class="order-title">{{ pedido.producto_nombre }}</h3>
                <span class="order-date">{{ formatDate(pedido.fecha) }}</span>
              </div>

              <div v-if="pedido.producto_imagen" class="order-image">
                <img
                  :src="pedido.producto_imagen"
                  :alt="pedido.producto_nombre"
                />
              </div>

              <div class="order-details">
                <div class="detail-item">
                  <span class="detail-label">Cantidad:</span>
                  <span class="detail-value">{{ pedido.cantidad }}</span>
                </div>
                <div class="detail-item">
                  <span class="detail-label">Precio unitario:</span>
                  <span class="detail-value">
                    {{ euroFormatter.format(pedido.precio_unitario) }}
                  </span>
                </div>
                <div class="detail-item total">
                  <span class="detail-label">Total:</span>
                  <span class="detail-value">
                    {{
                      euroFormatter.format(
                        pedido.precio_unitario * pedido.cantidad,
                      )
                    }}
                  </span>
                </div>
              </div>
            </div>
          </div>
        </section>
      </div>

      <!-- Error general -->
      <div v-if="error && auth.isAuthenticated" class="error-container">
        <p class="error-message">{{ error }}</p>
      </div>
    </div>
  </div>
</template>

<style scoped>
.perfil-wrapper {
  flex: 1;
  display: flex;
  justify-content: center;
  align-items: flex-start;
  min-height: calc(100vh - 200px);
  background: #000;
  padding: 2rem 1rem 3rem;
  font-family: "Space Grotesk", "Avenir Next", "Trebuchet MS", sans-serif;
}

.perfil-container {
  width: 100%;
  max-width: 1000px;
}

/* No autenticado */
.no-auth {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 60vh;
}

.no-auth-content {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1.5rem;
  text-align: center;
}

.no-auth-title {
  font-size: 2rem;
  color: #f7f1e8;
  margin: 0;
  max-width: 30ch;
}

.no-auth-subtitle {
  color: #999;
  font-size: 1rem;
  margin: 0;
  max-width: 50ch;
}

/* Loading */
.loading {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  min-height: 60vh;
  gap: 1rem;
}

.loading-spinner {
  width: 40px;
  height: 40px;
  border: 2px solid #333;
  border-top: 2px solid #f7f1e8;
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
}

@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}

.loading p {
  color: #f7f1e8;
  font-size: 0.95rem;
}

/* Contenido autenticado */
.perfil-content {
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

section {
  background: #1a1a1a;
  border: 1px solid #333;
  border-radius: 12px;
  padding: 2rem;
}

.section-title {
  color: #f7f1e8;
  font-size: 1.3rem;
  margin: 0 0 1.5rem 0;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

/* Información del usuario */
.user-info {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.5rem;
  margin-bottom: 2rem;
}

.info-item {
  display: flex;
  flex-direction: column;
  gap: 0.4rem;
}

.info-label {
  color: #999;
  font-size: 0.85rem;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.info-value {
  color: #f7f1e8;
  font-size: 1rem;
  margin: 0;
  word-break: break-all;
}

/* Cambiar contraseña */
.change-password-section {
  border-top: 1px solid #333;
  padding-top: 1.5rem;
}

.change-password-form {
  display: flex;
  flex-direction: column;
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

.form-group input {
  background: #111;
  border: 1px solid #444;
  color: #f7f1e8;
  padding: 0.6rem 0.8rem;
  font-size: 0.95rem;
  border-radius: 4px;
}

.form-group input:focus {
  outline: none;
  border-color: #f7f1e8;
}

.form-buttons {
  display: flex;
  gap: 1rem;
  margin-top: 1rem;
}

/* Buttons */
.btn-primary,
.btn-secondary,
.btn-cancel {
  padding: 0.7rem 1.5rem;
  font-size: 0.95rem;
  border-radius: 4px;
  cursor: pointer;
  transition: all 0.2s;
  font-family: "Space Grotesk", "Avenir Next", "Trebuchet MS", sans-serif;
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

/* Mensajes */
.error-message {
  color: #e05252;
  font-size: 0.85rem;
  margin: 0;
}

.success-message {
  color: #4ade80;
  font-size: 0.85rem;
  margin: 0;
}

/* Sección de pedidos */
.orders-section {
  padding: 2rem;
}

.empty-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1.5rem;
  padding: 2rem 0;
  color: #999;
  text-align: center;
}

.empty-state p {
  margin: 0;
  font-size: 1rem;
}

.orders-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 1.5rem;
}

.order-card {
  border: 1px solid #333;
  border-radius: 8px;
  overflow: hidden;
  transition: border-color 0.2s;
}

.order-card:hover {
  border-color: #555;
}

.order-header {
  padding: 1rem;
  border-bottom: 1px solid #333;
}

.order-title {
  color: #f7f1e8;
  font-size: 0.95rem;
  margin: 0;
  word-break: break-word;
}

.order-date {
  color: #666;
  font-size: 0.8rem;
}

.order-image {
  width: 100%;
  aspect-ratio: 1;
  overflow: hidden;
  background: #111;
}

.order-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.order-details {
  padding: 1rem;
  display: flex;
  flex-direction: column;
  gap: 0.8rem;
}

.detail-item {
  display: flex;
  justify-content: space-between;
  color: #999;
  font-size: 0.9rem;
}

.detail-item.total {
  border-top: 1px solid #333;
  padding-top: 0.8rem;
  color: #f7f1e8;
  font-weight: 600;
}

.detail-label {
  display: block;
}

.detail-value {
  display: block;
  color: #f7f1e8;
}

.detail-item.total .detail-value {
  color: #f7f1e8;
}

/* Historial de pedidos (admin) */
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
  border-radius: 8px;
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

/* Gestión de contenido */
.gestion-section {
  background: #1a1a1a;
  border: 1px solid #333;
  border-radius: 12px;
  padding: 2rem;
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.gestion-tabs {
  display: flex;
  gap: 0;
  border: 1px solid #333;
  border-radius: 6px;
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

.gestion-error {
  margin: 0;
}

.gestion-actions {
  display: flex;
  justify-content: flex-end;
}

.gestion-form {
  background: #111;
  border: 1px solid #333;
  border-radius: 8px;
  padding: 1.5rem;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.form-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
}

.form-preview {
  margin-top: 0.5rem;
  width: 80px;
  height: 80px;
  object-fit: cover;
  border-radius: 4px;
  border: 1px solid #333;
}

.gestion-list {
  display: flex;
  flex-direction: column;
  gap: 0;
  border: 1px solid #333;
  border-radius: 8px;
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
  border-radius: 4px;
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
  border-radius: 4px;
  cursor: pointer;
  font-family: inherit;
  transition: all 0.2s;
}

.btn-edit:hover {
  border-color: #f7f1e8;
  color: #f7f1e8;
}

@media (max-width: 600px) {
  .form-row {
    grid-template-columns: 1fr;
  }

  .gestion-item-meta {
    display: none;
  }
}

/* Admin tabla */
.admin-users-table {
  display: flex;
  flex-direction: column;
  gap: 0;
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
  .admin-table-header {
    grid-template-columns: 1fr 0.7fr 100px;
  }

  .admin-table-row {
    grid-template-columns: 1fr 0.7fr 100px;
  }

  .admin-cell-email {
    display: none;
  }
}

/* Error container */
.error-container {
  background: rgba(224, 82, 82, 0.1);
  border: 1px solid #e05252;
  border-radius: 12px;
  padding: 1.5rem;
  text-align: center;
}

.error-container .error-message {
  margin: 0;
}

/* Responsive */
@media (max-width: 720px) {
  .perfil-wrapper {
    padding: 1rem 0.5rem 2rem;
  }

  section {
    padding: 1.5rem;
  }

  .section-title {
    font-size: 1.1rem;
  }

  .user-info {
    grid-template-columns: 1fr;
  }

  .orders-grid {
    grid-template-columns: 1fr;
  }

  .form-buttons {
    flex-direction: column;
  }

  .form-buttons button {
    width: 100%;
  }

  .no-auth-title {
    font-size: 1.5rem;
  }
}
</style>
