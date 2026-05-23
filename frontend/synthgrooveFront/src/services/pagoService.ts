const API_BASE = import.meta.env.VITE_API_URL ?? "";

export async function iniciarPago(
  tipo: "producto" | "evento",
  id: number,
  cantidad = 1,
): Promise<void> {
  const token = localStorage.getItem("token");

  const response = await fetch(`${API_BASE}/api/pago-stripe/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      ...(token ? { Authorization: `Bearer ${token}` } : {}),
    },
    body: JSON.stringify({ tipo, id, cantidad }),
  });

  const data = await response.json();

  if (!response.ok) {
    throw new Error(data.error ?? "Error al procesar el pago");
  }

  window.location.href = data.checkout_url;
}
