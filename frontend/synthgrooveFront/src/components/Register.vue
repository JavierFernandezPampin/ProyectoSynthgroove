<script setup lang="ts">
import { ref } from "vue";
import { useAuthStore } from "@/stores/auth";
import { useRouter } from "vue-router";

const auth = useAuthStore();
const router = useRouter();

const usuario = ref("");
const mail = ref("");
const password = ref("");
const confirmPassword = ref("");
const error = ref("");

async function handleRegister() {
  error.value = "";

  if (password.value.length <= 6) {
    error.value = "La contraseña debe tener más de 6 caracteres";
    return;
  }

  if (password.value !== confirmPassword.value) {
    error.value = "Las contraseñas no coinciden";
    return;
  }

  try {
    await auth.register(mail.value, usuario.value, password.value);
    router.push("/");
  } catch (e: any) {
    error.value = e.message;
  }
}
</script>

<template>
  <div class="register-wrapper">
    <form class="register-form" @submit.prevent="handleRegister">
      <h2>Regístrate</h2>

      <div class="form-group">
        <label for="usuario">Usuario</label>
        <input
          id="usuario"
          v-model="usuario"
          type="text"
          placeholder="Tu nombre de usuario"
          required
        />
      </div>

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

      <div class="form-group">
        <label for="confirm-password">Repite la contraseña</label>
        <input
          id="confirm-password"
          v-model="confirmPassword"
          type="password"
          placeholder="••••••••"
          required
        />
      </div>

      <p v-if="error" class="error">{{ error }}</p>

      <button type="submit">Crear cuenta</button>

      <p class="auth-link-row">
        Ya tienes cuenta?
        <router-link class="auth-link" to="/login">Inicia sesión</router-link>
      </p>
    </form>
  </div>
</template>

<style scoped>
.register-wrapper {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 70vh;
  width: 100%;
  padding: 2rem 1rem 3rem;
  background: #000;
  font-family: "Space Grotesk", "Avenir Next", "Trebuchet MS", sans-serif;
}

.register-form {
  display: flex;
  flex-direction: column;
  gap: 1.2rem;
  width: min(100%, 420px);
  padding: 2rem;
  background: #1a1a1a;
  border: 1px solid #333;
  border-radius: 0;
}
.register-form h2 {
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

@media (max-width: 480px) {
  .register-wrapper {
    padding-inline: 0.85rem;
  }

  .register-form {
    padding: 1.4rem;
  }

  .auth-link-row {
    line-height: 1.6;
  }
}
</style>
