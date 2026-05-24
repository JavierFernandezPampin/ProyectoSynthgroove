<template>
  <div class="pago-stripe">
    <h2>Comprar</h2>

    <div class="form-group">
      <label>Tipo:</label>
      <select v-model="tipo">
        <option value="producto">Producto</option>
        <option value="evento">Evento</option>
      </select>
    </div>

    <div class="form-group">
      <label>ID:</label>
      <input
        v-model.number="id"
        type="number"
        placeholder="ID del producto o evento"
      />
    </div>

    <div class="form-group">
      <label>Cantidad:</label>
      <input v-model.number="cantidad" type="number" min="1" />
    </div>

    <button @click="pagar" :disabled="cargando">
      {{ cargando ? "Procesando..." : "Ir a Pagar" }}
    </button>

    <div v-if="error" class="error">{{ error }}</div>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";
import { iniciarPago } from "../services/pagoService";

const tipo = ref<"producto" | "evento">("producto");
const id = ref<number>(0);
const cantidad = ref<number>(1);
const cargando = ref(false);
const error = ref("");

async function pagar() {
  if (!id.value) {
    error.value = "Por favor ingresa un ID";
    return;
  }

  cargando.value = true;
  error.value = "";

  try {
    await iniciarPago(tipo.value, id.value, cantidad.value);
  } catch (err: any) {
    error.value = err.message || "Error al procesar el pago";
  } finally {
    cargando.value = false;
  }
}
</script>

<style scoped>
.pago-stripe {
  max-width: 400px;
  margin: 20px auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 8px;
}

.form-group {
  margin-bottom: 15px;
}

label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
}

input,
select {
  width: 100%;
  padding: 8px;
  border: 1px solid #ddd;
  border-radius: 4px;
  box-sizing: border-box;
}

button {
  width: 100%;
  padding: 10px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 16px;
}

button:disabled {
  background-color: #ccc;
  cursor: not-allowed;
}

button:hover:not(:disabled) {
  background-color: #0056b3;
}

.error {
  color: red;
  margin-top: 10px;
}
</style>
