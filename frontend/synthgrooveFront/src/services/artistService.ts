const API = import.meta.env.VITE_API_URL;
const BASE_URL = import.meta.env.VITE_API_URL || "";

export async function getArtistas() {
  const res = await fetch(`${API}/api/artistas/`);
  return res.json();
}
