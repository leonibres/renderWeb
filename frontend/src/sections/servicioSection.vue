<template>
  <!-- Sección principal de servicios -->
  <section id="services" class="servicio-section">
    <div class="container">
      <div class="row">
        <div class="col-lg-12" style="margin-top: 2.5rem;">
          <!-- Título de la sección -->
          <h2 class="section-title">Nuestros Servicios</h2>
          <!-- Subtítulo descriptivo -->
          <p class="section-subtitle text-center">
            Descubre los servicios que ofrecemos para cuidar tu estilo y apariencia.
          </p>
          <!-- Lista de servicios ofrecidos -->
          <div class="servicio-list">
            <!-- Servicio: Corte de Cabello -->
            <div class="servicio-item">
              <span class="servicio-icon fas fa-cut"></span>
              <h3>Corte de Cabello</h3>
              <p>
                Ofrecemos cortes modernos y clásicos adaptados a tu estilo.
                Nuestros barberos están capacitados para brindarte el mejor look.
              </p>
            </div>
            <!-- Servicio: Arreglo de Barba -->
            <div class="servicio-item">
              <span class="servicio-icon fas fa-user-tie"></span>
              <h3>Arreglo de Barba</h3>
              <p>
                Desde un perfilado perfecto hasta un afeitado completo, cuidamos
                cada detalle para que tu barba luzca impecable.
              </p>
            </div>
            <!-- Servicio: Tratamientos Capilares -->
            <div class="servicio-item">
              <span class="servicio-icon fas fa-spa"></span>
              <h3>Tratamientos Capilares</h3>
              <p>
                Utilizamos productos de alta calidad para tratamientos capilares
                que fortalecen y revitalizan tu cabello.
              </p>
            </div>
          </div>
          <!-- Fin de la lista de servicios -->
        </div>
      </div>
    </div>
  </section>
</template>

<script>
// Componente que representa la sección de servicios
export default {
  name: "ServicioSection"
};
</script>
