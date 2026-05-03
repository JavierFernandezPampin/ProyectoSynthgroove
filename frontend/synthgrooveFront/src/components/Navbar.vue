<script setup lang="ts">
import { useAuthStore } from "@/stores/auth.js";
import { useRouter } from "vue-router";

const logoBlanco = new URL("../assets/img/logoBlanco.png", import.meta.url)
  .href;

const auth = useAuthStore();
const router = useRouter();

async function handleLogout() {
  await auth.logout();
  router.push("/login");
}
</script>

<template>
  <header class="brand-header" aria-label="Identidad del colectivo">
    <nav class="nav-auth">
      <template v-if="auth.isAuthenticated">
        <span class="nav-usuario">LOGIN AS: {{ auth.usuario }}</span>
        <button class="nav-btn" @click="handleLogout">Cerrar sesión</button>
      </template>
      <template v-else>
        <router-link class="nav-btn" to="/login">Iniciar sesión</router-link>
      </template>
    </nav>

    <router-link class="brand-center brand-home" to="/" aria-label="Volver al inicio">
      <img
        class="brand-logo"
        :src="logoBlanco"
        alt="Logo blanco del colectivo"
      />
    </router-link>

    <div class="brand-spacer" aria-hidden="true"></div>
  </header>
</template>

<style scoped>
.brand-header {
  display: grid;
  grid-template-columns: 1fr auto 1fr;
  align-items: center;
  padding: 10px 20px;
  background: black;
  font-family: "Space Grotesk", "Avenir Next", "Trebuchet MS", sans-serif;
}
.brand-center {
  display: flex;
  justify-content: center;
}
.brand-home {
  text-decoration: none;
}
.brand-logo {
  width: 70px;
  height: auto;
  object-fit: contain;
}
.nav-auth {
  display: flex;
  align-items: center;
  gap: 1rem;
  justify-self: start;
}
.nav-usuario {
  color: #f7f1e8;
  font-size: 0.9rem;
  white-space: nowrap;
}
.nav-btn {
  background: transparent;
  border: 1px solid #f7f1e8;
  color: #f7f1e8;
  padding: 0.4rem 1rem;
  cursor: pointer;
  font-size: 0.85rem;
  text-decoration: none;
  transition: background 0.2s;
}
.nav-btn:hover {
  background: rgba(247, 241, 232, 0.1);
}
.brand-spacer {
  justify-self: end;
}

@media (max-width: 640px) {
  .brand-header {
    grid-template-columns: 1fr;
    gap: 0.8rem;
  }
  .nav-auth,
  .brand-center,
  .brand-spacer {
    justify-self: center;
  }
  .nav-auth {
    order: 2;
  }
  .brand-center {
    order: 1;
  }
  .brand-spacer {
    display: none;
  }
}
</style>
