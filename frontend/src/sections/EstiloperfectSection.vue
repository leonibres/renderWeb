<template>
  <!-- Sección principal que presenta el mensaje de bienvenida y llamado a la acción -->
  <section class="estiloperfect-section">
    <div class="container">
      <div class="row">
        <div class="col-lg-12">
          <!-- Contenedor de texto con título, descripción y botón de reserva -->
          <div class="text-container estiloperfect-text">
            <!-- Título principal de la sección -->
            <h2 class="estiloperfect-title">¡Encuentra tu estilo perfecto con nosotros!</h2>
            <!-- Descripción breve de los servicios -->
            <p class="p-large estiloperfect-desc">
              En <strong>Beard & Style</strong>, nos especializamos en realzar
              tu imagen con cortes modernos, arreglos de barba impecables y un
              servicio excepcional. ¡Déjanos cuidar de tu estilo!
            </p>
            <!-- Botón para reservar cita, navega a la ruta /citas -->
            <router-link class="btn-hero-solid estiloperfect-btn" to="/citas">
              <i class="fas fa-calendar-check me-2"></i>Reserva tu cita ahora
            </router-link>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
// Componente de sección para mostrar información destacada y botón de reserva
export default {
  name: "EstiloperfectSection"
};
</script>



