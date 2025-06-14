<template>
  <div class="my-appointments">
    <h2>Mis Citas</h2>
    <div v-if="appointments.length" class="appointments-list">
      <div v-for="appointment in appointments" :key="appointment.id" class="appointment-card">
        <h3>Cita: {{ appointment.date }}</h3>
        <p>Servicio: {{ appointment.service }}</p>
        <div class="actions">
          <button @click="editAppointment(appointment.id)">Editar</button>
          <button @click="deleteAppointment(appointment.id)">Cancelar</button>
        </div>
      </div>
    </div>
    <p v-else>No tienes citas programadas</p>
  </div>
</template>

<script>
export default {
  name: 'MyAppointments',
  data() {
    return {
      appointments: []
    }
  },
  methods: {
    async loadAppointments() {
      try {
        const response = await fetch('http://localhost:8000/api/appointments/my/');
        if (response.ok) {
          this.appointments = await response.json();
        }
      } catch (error) {
        console.error('Error cargando citas:', error);
      }
    },
    editAppointment(id) {
      this.$router.push(`/edit-appointment/${id}`);
    },
    async deleteAppointment(id) {
      if (confirm('¿Estás seguro de cancelar esta cita?')) {
        try {
          const response = await fetch(`http://localhost:8000/api/appointments/${id}/`, {
            method: 'DELETE'
          });
          if (response.ok) {
            this.loadAppointments();
          }
        } catch (error) {
          console.error('Error eliminando cita:', error);
        }
      }
    }
  },
  mounted() {
    this.loadAppointments();
  }
}
</script>
