<template>
  <section class="edit-appointment">
    <div class="container">
      <h2>Editar Cita</h2>
      
      <!-- Alerta de error -->
      <div v-if="error" class="alert alert-error">
        {{ error }}
      </div>

      <form @submit.prevent="updateAppointment" class="appointment-form">
        <!-- Información del Cliente -->
        <div class="form-section">
          <h3>Información del Cliente</h3>
          <div class="form-group">
            <label for="nombre">Nombre</label>
            <input 
              id="nombre" 
              v-model="appointment.nombre" 
              type="text" 
              required 
              disabled
            />
          </div>
          <div class="form-group">
            <label for="email">Email</label>
            <input 
              id="email" 
              v-model="appointment.email" 
              type="email" 
              required 
              disabled
            />
          </div>
        </div>

        <!-- Detalles de la Cita -->
        <div class="form-section">
          <h3>Detalles de la Cita</h3>
          <div class="form-group">
            <label for="fecha">Fecha</label>
            <input 
              id="fecha" 
              v-model="appointment.fecha" 
              type="date" 
              required
              :min="minDate"
            />
          </div>
          <div class="form-group">
            <label for="hora">Hora</label>
            <select 
              id="hora" 
              v-model="appointment.hora" 
              required
            >
              <option v-for="time in availableTimes" :key="time" :value="time">
                {{ time }}
              </option>
            </select>
          </div>
          <div class="form-group">
            <label for="servicio">Servicio</label>
            <select 
              id="servicio" 
              v-model="appointment.servicio" 
              required
            >
              <option v-for="service in services" :key="service._id" :value="service._id">
                {{ service.name }} - {{ formatPrice(service.price) }}
              </option>
            </select>
          </div>
          <div class="form-group">
            <label for="comentario">Comentarios</label>
            <textarea 
              id="comentario" 
              v-model="appointment.comentario" 
              rows="3"
            ></textarea>
          </div>
        </div>

        <!-- Estado de la Cita -->
        <div class="form-section">
          <h3>Estado de la Cita</h3>
          <div class="form-group">
            <label for="estado">Estado</label>
            <select 
              id="estado" 
              v-model="appointment.estado"
              :class="appointment.estado"
            >
              <option value="pendiente">Pendiente</option>
              <option value="confirmada">Confirmada</option>
              <option value="completada">Completada</option>
              <option value="cancelada">Cancelada</option>
            </select>
          </div>
        </div>

        <div class="form-actions">
          <button type="button" class="btn btn-secondary" @click="goBack">
            Cancelar
          </button>
          <button type="submit" class="btn btn-primary" :disabled="loading">
            {{ loading ? 'Guardando...' : 'Guardar Cambios' }}
          </button>
        </div>
      </form>
    </div>
  </section>
</template>

<script>
import axios from "axios";
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';

export default {
  name: "EditAppointment",
  props: {
    id: {
      type: String,
      required: true
    }
  },

  setup(props) {
    const router = useRouter();
    const appointment = ref({
      nombre: "",
      email: "",
      fecha: "",
      hora: "",
      servicio: "",
      estado: "",
      comentario: ""
    });
    const loading = ref(false);
    const error = ref(null);
    const services = ref([]);

    const availableTimes = [
      '09:00', '09:30', '10:00', '10:30', '11:00', '11:30',
      '12:00', '12:30', '15:00', '15:30', '16:00', '16:30',
      '17:00', '17:30', '18:00'
    ];

    const minDate = new Date().toISOString().split('T')[0];

    const formatPrice = (price) => {
      return new Intl.NumberFormat('es-CO', {
        style: 'currency',
        currency: 'COP'
      }).format(price);
    };

    const loadAppointment = async () => {
      try {
        loading.value = true;
        error.value = null;
        const token = localStorage.getItem("token");
        const response = await axios.get(`/api/appointments/${props.id}`, {
          headers: { Authorization: `Bearer ${token}` }
        });
        appointment.value = {
          nombre: response.data.data.nombre,
          email: response.data.data.email,
          fecha: response.data.data.fecha,
          hora: response.data.data.hora,
          servicio: response.data.data.servicio._id,
          estado: response.data.data.estado,
          comentario: response.data.data.comentario || ''
        };
      } catch (err) {
        error.value = 'Error al cargar la cita. Por favor, intente de nuevo.';
        console.error('Error loading appointment:', err);
      } finally {
        loading.value = false;
      }
    };

    const loadServices = async () => {
      try {
        const token = localStorage.getItem("token");
        const response = await axios.get('/api/services', {
          headers: { Authorization: `Bearer ${token}` }
        });
        services.value = response.data;
      } catch (err) {
        console.error('Error loading services:', err);
      }
    };

    const updateAppointment = async () => {
      try {
        loading.value = true;
        error.value = null;
        const token = localStorage.getItem("token");
        
        await axios.patch(`/api/appointments/${props.id}`, {
          fecha: appointment.value.fecha,
          hora: appointment.value.hora,
          servicio: appointment.value.servicio,
          estado: appointment.value.estado,
          comentario: appointment.value.comentario
        }, {
          headers: { Authorization: `Bearer ${token}` }
        });

        router.push('/appointments');
      } catch (err) {
        error.value = err.response?.data?.message || 
          'Error al actualizar la cita. Por favor, intente de nuevo.';
        console.error('Error updating appointment:', err);
      } finally {
        loading.value = false;
      }
    };

    const goBack = () => {
      router.back();
    };

    onMounted(() => {
      loadAppointment();
      loadServices();
    });

    return {
      appointment,
      loading,
      error,
      services,
      availableTimes,
      minDate,
      formatPrice,
      updateAppointment,
      goBack
    };
  }
};
</script>

<style scoped>
.edit-appointment {
  padding: 2rem;
  max-width: 800px;
  margin: 0 auto;
}

.container {
  background: white;
  padding: 2rem;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.appointment-form {
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.form-section {
  border: 1px solid #e0e0e0;
  padding: 1.5rem;
  border-radius: 4px;
}

.form-section h3 {
  margin-top: 0;
  margin-bottom: 1rem;
  color: #2c3e50;
}

.form-group {
  margin-bottom: 1rem;
}

label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: 500;
  color: #4a5568;
}

input, select, textarea {
  width: 100%;
  padding: 0.5rem;
  border: 1px solid #cbd5e0;
  border-radius: 4px;
  font-size: 1rem;
}

input:disabled {
  background-color: #f7fafc;
  cursor: not-allowed;
}

textarea {
  resize: vertical;
  min-height: 100px;
}

.form-actions {
  display: flex;
  gap: 1rem;
  justify-content: flex-end;
  margin-top: 1rem;
}

.btn {
  padding: 0.5rem 1rem;
  border-radius: 4px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s;
}

.btn-primary {
  background-color: #4299e1;
  color: white;
  border: none;
}

.btn-primary:hover {
  background-color: #3182ce;
}

.btn-primary:disabled {
  background-color: #90cdf4;
  cursor: not-allowed;
}

.btn-secondary {
  background-color: #e2e8f0;
  color: #4a5568;
  border: none;
}

.btn-secondary:hover {
  background-color: #cbd5e0;
}

.alert {
  padding: 1rem;
  border-radius: 4px;
  margin-bottom: 1rem;
}

.alert-error {
  background-color: #fed7d7;
  color: #c53030;
  border: 1px solid #fc8181;
}

select.pendiente { color: #d69e2e; }
select.confirmada { color: #2f855a; }
select.completada { color: #2c5282; }
select.cancelada { color: #c53030; }
</style>
