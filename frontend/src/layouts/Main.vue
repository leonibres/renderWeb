<script setup>
// Main.vue - Layout principal de la página de inicio

// Importa estilos globales
import '../assets/styles/global.css'

// Importa las secciones principales de la landing page
import HeroSection from "../sections/HeroSection.vue"      // Sección principal/hero
import ContactoSection from "../sections/ContactoSection.vue" // Sección de contacto
import FaqSection from "../sections/FaqSection.vue"        // Sección de preguntas frecuentes
import EstiloperfectSection from "../sections/EstiloperfectSection.vue" // Sección de marcas asociadas
import NosotrosSection from "../sections/NosotrosSection.vue" // Sección de nosotros
import ServicioSection from "../sections/servicioSection.vue" // Usa el nombre exacto del archivo
import EnfoqueSection from "../sections/EnfoqueSection.vue"   // Sección de enfoque
import TestimonioSection from "../sections/TestimonioSection.vue" // Sección de testimonios
</script>

<template>
  <!-- Renderiza las secciones principales en orden -->
  <HeroSection />
  <ServicioSection />
  <EstiloperfectSection />
  <EnfoqueSection />
  <NosotrosSection />
  <ContactoSection />
  <FaqSection />
  <TestimonioSection />
</template>