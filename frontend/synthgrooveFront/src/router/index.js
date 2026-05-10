// archivo que sirve para configurar que pagina mostrar en cada ruta
import { createRouter, createWebHistory } from "vue-router";
import { useAuthStore } from "@/stores/auth";
import HomeView from "@/views/home.vue";
import MerchandisingView from "@/views/merchandising.vue";
import EventosView from "@/views/eventos.vue";
import ReleasesView from "@/views/releases.vue";
import PodcastView from "@/views/podcast.vue";
import SobreView from "@/views/sobre.vue";
import Login from "@/components/Login.vue";
import Register from "@/components/Register.vue";

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: "/", component: HomeView },
    { path: "/merchandising", component: MerchandisingView },
    { path: "/eventos", component: EventosView },
    { path: "/releases", component: ReleasesView },
    { path: "/podcasts", component: PodcastView },
    { path: "/sobre", component: SobreView },
    { path: "/login", component: Login, meta: { guestOnly: true } },
    { path: "/registro", component: Register, meta: { guestOnly: true } },
  ],
});

router.beforeEach((to, from, next) => {
  const auth = useAuthStore();
  if (to.meta.requiresAuth && !auth.isAuthenticated) {
    next("/login");
  } else if (to.meta.guestOnly && auth.isAuthenticated) {
    next("/");
  } else {
    next();
  }
});

export default router;
