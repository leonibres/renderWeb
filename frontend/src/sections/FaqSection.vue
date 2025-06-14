<template>
  <!-- FAQ Section -->
  <section id="faq" class="faq-section">
    <div class="container">
      <!-- Section Title and Subtitle -->
      <div class="row" style="margin-top: 2.5rem;">
        <div class="col-xl-12 text-center">
          <h2 class="section-title">Preguntas Frecuentes</h2>
          <p class="section-subtitle">
            Encuentra respuestas a las preguntas más comunes sobre nuestros
            servicios y horarios.
          </p>
        </div>
      </div>
      <div class="row justify-content-center">
        <div class="col-xl-8">
          <!-- FAQ Accordion -->
          <div class="faq-accordion" id="faqAccordion">
            <!-- FAQ Item 1: Horarios de atención -->
            <div class="faq-item">
              <div class="faq-header" id="headingOne">
                <button class="faq-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapseOne"
                  aria-expanded="true" aria-controls="collapseOne">
                  <span class="faq-icon bg-primary">
                    <i class="fas fa-clock"></i>
                  </span>
                  <span class="faq-question">¿Cuáles son los horarios de atención?</span>
                  <span class="faq-arrow">
                    <i class="fas fa-chevron-down"></i>
                  </span>
                </button>
              </div>
              <div id="collapseOne" class="accordion-collapse collapse show" aria-labelledby="headingOne"
                data-bs-parent="#faqAccordion">
                <div class="faq-answer">
                  Nuestro horario es de lunes a viernes de 7:00 am a 7:00 pm, y
                  los sábados y domingos de 10:00 am a 5:00 pm.
                </div>
              </div>
            </div>

            <!-- FAQ Item 2: Servicios ofrecidos -->
            <div class="faq-item">
              <div class="faq-header" id="headingTwo">
                <button class="faq-button collapsed" type="button" data-bs-toggle="collapse"
                  data-bs-target="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">
                  <span class="faq-icon bg-info">
                    <i class="fas fa-cut"></i>
                  </span>
                  <span class="faq-question">¿Qué servicios ofrecen?</span>
                  <span class="faq-arrow">
                    <i class="fas fa-chevron-down"></i>
                  </span>
                </button>
              </div>
              <div id="collapseTwo" class="accordion-collapse collapse" aria-labelledby="headingTwo"
                data-bs-parent="#faqAccordion">
                <div class="faq-answer">
                  Ofrecemos cortes de cabello, arreglo de barba, y combos de
                  corte + barba. También utilizamos productos de alta calidad
                  para el cuidado personal.
                </div>
              </div>
            </div>

            <!-- FAQ Item 3: Reserva de cita -->
            <div class="faq-item">
              <div class="faq-header" id="headingThree">
                <button class="faq-button collapsed" type="button" data-bs-toggle="collapse"
                  data-bs-target="#collapseThree" aria-expanded="false" aria-controls="collapseThree">
                  <span class="faq-icon bg-purple">
                    <i class="fas fa-calendar-check"></i>
                  </span>
                  <span class="faq-question">¿Es necesario reservar cita?</span>
                  <span class="faq-arrow">
                    <i class="fas fa-chevron-down"></i>
                  </span>
                </button>
              </div>
              <div id="collapseThree" class="accordion-collapse collapse" aria-labelledby="headingThree"
                data-bs-parent="#faqAccordion">
                <div class="faq-answer">
                  Recomendamos reservar tu cita para garantizar disponibilidad,
                  pero también aceptamos clientes sin cita según la
                  disponibilidad.
                </div>
              </div>
            </div>

            <!-- FAQ Item 4: Ubicación -->
            <div class="faq-item">
              <div class="faq-header" id="headingFour">
                <button class="faq-button collapsed" type="button" data-bs-toggle="collapse"
                  data-bs-target="#collapseFour" aria-expanded="false" aria-controls="collapseFour">
                  <span class="faq-icon bg-warning">
                    <i class="fas fa-map-marker-alt"></i>
                  </span>
                  <span class="faq-question">¿Dónde están ubicados?</span>
                  <span class="faq-arrow">
                    <i class="fas fa-chevron-down"></i>
                  </span>
                </button>
              </div>
              <div id="collapseFour" class="accordion-collapse collapse" aria-labelledby="headingFour"
                data-bs-parent="#faqAccordion">
                <div class="faq-answer">
                  Estamos ubicados en Calle 10 # 43A-00 Int 101, Barrio El
                  Poblado, Medellín, Colombia.
                </div>
              </div>
            </div>
            <!-- End FAQ Items -->
          </div>
          <!-- End FAQ Accordion -->
        </div>
      </div>
    </div>
  </section>
</template>

<script>
// Componente de sección de preguntas frecuentes (FAQ)
export default {
  name: "FaqSection"
};
</script>


