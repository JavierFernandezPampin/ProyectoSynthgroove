<script setup lang="ts">
import { useAuthStore } from "@/stores/auth.js";
import { useRoute, useRouter } from "vue-router";

const logoBlanco = new URL("../assets/img/logoBlanco.png", import.meta.url)
  .href;

const auth = useAuthStore();
const route = useRoute();
const router = useRouter();
const navItems = [
  { label: "Inicio", path: "/" },
  { label: "Merchandising", path: "/merchandising" },
  { label: "Eventos", path: "/eventos" },
  { label: "Releases", path: "/releases" },
  { label: "Podcasts", path: "/podcasts" },
  { label: "Sobre", path: "/sobre" },
];

async function handleLogout() {
  await auth.logout();
  router.push("/login");
}
</script>

<template>
  <header class="brand-header">
    <div class="brand-top">
      <div class="nav-auth">
        <template v-if="auth.isAuthenticated">
          <span class="nav-usuario">LOGGED AS: {{ auth.usuario }}</span>
          <button class="btn btn-outline-light btn-sm" @click="handleLogout">
            Cerrar sesion
          </button>
        </template>
        <template v-else>
          <router-link class="btn btn-outline-light btn-sm" to="/login">
            Iniciar sesion
          </router-link>
        </template>
      </div>

      <router-link
        class="brand-center brand-home"
        to="/"
        aria-label="Volver al inicio"
      >
        <img
          class="brand-logo"
          :src="logoBlanco"
          alt="Logo blanco del colectivo"
        />
      </router-link>

      <div class="brand-spacer">
        <router-link
          v-if="auth.isAuthenticated"
          to="/perfil"
          class="profile-icon"
          aria-label="Ir a mi perfil"
          title="Mi perfil"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round"
          >
            <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
            <circle cx="12" cy="7" r="4"></circle>
          </svg>
        </router-link>
      </div>
    </div>

    <nav class="section-nav" aria-label="Secciones principales">
      <ul class="section-nav__list">
        <li v-for="item in navItems" :key="item.path">
          <router-link
            :to="item.path"
            class="section-nav__link"
            :aria-current="route.path === item.path ? 'page' : undefined"
          >
            {{ item.label }}
          </router-link>
        </li>
      </ul>
    </nav>
  </header>
</template>

<style scoped>
.brand-header {
  position: sticky;
  top: 0;
  z-index: 20;
  width: 100%;
  background: rgba(0, 0, 0, 0.96);
  backdrop-filter: blur(14px);
  border-bottom: 1px solid #181818;
  font-family: "Space Grotesk", "Avenir Next", "Trebuchet MS", sans-serif;
}

.brand-top {
  display: grid;
  grid-template-columns: 1fr auto 1fr;
  align-items: center;
  gap: 1rem;
  padding: 0.9rem 1.4rem 0.55rem;
}

.brand-center {
  display: flex;
  justify-content: center;
}

.brand-home {
  text-decoration: none;
}

.brand-logo {
  width: 72px;
  height: auto;
  object-fit: contain;
}

.nav-auth {
  display: flex;
  align-items: center;
  gap: 0.85rem;
  flex-wrap: wrap;
  justify-self: start;
}

.nav-usuario {
  color: #f7f1e8;
  font-size: 0.72rem;
  letter-spacing: 0.18em;
  white-space: nowrap;
}

.brand-spacer {
  justify-self: end;
  display: flex;
  align-items: center;
  justify-content: flex-end;
}

.profile-icon {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 2.2rem;
  height: 2.2rem;
  color: #8d8d8d;
  text-decoration: none;
  border: 1px solid transparent;
  border-radius: 50%;
  transition:
    color 0.2s ease,
    border-color 0.2s ease,
    background 0.2s ease,
    transform 0.2s ease;
}

.profile-icon:hover {
  color: #f7f1e8;
  border-color: #2d2d2d;
  background: rgba(247, 241, 232, 0.05);
  transform: scale(1.08);
}

.profile-icon:focus-visible {
  outline: 2px solid #f7f1e8;
  outline-offset: 2px;
  color: #f7f1e8;
}

.profile-icon svg {
  width: 1.2rem;
  height: 1.2rem;
  stroke-width: 2;
}

.section-nav {
  padding: 0 1.25rem 1rem;
}

.section-nav__list {
  list-style: none;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-wrap: wrap;
  gap: 0.55rem 0.75rem;
  margin: 0;
  padding: 0;
}

.section-nav__link {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-height: 2.5rem;
  padding: 0.65rem 1rem;
  border: 1px solid transparent;
  border-radius: 999px;
  color: #8d8d8d;
  font-size: 0.76rem;
  font-weight: 600;
  letter-spacing: 0.18em;
  text-decoration: none;
  text-transform: uppercase;
  transition:
    color 0.2s ease,
    border-color 0.2s ease,
    background 0.2s ease,
    transform 0.2s ease;
}

.section-nav__link:hover {
  color: #f7f1e8;
  border-color: #2d2d2d;
  background: rgba(247, 241, 232, 0.05);
  transform: translateY(-1px);
}

.section-nav__link:focus-visible {
  outline: 2px solid #f7f1e8;
  outline-offset: 3px;
  color: #f7f1e8;
}

.section-nav__link[aria-current="page"] {
  color: #111;
  background: #f7f1e8;
  border-color: #f7f1e8;
}

@media (max-width: 780px) {
  .brand-top {
    grid-template-columns: 1fr;
    padding-bottom: 0.85rem;
    text-align: center;
  }

  .nav-auth,
  .brand-center,
  .brand-spacer {
    justify-self: center;
  }

  .nav-auth {
    order: 2;
    justify-content: center;
    width: 100%;
  }

  .brand-center {
    order: 1;
  }

  .brand-spacer {
    order: 3;
    margin-top: 0.5rem;
  }

  .section-nav {
    padding-top: 0.1rem;
  }

  .section-nav__list {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }

  .section-nav__link {
    width: 100%;
    min-height: 2.9rem;
    padding-inline: 0.75rem;
    letter-spacing: 0.12em;
  }

  .nav-usuario {
    white-space: normal;
    text-align: center;
  }
}

@media (max-width: 480px) {
  .brand-top {
    padding-inline: 1rem;
  }

  .section-nav {
    padding-inline: 1rem;
  }

  .section-nav__list {
    grid-template-columns: 1fr;
  }

  .brand-logo {
    width: 60px;
  }

  .nav-auth {
    gap: 0.6rem;
  }

  .section-nav__link {
    min-height: 2.65rem;
    font-size: 0.7rem;
  }
}
</style>
