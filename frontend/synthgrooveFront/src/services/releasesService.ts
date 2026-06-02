const API_URL = import.meta.env.VITE_API_URL || "";

export async function getReleases() {
  const res = await fetch(`${API_URL}/api/releases/`);
  if (!res.ok) throw new Error("Error al cargar releases");
  return res.json();
}
