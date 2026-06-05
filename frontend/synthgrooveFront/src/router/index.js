import { createRouter, createWebHashHistory } from "vue-router";

const router = createRouter({
  history: createWebHashHistory(),
  routes: [
    { path: "/", component: () => import("@/views/home.vue") },
    {
      path: "/merchandising",
      component: () => import("@/views/merchandising.vue"),
    },
    { path: "/eventos", component: () => import("@/views/eventos.vue") },
    { path: "/releases", component: () => import("@/views/releases.vue") },
    { path: "/podcasts", component: () => import("@/views/podcast.vue") },
    { path: "/sobre", component: () => import("@/views/sobre.vue") },
    { path: "/login", component: () => import("@/components/Login.vue") },
    { path: "/registro", component: () => import("@/components/Register.vue") },
    {
      path: "/compra-exitosa",
      component: () => import("@/views/compra-exitosa.vue"),
    },
    {
      path: "/compra-cancelada",
      component: () => import("@/views/compra-cancelada.vue"),
    },
    { path: "/perfil", component: () => import("@/views/perfil.vue") },
    { path: "/privacidad", component: () => import("@/views/privacidad.vue") },
    { path: "/cookies", component: () => import("@/views/cookies.vue") },
    { path: "/aviso-legal", component: () => import("@/views/aviso-legal.vue") },
  ],
});

export default router;
