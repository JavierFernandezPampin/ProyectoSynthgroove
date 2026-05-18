const API_URL = import.meta.env.VITE_API_URL || "";

export async function getProductos() {
  const response = await fetch(`${API_URL}/api/productos/`);
  if (!response.ok) throw new Error("Error al cargar productos");
  const data = await response.json();

  return data.map((p: any) => ({
    ...p,
    imagen: p.imagen ? p.imagen.replace(/^https?:\/\/[^/]+/, API_URL) : "",
  }));
}
