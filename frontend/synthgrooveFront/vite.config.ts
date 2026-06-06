import { fileURLToPath, URL } from "node:url";

import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";
import vueDevTools from "vite-plugin-vue-devtools";

const apiProxyTarget = process.env.VITE_API_PROXY_TARGET || "http://localhost:8000";

export default defineConfig({
  plugins: [vue(), ...(process.env.NODE_ENV !== "production" ? [vueDevTools()] : [])],
  resolve: {
    alias: {
      "@": fileURLToPath(new URL("./src", import.meta.url)),
    },
  },
  server: {
    proxy: {
      "/api": { target: apiProxyTarget, changeOrigin: true },
      "/media": { target: apiProxyTarget, changeOrigin: true },
    },
  },
});
