import { defineStore } from "pinia";
const API_URL = import.meta.env.VITE_API_URL ?? "";

async function parseResponseBody(res) {
  const text = await res.text();

  if (!text) {
    return null;
  }

  try {
    return JSON.parse(text);
  } catch {
    return { raw: text };
  }
}

function getErrorMessage(data, fallback) {
  if (!data) {
    return fallback;
  }

  if (typeof data.error === "string" && data.error.trim()) {
    return data.error;
  }

  if (typeof data.detail === "string" && data.detail.trim()) {
    return data.detail;
  }

  if (typeof data.raw === "string" && data.raw.trim()) {
    return data.raw;
  }

  return fallback;
}

export const useAuthStore = defineStore("auth", {
  state: () => ({
    access: localStorage.getItem("access") || null,
    refresh: localStorage.getItem("refresh") || null,
    usuario: localStorage.getItem("usuario") || null,
    rol: localStorage.getItem("rol") || null,
  }),

  getters: {
    isAuthenticated: (state) => !!state.access,
  },

  actions: {
    async login(mail, password) {
      const res = await fetch(`${API_URL}/api/auth/login/`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ mail, password }),
      });
      const data = await parseResponseBody(res);

      if (!res.ok) {
        throw new Error(getErrorMessage(data, "Error al iniciar sesión"));
      }

      if (!data?.access || !data?.refresh || !data?.usuario) {
        throw new Error(
          "La respuesta del servidor al iniciar sesión no es válida",
        );
      }

      this.access = data.access;
      this.refresh = data.refresh;
      this.usuario = data.usuario;
      this.rol = data.rol;
      localStorage.setItem("access", data.access);
      localStorage.setItem("refresh", data.refresh);
      localStorage.setItem("usuario", data.usuario);
      localStorage.setItem("rol", data.rol);
    },

    async logout() {
      await fetch(`${API_URL}/api/auth/logout/`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${this.access}`,
        },
        body: JSON.stringify({ refresh: this.refresh }),
      });
      this.access = null;
      this.refresh = null;
      this.usuario = null;
      this.rol = null;
      localStorage.removeItem("access");
      localStorage.removeItem("refresh");
      localStorage.removeItem("usuario");
      localStorage.removeItem("rol");
    },

    async register(mail, usuario, password) {
      const res = await fetch(`${API_URL}/api/auth/register/`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ mail, usuario, password }),
      });
      const data = await parseResponseBody(res);

      if (!res.ok) {
        throw new Error(getErrorMessage(data, "Error al registrarse"));
      }

      if (!data?.access || !data?.refresh || !data?.usuario) {
        throw new Error(
          "La respuesta del servidor al registrarse no es válida",
        );
      }

      this.access = data.access;
      this.refresh = data.refresh;
      this.usuario = data.usuario;
      this.rol = data.rol;
      localStorage.setItem("access", data.access);
      localStorage.setItem("refresh", data.refresh);
      localStorage.setItem("usuario", data.usuario);
      localStorage.setItem("rol", data.rol);
    },
  },
});
