const API_URL = "/api";

export const authService = {
  async login(username, password) {
    const response = await fetch(`${API_URL}/auth/login`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json",
      },
      credentials: "include",
      body: JSON.stringify({
        email: username.trim(),
        password,
      }),
    });

    if (!response.ok) {
      throw new Error("Error de autenticación");
    }

    return response.json();
  },

  async logout() {
    localStorage.removeItem("token");
    await fetch(`${API_URL}/auth/logout/`, {
      method: "POST",
      credentials: "include",
    });
  },

  isAuthenticated() {
    return !!localStorage.getItem("token");
  },
};
