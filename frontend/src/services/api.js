import axios from "axios";

// Función para obtener el token CSRF de las cookies
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

const API_BASE_URL =
  process.env.VUE_APP_API_URL || "https://backend-en-render.com/api";

const api = axios.create({
  baseURL: API_BASE_URL, // Usa ruta relativa para aprovechar el proxy
  withCredentials: true,
  headers: {
    "Content-Type": "application/json",
  },
});

// Interceptor para limpiar URLs
api.interceptors.request.use((config) => {
  // Eliminar slashes finales y caracteres especiales
  config.url = config.url.replace(/\/+$/, "").trim();
  // Agregar CSRF token si es POST, PUT, PATCH o DELETE
  if (["post", "put", "patch", "delete"].includes(config.method)) {
    const csrftoken = getCookie("csrftoken");
    if (csrftoken) {
      config.headers["X-CSRFToken"] = csrftoken;
    }
  }
  return config;
});

export const authService = {
  login: (credentials) => api.post("/auth/login", credentials),
  register: (userData) => api.post("/auth/register", userData),
  logout: () => api.post("/auth/logout"),
};

export const appointmentService = {
  getMine: () => api.get("/appointments/my"),
  create: (appointment) => api.post("/appointments", appointment),
  update: (id, appointment) => api.put(`/appointments/${id}`, appointment),
  delete: (id) => api.delete(`/appointments/${id}`),
};
