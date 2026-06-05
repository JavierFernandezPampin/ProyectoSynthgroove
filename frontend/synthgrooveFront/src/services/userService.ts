const API_URL = import.meta.env.VITE_API_URL || "";

export interface UserProfile {
  id: number;
  usuario: string;
  nombre: string | null;
  apellido: string | null;
  mail: string;
  rol: string;
}

export const getUserProfile = async (token: string): Promise<UserProfile> => {
  const response = await fetch(`${API_URL}/api/auth/me/`, {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });
  if (!response.ok) throw new Error("Error al cargar el perfil del usuario");
  return response.json();
};

export interface Pedido {
  id: number;
  producto: number;
  producto_nombre: string;
  producto_imagen: string | null;
  cantidad: number;
  precio_unitario: number;
  fecha: string;
}

export const getPedidos = async (token: string): Promise<Pedido[]> => {
  const response = await fetch(`${API_URL}/api/pedidos/`, {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });
  if (!response.ok) throw new Error("Error al cargar los pedidos");
  return response.json();
};

export const getUsuarios = async (token: string): Promise<UserProfile[]> => {
  const response = await fetch(`${API_URL}/api/admin/usuarios/`, {
    headers: { Authorization: `Bearer ${token}` },
  });
  if (!response.ok) throw new Error("Error al cargar los usuarios");
  return response.json();
};

export const changeUserRole = async (
  token: string,
  id: number,
  rol: "suscriptor" | "gestor"
): Promise<UserProfile> => {
  const response = await fetch(`${API_URL}/api/admin/usuarios/${id}/`, {
    method: "PATCH",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${token}`,
    },
    body: JSON.stringify({ rol }),
  });
  if (!response.ok) throw new Error("Error al cambiar el rol");
  return response.json();
};

export const deleteUsuario = async (token: string, id: number): Promise<void> => {
  const response = await fetch(`${API_URL}/api/admin/usuarios/${id}/`, {
    method: "DELETE",
    headers: { Authorization: `Bearer ${token}` },
  });
  if (!response.ok) throw new Error("Error al eliminar el usuario");
};

export const changePassword = async (
  token: string,
  oldPassword: string,
  newPassword: string
): Promise<{ message: string }> => {
  const response = await fetch(`${API_URL}/api/auth/change-password/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${token}`,
    },
    body: JSON.stringify({
      old_password: oldPassword,
      new_password: newPassword,
    }),
  });
  if (!response.ok) throw new Error("Error al cambiar la contraseña");
  return response.json();
};
