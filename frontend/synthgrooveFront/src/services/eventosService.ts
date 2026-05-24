const API_URL = import.meta.env.VITE_API_URL || "";

export const getEventos = async () => {
  const response = await fetch(`${API_URL}/api/eventos/`);
  if (!response.ok) throw new Error("Error al cargar eventos");
  return response.json();
};
