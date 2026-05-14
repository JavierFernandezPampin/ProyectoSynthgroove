<script setup lang="ts">
import { ref } from "vue";
import { useAuthStore } from "@/stores/auth";
import { useRouter } from "vue-router";

const auth = useAuthStore();
const router = useRouter();

const mail = ref("");
const password = ref("");
const error = ref("");
const loading = ref(false);
const ERROR_MESSAGES: Record<string, string> = {
  "No active account found with the given credentials":
    "Email o contraseña incorrectos.",
};

async function handleLogin() {
  error.value = "";
  loading.value = true;
  try {
    await auth.login(mail.value, password.value);
    router.push("/");
  } catch (e: any) {
    error.value =
      ERROR_MESSAGES[e.message] ??
      "Error al iniciar sesión. Inténtalo de nuevo.";
  } finally {
    loading.value = false;
  }
}
</script>

<template>
  <div class="login-wrapper">
    <form class="login-form" @submit.prevent="handleLogin">
      <h2>Iniciar sesión</h2>

      <div class="form-group">
        <label for="mail">Email</label>
        <input
          id="mail"
          v-model="mail"
          type="email"
          placeholder="tu@email.com"
          required
        />
      </div>

      <div class="form-group">
        <label for="password">Contraseña</label>
        <input
          id="password"
          v-model="password"
          type="password"
          placeholder="••••••••"
          required
        />
      </div>

      <p v-if="error" class="error">{{ error }}</p>

      <button type="submit" :disabled="loading">
        {{ loading ? "Entrando..." : "Entrar" }}
      </button>

      <p class="auth-link-row">
        No estás registrado?
        <router-link class="auth-link" to="/registro">Regístrate</router-link>
      </p>
    </form>
  </div>
</template>

<style scoped>
.login-wrapper {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background: #121212;
  font-family: "Space Grotesk", "Avenir Next", "Trebuchet MS", sans-serif;
}
.login-form {
  display: flex;
  flex-direction: column;
  gap: 1.2rem;
  width: min(100%, 380px);
  padding: 2rem;
  background: #1a1a1a;
  border: 1px solid #333;
}
.login-form h2 {
  color: #f7f1e8;
  margin: 0;
  font-size: 1.4rem;
}
.form-group {
  display: flex;
  flex-direction: column;
  gap: 0.4rem;
}
label {
  color: #f7f1e8;
  font-size: 0.85rem;
}
input {
  background: #111;
  border: 1px solid #444;
  color: #f7f1e8;
  padding: 0.6rem 0.8rem;
  font-size: 0.95rem;
}
input:focus {
  outline: none;
  border-color: #f7f1e8;
}
button {
  background: transparent;
  border: 1px solid #f7f1e8;
  color: #f7f1e8;
  padding: 0.7rem;
  cursor: pointer;
  font-size: 0.95rem;
  transition: background 0.2s;
}
button:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}
button:hover {
  background: rgba(247, 241, 232, 0.1);
}
.error {
  color: #e05252;
  font-size: 0.85rem;
  margin: 0;
}
.auth-link-row {
  margin: 0;
  color: #f7f1e8;
  font-size: 0.9rem;
  text-align: center;
}
.auth-link {
  color: #f7f1e8;
  text-decoration: underline;
  text-underline-offset: 0.2rem;
}
.auth-link:hover {
  color: rgba(247, 241, 232, 0.8);
}
</style>
