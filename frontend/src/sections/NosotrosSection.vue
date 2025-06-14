
<template>
  <!-- Sección "Sobre Nosotros" con diseño responsivo -->
  <section id="details" class="nosotros-section">
    <div class="container">
      <div class="row" style="margin-top: 2.5rem;">
        <!-- Columna de texto informativo -->
        <div class="col-lg-6 col-xl-5">
          <div class="text-container">
            <div class="section-title">Sobre Nosotros</div>
            <h2>¡10 años transformando estilos!</h2>
            <p>
              En Beard & Style, no solo cortamos cabello, ¡creamos experiencias!
              Nuestro equipo de expertos combina técnica y creatividad para
              resaltar lo mejor de ti.
            </p>
            <!-- Botón para reservar cita, navega a la ruta /citas -->
            <router-link class="btn-hero-solid" to="/citas">
              <i class="fas fa-calendar-check me-2"></i>Reserva ya
            </router-link>
          </div>
        </div>
        <!-- Columna de imagen ilustrativa -->
        <div class="col-lg-6 col-xl-7">
          <div class="image-container">
            <img class="img-fluid" src="assets/images/details-2.png" alt="alternative" />
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: "NosotrosSection" // Nombre del componente para identificación en Vue
};
</script>

