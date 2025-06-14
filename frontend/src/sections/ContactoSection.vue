
<template>
  <!-- Sección de contacto principal -->
  <section id="contact" class="contacto-section">
    <div class="container">
      <div class="row">
        <!-- Columna de información de contacto -->
        <div class="col-lg-6" style="margin-top: 2.5rem;">
          <div class="text-container">
            <!-- Título de la sección -->
            <div class="section-title">Contáctanos</div>
            <h2>Reserva o consulta tu cita</h2>
            <p>
              En <strong>Beard & Style</strong>, estamos aquí para ayudarte. Si
              tienes preguntas o deseas reservar una cita, completa el
              formulario y nos pondremos en contacto contigo lo antes posible.
            </p>
            <!-- Lista de información de contacto -->
            <ul class="list-unstyled li-space-lg">
              <li class="d-flex">
                <i class="fas fa-phone-alt"></i>
                <div class="flex-grow-1">
                  <strong>Teléfono:</strong> +57 300 123 4567
                </div>
              </li>
              <li class="d-flex">
                <i class="fas fa-envelope"></i>
                <div class="flex-grow-1">
                  <strong>Email:</strong> contacto@beardandstyle.com
                </div>
              </li>
              <li class="d-flex">
                <i class="fas fa-map-marker-alt"></i>
                <div class="flex-grow-1">
                  <strong>Dirección:</strong> Calle 10 # 43A-00 Int 101, Barrio
                  El Poblado, Medellín, Colombia
                </div>
              </li>
            </ul>
          </div>
        </div>
        <!-- Columna del formulario de contacto -->
        <div class="col-lg-6" style="margin-top: 2.5rem;">
          <form>
            <!-- Campo para el nombre del usuario -->
            <div class="form-group">
              <input type="text" class="form-control-input" placeholder="Nombre" required />
            </div>
            <!-- Campo para el correo electrónico del usuario -->
            <div class="form-group">
              <input type="email" class="form-control-input" placeholder="Correo Electrónico" required />
            </div>
            <!-- Campo para el mensaje del usuario -->
            <div class="form-group">
              <textarea class="form-control-input" placeholder="Mensaje" rows="4" required></textarea>
            </div>
            <!-- Botón para enviar el formulario -->
            <div class="form-group">
              <button type="submit" class="form-control-submit-button">
                Enviar
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: "ContactoSection" // Nombre del componente
};
</script>
