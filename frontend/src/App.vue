<script setup>
// Importa el header y el footer globales de la aplicación
import Header from './layouts/Header.vue';
import Footer from './layouts/footer.vue';
</script>

<template>
  <!-- Componente de cabecera global -->
  <Header/>
  <main>
    <!-- Renderiza la vista de la ruta actual -->
    <router-view />
  </main>
  <!-- Componente de pie de página global -->
  <Footer />
</template>



