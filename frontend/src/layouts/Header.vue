<template>
  <!-- Barra de navegación principal -->
  <nav class="navbar navbar-expand-lg fixed-top">
    <div class="container">
      <!-- Logo y enlace a la página principal -->
      <router-link class="navbar-brand" to="/">
        <span class="fw-bold">Beard & Style</span>
      </router-link>

      <!-- Botón para mostrar/ocultar el menú en pantallas pequeñas -->
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarContent"
        aria-controls="navbarContent" aria-expanded="false" aria-label="Toggle navigation" @click="toggleNavbar">
        <span class="navbar-toggler-icon"></span>
      </button>

      <!-- Contenido del menú de navegación -->
      <div class="collapse navbar-collapse" id="navbarContent" :class="{ show: isNavbarOpen }">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <!-- Enlace a Inicio -->
          <li class="nav-item">
            <router-link class="nav-link" to="/" @click="scrollToTop">Inicio</router-link>
          </li>
          <!-- Enlace a Servicios (scroll a sección) -->
          <li class="nav-item">
            <router-link class="nav-link" to="/#services" @click="scrollToSection('services')">
              Servicios
            </router-link>
          </li>
          <!-- Enlace a Citas (requiere autenticación) -->
          <li class="nav-item">
            <a class="nav-link" href="#" @click.prevent="handleCitasClick">Citas</a>
          </li>
          <!-- Enlace a Nosotros (scroll a sección) -->
          <li class="nav-item">
            <router-link class="nav-link" to="/#details" @click="scrollToSection('details')">
              Nosotros
            </router-link>
          </li>
          <!-- Enlace a Contacto (scroll a sección) -->
          <li class="nav-item">
            <router-link class="nav-link" to="/#contact" @click="scrollToSection('contact')">
              Contacto
            </router-link>
          </li>          
        </ul>

        <!-- Botón de acceso o menú de usuario según autenticación -->
        <div v-if="!isAuthenticated">
          <!-- Botón para iniciar sesión -->
          <router-link to="/login" class="btn-hero-solid" style="padding: 0.5rem 1.2rem; font-size: 0.98rem;">
            <i class="fas fa-sign-in-alt me-2"></i>Acceder
          </router-link>
        </div>
        <div v-else class="dropdown">
          <!-- Menú desplegable de usuario autenticado -->
          <button 
            class="btn-hero-solid dropdown-toggle"
            style="padding: 0.5rem 1.2rem; font-size: 0.98rem;"
            type="button"
            id="userMenuButton"
            data-bs-toggle="dropdown"
            aria-expanded="false"
          >
            <i class="fas fa-user me-2"></i>{{ userData?.nombre || userData?.username || 'Usuario' }}
          </button>
          <ul class="dropdown-menu dropdown-menu-end" aria-labelledby="userMenuButton">             
            <li><hr class="dropdown-divider"></li>
            <li><a class="dropdown-item" href="#" @click.prevent="handleLogout">Cerrar Sesión</a></li>
          </ul>
        </div>
      </div>
    </div>
  </nav>
</template>

<script>
import { useAuth } from '@/composables/useAuth';

export default {
  name: 'NavBar',
  setup() {
    // Composable para autenticación
    const { isAuthenticated, userData, logout } = useAuth();
    return { isAuthenticated, userData, logout };
  },
  data() {
    return {
      isNavbarOpen: false,    // Estado del menú en móviles
      isDropdownOpen: false,  // Estado del dropdown "Más"
      showAuthModal: false,   // Estado del modal de autenticación (no usado aquí)
      authActiveTab: 'login'  // Pestaña activa en el modal de autenticación (no usado aquí)
    };
  },
  methods: {
    // Alterna el menú de navegación en móviles
    toggleNavbar() {
      this.isNavbarOpen = !this.isNavbarOpen;
    },
    // Alterna el menú desplegable "Más"
    toggleDropdown() {
      this.isDropdownOpen = !this.isDropdownOpen;
    },
    // Hace scroll al inicio de la página
    scrollToTop() {
      window.scrollTo({
        top: 0,
        behavior: 'smooth'
      });
    },
    // Hace scroll suave a una sección específica
    scrollToSection(sectionId) {
      const element = document.getElementById(sectionId);
      if (element) {
        element.scrollIntoView({ behavior: 'smooth' });
      }
    },
    // Maneja el click en "Citas", redirige según autenticación
    async handleCitasClick() {
      this.isNavbarOpen = false;
      if (this.isAuthenticated) {
        await this.$router.push('/citas');
      } else {
        sessionStorage.setItem('intendedPath', '/citas');
        await this.$router.push('/login');
      }
    },
    // Maneja el click en "Mi Perfil", redirige según autenticación
    async handlePerfilClick() {
      if (this.isAuthenticated) {
        await this.$router.push('/perfil');
      } else {
        sessionStorage.setItem('intendedPath', '/perfil');
        await this.$router.push('/login');
      }
    },
    // Maneja el click en "Mis Citas", redirige según autenticación
    async handleMisCitasClick() {
      if (this.isAuthenticated) {
        await this.$router.push('/mis-citas');
      } else {
        sessionStorage.setItem('intendedPath', '/mis-citas');
        await this.$router.push('/login');
      }
    },
    // Cierra sesión y redirige a inicio
    async handleLogout() {
      await this.logout();
      this.$router.push('/');
    }
  }
};
</script>