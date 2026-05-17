const API_URL = import.meta.env.VITE_API_URL || "";

export async function getArtistas() {
  const res = await fetch(`${API_URL}/api/artistas/`);
  return res.json();
}
