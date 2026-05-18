const API_URL = import.meta.env.VITE_API_URL || "";

export async function getArtistas() {
  const res = await fetch(`${API_URL}/api/artistas/`);
  if (!res.ok) throw new Error("Error al cargar artistas");
  return res.json();
}
