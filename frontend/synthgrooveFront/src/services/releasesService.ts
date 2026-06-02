const API_URL = import.meta.env.VITE_API_URL || "";

export async function getReleases() {
  const response = await fetch(`${API_URL}/api/releases/`);
  if (!response.ok) throw new Error("Error al cargar releases");
  return response.json();
}
