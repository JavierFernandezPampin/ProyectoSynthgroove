const BASE_URL = import.meta.env.VITE_API_URL || "";
const API_URL = `${BASE_URL}/api/productos/`;

export async function getProductos() {
  const response = await fetch(API_URL);
  if (!response.ok) throw new Error("Error al cargar productos");
  return response.json();
}
