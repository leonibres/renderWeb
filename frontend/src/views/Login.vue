<template>
  <div class="login-page">
    <div class="login-container">
      <div class="login-header">
        <h2>Iniciar Sesión</h2>
        <p>Ingresa tus credenciales para continuar</p>
      </div>

      <form @submit.prevent="handleLogin" class="login-form">
        <div class="form-group">
          <input 
            type="text" 
            v-model="username" 
            placeholder="Usuario" 
            required
            class="form-input"
          >
        </div>

        <div class="form-group">
          <input 
            type="password" 
            v-model="password" 
            placeholder="Contraseña" 
            required
            class="form-input"
          >
        </div>

        <p v-if="error" class="error-message">{{ error }}</p>

        <button type="submit" class="login-button">
          Ingresar
        </button>

        <p class="login-link">
          ¿No tienes cuenta? <router-link to="/register">Regístrate aquí</router-link>
        </p>
      </form>
    </div>
  </div>
</template>

<script>
import { useAuth } from '@/composables/useAuth'

export default {
  name: 'Login',
  data() {
    return {
      username: '',
      password: '',
      error: '',
      isLoading: false
    }
  },
  setup() {
    const { login } = useAuth()
    return { login }
  },
  methods: {
    async handleLogin() {
      this.isLoading = true;
      this.error = '';
      try {
        await this.login({
          email: this.username.trim(),
          password: this.password
        });
        const intendedPath = sessionStorage.getItem('intendedPath') || '/citas';
        sessionStorage.removeItem('intendedPath');
        this.$router.push(intendedPath);
      } catch (error) {
        this.error = error.message || 'Error de conexión. Por favor, intenta más tarde.';
      } finally {
        this.isLoading = false;
      }
    },
    getCookie(name) {
      const value = `; ${document.cookie}`;
      const parts = value.split(`; ${name}=`);
      if (parts.length === 2) return parts.pop().split(';').shift();
    }
  }
}
</script>

<style scoped>
.login-page {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: var(--color-background);
  padding: 1rem;
}

.login-container {
  background: var(--color-gray);
  border-radius: 12px;
  padding: 2rem;
  width: 100%;
  max-width: 400px;
  box-shadow: 0 4px 24px rgba(0, 0, 0, 0.1);
}

.login-header {
  text-align: center;
  margin-bottom: 2rem;
}

.login-header h2 {
  color: var(--color-primary);
  margin-bottom: 0.5rem;
}

.login-header p {
  color: var(--color-text);
  margin-bottom: 0;
}

.login-form {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.form-group {
  position: relative;
}

.form-input {
  width: 100%;
  padding: 0.8rem 1rem;
  background: var(--color-background);
  border: 1px solid var(--color-border);
  border-radius: 8px;
  color: var(--color-white);
  transition: border-color 0.2s;
}

.form-input:focus {
  border-color: var(--color-primary);
}

.error-message {
  color: #ff4d4d;
  font-size: 0.9rem;
  margin: -0.5rem 0 0.5rem;
  text-align: center;
}

.login-button {
  background: var(--color-primary);
  color: var(--color-dark);
  padding: 0.8rem;
  border-radius: 8px;
  font-weight: var(--font-weight-semibold);
  cursor: pointer;
  transition: all 0.2s;
}

.login-button:hover {
  background: transparent;
  color: var(--color-primary);
  border: 2px solid var(--color-primary);
}

.login-link {
  text-align: center;
  margin-top: 1rem;
  color: var(--color-text);
}
</style>


