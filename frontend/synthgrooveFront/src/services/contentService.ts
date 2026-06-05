const API_URL = import.meta.env.VITE_API_URL || "";

export interface GestionProducto {
  id: number;
  nombre: string;
  precio: number;
  categoria: string;
  imagen: string | null;
  usuario: number | null;
}

export interface GestionEvento {
  id: number;
  nombre: string;
  localizacion: string;
  fecha_release: string | null;
  imagen: string | null;
  precio: number;
  usuario: number | null;
}

export const getProductos = async (token: string): Promise<GestionProducto[]> => {
  const response = await fetch(`${API_URL}/api/productos/`, {
    headers: { Authorization: `Bearer ${token}` },
  });
  if (!response.ok) throw new Error("Error al cargar los productos");
  return response.json();
};

export const createProducto = async (
  token: string,
  data: FormData
): Promise<GestionProducto> => {
  const response = await fetch(`${API_URL}/api/productos/`, {
    method: "POST",
    headers: { Authorization: `Bearer ${token}` },
    body: data,
  });
  if (!response.ok) throw new Error("Error al crear el producto");
  return response.json();
};

export const updateProducto = async (
  token: string,
  id: number,
  data: FormData
): Promise<GestionProducto> => {
  const response = await fetch(`${API_URL}/api/productos/${id}/`, {
    method: "PATCH",
    headers: { Authorization: `Bearer ${token}` },
    body: data,
  });
  if (!response.ok) throw new Error("Error al actualizar el producto");
  return response.json();
};

export const deleteProducto = async (token: string, id: number): Promise<void> => {
  const response = await fetch(`${API_URL}/api/productos/${id}/`, {
    method: "DELETE",
    headers: { Authorization: `Bearer ${token}` },
  });
  if (!response.ok) throw new Error("Error al eliminar el producto");
};

export const getEventos = async (token: string): Promise<GestionEvento[]> => {
  const response = await fetch(`${API_URL}/api/eventos/`, {
    headers: { Authorization: `Bearer ${token}` },
  });
  if (!response.ok) throw new Error("Error al cargar los eventos");
  return response.json();
};

export const createEvento = async (
  token: string,
  data: FormData
): Promise<GestionEvento> => {
  const response = await fetch(`${API_URL}/api/eventos/`, {
    method: "POST",
    headers: { Authorization: `Bearer ${token}` },
    body: data,
  });
  if (!response.ok) throw new Error("Error al crear el evento");
  return response.json();
};

export const updateEvento = async (
  token: string,
  id: number,
  data: FormData
): Promise<GestionEvento> => {
  const response = await fetch(`${API_URL}/api/eventos/${id}/`, {
    method: "PATCH",
    headers: { Authorization: `Bearer ${token}` },
    body: data,
  });
  if (!response.ok) throw new Error("Error al actualizar el evento");
  return response.json();
};

export const deleteEvento = async (token: string, id: number): Promise<void> => {
  const response = await fetch(`${API_URL}/api/eventos/${id}/`, {
    method: "DELETE",
    headers: { Authorization: `Bearer ${token}` },
  });
  if (!response.ok) throw new Error("Error al eliminar el evento");
};
