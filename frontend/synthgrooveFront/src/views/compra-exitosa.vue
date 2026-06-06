<template>
  <div class="compra-wrapper">
    <div class="compra-card">
      <div class="icono icono-ok">✓</div>
      <h1>Compra exitosa</h1>
      <p>Tu pago ha sido procesado correctamente. En breve recibirás un email de confirmación.</p>
      <div class="actions">
        <router-link to="/perfil" class="btn-primary">Ver mis pedidos</router-link>
        <router-link to="/merchandising" class="btn-secondary">Seguir comprando</router-link>
      </div>
    </div>
  </div>
</template>

<style scoped>
.compra-wrapper {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  min-height: 60vh;
  padding: 2rem 1rem 3rem;
  background: #000;
  font-family: "Space Grotesk", "Avenir Next", "Trebuchet MS", sans-serif;
}

.compra-card {
  width: min(100%, 480px);
  background: #1a1a1a;
  border: 1px solid #333;
  border-radius: 12px;
  padding: 2.5rem 2rem;
  text-align: center;
  display: flex;
  flex-direction: column;
  gap: 1.25rem;
}

.icono {
  width: 64px;
  height: 64px;
  border-radius: 0;
  font-size: 1.75rem;
  line-height: 64px;
  margin: 0 auto;
}

.icono-ok {
  background: rgba(74, 222, 128, 0.1);
  border: 1px solid #4ade80;
  color: #4ade80;
}

h1 {
  color: #f7f1e8;
  font-size: 1.5rem;
  margin: 0;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

p {
  color: #888;
  font-size: 0.9rem;
  line-height: 1.6;
  margin: 0;
}

.actions {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
  margin-top: 0.5rem;
}

.btn-primary,
.btn-secondary {
  display: block;
  padding: 0.75rem 1.5rem;
  border-radius: 4px;
  font-size: 0.85rem;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  text-decoration: none;
  transition: background 0.2s;
  font-family: inherit;
}

.btn-primary {
  background: #f7f1e8;
  color: #111;
  border: 1px solid #f7f1e8;
}

.btn-primary:hover {
  background: #e1d7c6;
}

.btn-secondary {
  background: transparent;
  color: #f7f1e8;
  border: 1px solid #333;
}

.btn-secondary:hover {
  border-color: #f7f1e8;
}
</style>
