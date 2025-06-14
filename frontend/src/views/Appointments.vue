<template>
  <div class="appointments">
    <h2>Gestionar Citas</h2>
    <div class="appointment-form">
      <!-- Formulario de citas -->
    </div>
    <div class="appointments-list">
      <!-- Lista de citas -->
    </div>
  </div>
</template>

<script>
import { appointmentService } from '../services/api'

export default {
  name: 'Appointments',
  data() {
    return {
      appointments: []
    }
  },
  methods: {
    async loadAppointments() {
      try {
        const response = await appointmentService.getAll()
        this.appointments = response.data
      } catch (error) {
        console.error('Error cargando citas:', error)
      }
    }
  },
  mounted() {
    this.loadAppointments()
  }
}
</script>
