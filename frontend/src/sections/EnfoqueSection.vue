<template>
  <!-- Sección principal que describe el enfoque del negocio -->
  <section id="details" class="enfoque-section">
    <div class="container">
      <div class="row" style="margin-top: 2.5rem;">
        <!-- Columna de imagen representativa -->
        <div class="col-lg-6 col-xl-7">
          <div class="image-container">
            <!-- Imagen ilustrativa de los servicios -->
            <img class="img-fluid" src="assets/images/details-1.png" alt="Servicios destacados" />
          </div>
        </div>
        <!-- Columna de texto descriptivo -->
        <div class="col-lg-6 col-xl-5">
          <div class="text-container">
            <!-- Título de la sección -->
            <div class="section-title">Nuestro Enfoque</div>
            <!-- Encabezado principal -->
            <h2>Transformamos tu estilo, potenciamos tu confianza</h2>
            <!-- Descripción del enfoque y valores -->
            <p>
              En <strong>Beard & Style</strong>, creemos que un buen estilo
              puede cambiarlo todo. Nuestro equipo combina experiencia y pasión
              para ofrecerte un servicio personalizado que resalte lo mejor de
              ti.
            </p>
            <p>
              Desde cortes modernos hasta el cuidado de tu barba, estamos aquí
              para ayudarte a lucir y sentirte increíble.
            </p>
            <!-- Botón de contacto -->
            <a class="btn-hero-solid" href="#contact">
              <i class="fas fa-envelope me-2"></i>Contáctanos
            </a>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
// Componente que representa la sección de enfoque de la página principal
export default {
  name: "EnfoqueSection"
};
</script>


