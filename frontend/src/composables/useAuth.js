import { ref, computed } from "vue";
import axiosInstance from "../axiosConfig";

const user = ref(null);
const loading = ref(false);

export function useAuth() {
  const isAuthenticated = computed(() => !!user.value);
  const userData = user; // Alias para compatibilidad con Header

  const checkAuth = () => {
    const userDataLocal = localStorage.getItem("userData");
    if (userDataLocal) {
      user.value = JSON.parse(userDataLocal);
      return true;
    }
    user.value = null;
    return false;
  };

  const logout = () => {
    localStorage.removeItem("token");
    localStorage.removeItem("userData");
    user.value = null;
  };

  const login = async (credentials) => {
    loading.value = true;
    try {
      const response = await axiosInstance.post("/api/auth/login", credentials);
      const { user: userObj } = response.data;
      localStorage.setItem("userData", JSON.stringify(userObj));
      user.value = userObj;
      return true;
    } catch (error) {
      console.error("Error en login:", error);
      throw error;
    } finally {
      loading.value = false;
    }
  };

  const register = async (userData) => {
    loading.value = true;
    try {
      const response = await axiosInstance.post("/api/auth/register", userData);
      return response.data;
    } catch (error) {
      console.error("Error en registro:", error);
      throw error;
    } finally {
      loading.value = false;
    }
  };

  // Inicializar estado de autenticación
  checkAuth();

  return {
    userData,
    loading,
    isAuthenticated,
    checkAuth,
    login,
    register,
    logout,
  };
}
