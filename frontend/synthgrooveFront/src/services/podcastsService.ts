const API_URL = import.meta.env.VITE_API_URL || "";

export async function getPodcasts() {
  const response = await fetch(`${API_URL}/api/podcasts/`);
  if (!response.ok) throw new Error("Error al cargar podcasts");
  return response.json();
}
