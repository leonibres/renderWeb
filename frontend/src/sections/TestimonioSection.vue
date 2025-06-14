<template>
  <!-- Sección de testimonios de clientes -->
  <section class="testimonio-section">
    <div class="container">
      <div class="row">
        <div class="col-12 text-center">
          <!-- Título de la sección -->
          <h2 class="section-title">Testimonios</h2>
          <!-- Subtítulo de la sección -->
          <p class="section-subtitle">
            Lo que nuestros clientes dicen de <strong>Beard & Style</strong>
          </p>
        </div>
      </div>
      <div class="row justify-content-center">
        <!-- Itera sobre cada testimonio y muestra su información -->
        <div class="col-md-4" v-for="(testimonio, idx) in testimonios" :key="idx">
          <div class="testimonio-card">
            <!-- Avatar del cliente -->
            <div class="testimonio-avatar">
              <img :src="testimonio.avatar" :alt="testimonio.nombre" />
            </div>
            <!-- Texto del testimonio -->
            <div class="testimonio-text">
              <p>"{{ testimonio.texto }}"</p>
            </div>
            <!-- Nombre y servicio recibido por el cliente -->
            <div class="testimonio-nombre">
              <strong>{{ testimonio.nombre }}</strong>
              <span class="testimonio-servicio">{{ testimonio.servicio }}</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: "TestimonioSection",
  data() {
    return {
      // Lista de testimonios de clientes
      testimonios: [
        {
          nombre: "Carlos Ramírez",
          servicio: "Corte y barba",
          texto: "¡Excelente atención y resultados! Siempre salgo renovado y satisfecho.",
          avatar: "/assets/images/testimonio1.jpg"
        },
        {
          nombre: "Juan Pérez",
          servicio: "Tratamiento capilar",
          texto: "El mejor lugar para cuidar mi cabello. ¡Recomendado 100%!",
          avatar: "/assets/images/testimonio2.jpg"
        },
        {
          nombre: "Andrés Gómez",
          servicio: "Arreglo de barba",
          texto: "Profesionales y muy atentos. Mi barba nunca había lucido tan bien.",
          avatar: "/assets/images/testimonio3.jpg"
        }
      ]
    };
  }
};
</script>

