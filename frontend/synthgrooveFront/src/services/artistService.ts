const API_URL = import.meta.env.VITE_API_URL || "";

export async function getArtistas() {
  const res = await fetch(`${API_URL}/api/artistas/`);
  if (!res.ok) throw new Error("Error al cargar artistas");
  const data = await res.json();

  return data.map((a: any) => ({
    ...a,
    imagen: a.imagen ? a.imagen.replace(/^https?:\/\/[^/]+/, API_URL) : "",
  }));
}
