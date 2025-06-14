<template>
  <div class="login-page">
    <div class="login-container">
      <div class="login-header">
        <h2>Registro</h2>
        <p>Crea tu cuenta para agendar citas</p>
      </div>

      <form @submit.prevent="handleRegister" class="login-form">
        <div class="form-group">
          <input 
            type="text" 
            v-model="formData.nombre" 
            placeholder="Nombre"
            required
            class="form-input"
          >
        </div>

        <div class="form-group">
          <input 
            type="text" 
            v-model="formData.apellido" 
            placeholder="Apellido"
            required
            class="form-input"
          >
        </div>

        <div class="form-group">
          <input 
            type="email" 
            v-model="formData.email" 
            placeholder="Correo electrónico"
            required
            class="form-input"
          >
        </div>

        <div class="form-group">
          <input 
            type="password" 
            v-model="formData.password" 
            placeholder="Contraseña"
            required
            class="form-input"
          >
        </div>

        <div class="form-group">
          <input 
            type="password" 
            v-model="formData.confirmPassword" 
            placeholder="Confirmar contraseña"
            required
            class="form-input"
          >
        </div>

        <p v-if="error" class="error-message">{{ error }}</p>

        <button type="submit" class="login-button" :disabled="isLoading">
          {{ isLoading ? 'Registrando...' : 'Registrarse' }}
        </button>

        <p class="login-link">
          ¿Ya tienes cuenta? <router-link to="/login">Inicia sesión</router-link>
        </p>
      </form>
    </div>
  </div>
</template>

<script>
import { authService } from '../services/api'

export default {
  name: 'Register',
  data() {
    return {
      formData: {
        nombre: '',
        apellido: '',
        email: '',
        password: '',
        confirmPassword: ''
      },
      error: '',
      isLoading: false
    }
  },
  methods: {
    async handleRegister() {
      if (this.formData.password !== this.formData.confirmPassword) {
        this.error = 'Las contraseñas no coinciden';
        return;
      }

      this.isLoading = true;
      this.error = '';
      
      try {
        console.log('Enviando datos de registro:', this.formData);
        
        await authService.register({
          email: this.formData.email.trim(),
          username: this.formData.email.trim(),
          password: this.formData.password,
          nombre: this.formData.nombre.trim(),
          apellido: this.formData.apellido.trim()
        });

        // Mostrar mensaje de éxito y redirigir
        alert('Usuario registrado exitosamente. Ahora puedes iniciar sesión.');
        this.$router.push('/login');
        
      } catch (error) {
        console.error('Error en registro:', error);
        this.error = error.message || 'Error de conexión. Por favor, intenta más tarde.';
      } finally {
        this.isLoading = false;
      }
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

.login-button:disabled {
  opacity: 0.7;
  cursor: not-allowed;
}

.login-link {
  text-align: center;
  margin-top: 1rem;
  color: var(--color-text);
}

.login-link a {
  color: var(--color-primary);
  text-decoration: none;
  font-weight: var(--font-weight-medium);
}

.login-link a:hover {
  text-decoration: underline;
}
</style>
