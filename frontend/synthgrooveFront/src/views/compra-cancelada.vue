<template>
  <div class="compra-cancelada">
    <div class="container">
      <div class="error-card">
        <div class="icon">✕</div>
        <h1>Compra Cancelada</h1>
        <p>Tu pago ha sido cancelado o hubo un problema.</p>

        <div class="mensaje">
          <p>
            Si crees que es un error, intenta de nuevo o contacta con soporte.
          </p>
        </div>

        <div class="actions">
          <router-link to="/" class="btn btn-primary"
            >Volver al inicio</router-link
          >
          <router-link to="/merchandising" class="btn btn-secondary"
            >Intentar de nuevo</router-link
          >
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts"></script>

<style scoped>
.compra-cancelada {
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
}

.container {
  width: 100%;
  max-width: 500px;
  padding: 20px;
}

.error-card {
  background: white;
  border-radius: 12px;
  padding: 40px 30px;
  text-align: center;
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.1);
}

.icon {
  font-size: 60px;
  color: #f5576c;
  margin-bottom: 20px;
  display: inline-block;
  background: #ffebee;
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

.compra-cancelada > .container > .error-card > p {
  color: #666;
  font-size: 16px;
  margin-bottom: 20px;
}

.mensaje {
  background: #fff3e0;
  padding: 20px;
  border-radius: 8px;
  margin: 20px 0;
  border-left: 4px solid #ff9800;
}

.mensaje p {
  color: #e65100;
  font-size: 14px;
  margin: 0;
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
  .error-card {
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
