const API_URL = import.meta.env.VITE_API_URL || "";

export const getEventos = async () => {
  console.log("API_URL:", API_URL); // ← dentro de la función
  const response = await fetch(`${API_URL}/api/eventos/`);
  if (!response.ok) throw new Error("Error al cargar eventos");
  const data = await response.json();

  console.log("imagen raw:", data[0]?.imagen);
  return data.map((e: any) => ({
    ...e,
    imagen: e.imagen
      ? `https://proyecto-fct-synthgroove.onrender.com/media/${e.imagen.split("/media/")[1]}`
      : "",
  }));
};
