<template>
  <div class="compra-exitosa">
    <div class="container">
      <div class="success-card">
        <div class="icon">✓</div>
        <h1>¡Compra Exitosa!</h1>
        <p>Tu pago ha sido procesado correctamente.</p>

        <div class="detalles">
          <p><strong>ID de sesión:</strong> {{ sessionId }}</p>
          <p>En breve recibirás un email de confirmación.</p>
        </div>

        <div class="actions">
          <router-link to="/" class="btn btn-primary"
            >Volver al inicio</router-link
          >
          <router-link to="/merchandising" class="btn btn-secondary"
            >Seguir comprando</router-link
          >
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from "vue";
import { useRoute } from "vue-router";

const route = useRoute();
const sessionId = ref("");

onMounted(() => {
  sessionId.value = (route.query.session_id as string) || "N/A";
});
</script>

<style scoped>
.compra-exitosa {
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}

.container {
  width: 100%;
  max-width: 500px;
  padding: 20px;
}

.success-card {
  background: white;
  border-radius: 12px;
  padding: 40px 30px;
  text-align: center;
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.1);
}

.icon {
  font-size: 60px;
  color: #4caf50;
  margin-bottom: 20px;
  display: inline-block;
  background: #e8f5e9;
  width: 80px;
  height: 80px;
  border-radius: 50%;
  line-height: 80px;
}

h1 {
  color: #333;
  margin-bottom: 10px;
  font-size: 28px;
}

.compra-exitosa > .container > .success-card > p {
  color: #666;
  font-size: 16px;
  margin-bottom: 30px;
}

.detalles {
  background: #f5f5f5;
  padding: 20px;
  border-radius: 8px;
  margin: 20px 0;
  text-align: left;
}

.detalles p {
  margin: 10px 0;
  font-size: 14px;
  color: #555;
}

.detalles strong {
  color: #333;
}

.actions {
  display: flex;
  gap: 10px;
  margin-top: 30px;
  flex-direction: column;
}

.btn {
  padding: 12px 20px;
  border-radius: 8px;
  text-decoration: none;
  font-weight: 500;
  transition: all 0.3s ease;
  display: inline-block;
}

.btn-primary {
  background-color: #667eea;
  color: white;
}

.btn-primary:hover {
  background-color: #5568d3;
}

.btn-secondary {
  background-color: #e0e0e0;
  color: #333;
}

.btn-secondary:hover {
  background-color: #d0d0d0;
}

@media (max-width: 600px) {
  .success-card {
    padding: 30px 20px;
  }

  h1 {
    font-size: 24px;
  }

  .actions {
    flex-direction: column;
  }
}
</style>
