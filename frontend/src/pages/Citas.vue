<template>
  <div class="admin-citas-panel">
    <!-- Header -->
    <header class="admin-header">
      <div class="header-content">
        <div class="header-title">
          <i class="fas fa-cut"></i>
          <h1>Tu cita, tu estilo, tu momento</h1>
        </div>
        <div class="user-info">
          <span>Bienvenido, <strong>Leoni</strong></span>
          <div class="user-avatar">L</div>
        </div>
      </div>
    </header>

    <!-- Panel principal -->
    <main class="admin-main">
      <section class="citas-section">
        <div class="section-header">
          <h2><i class="fas fa-calendar-alt"></i> Gestión de Citas</h2>
          <button class="btn-primary" @click="abrirFormularioNuevaCita">
            <i class="fas fa-plus"></i> Nueva Cita
          </button>
        </div>

        <!-- Listado de citas -->
        <div class="citas-container">
          <div v-if="citas.length === 0" class="empty-state">
            <i class="fas fa-calendar-times"></i>
            <h3>No hay citas registradas</h3>
            <button class="btn-primary" @click="abrirFormularioNuevaCita">
              <i class="fas fa-cut"></i> Crear primera cita
            </button>
          </div>

          <div v-else class="citas-grid">
            <div v-for="cita in citas" :key="cita.id || cita._id" class="cita-card" :class="cita.status">
              <div class="card-header">
                <h3>{{ cita.service }}</h3>
                <span class="status-badge">{{ formatEstado(cita.status) }}</span>
              </div>
              
              <div class="card-body">
                <div class="info-item">
                  <i class="fas fa-calendar-day"></i>
                  <span>{{ formatFecha(cita.date) }}</span>
                </div>
                <div class="info-item">
                  <i class="fas fa-clock"></i>
                  <span>{{ cita.date ? cita.date.slice(11, 16) : '' }}</span>
                </div>
                <!-- Si tienes comentario en el modelo, descomenta esto:
                <div v-if="cita.comentario" class="info-item">
                  <i class="fas fa-comment"></i>
                  <span>{{ cita.comentario }}</span>
                </div>
                -->
              </div>
              
              <div class="card-actions">
                <button class="btn-icon edit" @click="abrirFormularioEditarCita(cita)" title="Editar">
                  <i class="fas fa-edit"></i>
                </button>
                <button class="btn-icon delete" @click="abrirModalEliminarCita(cita)" title="Eliminar">
                  <i class="fas fa-trash-alt"></i>
                </button>
              </div>
            </div>
          </div>
        </div>
      </section>
    </main>

    <!-- Formulario de cita -->
    <div v-if="showForm" class="form-overlay" @click.self="cerrarFormulario">
      <div class="cita-form">
        <div class="form-header">
          <h3>{{ editando ? 'Editar Cita' : 'Nueva Cita' }}</h3>
          <button class="btn-close" @click="cerrarFormulario">
            <i class="fas fa-times"></i>
          </button>
        </div>
        
        <form @submit.prevent="editando ? actualizarCita() : crearCita()">
          <div class="form-group">
            <label>Servicio</label>
            <select v-model="form.servicio" required>
              <option value="" disabled>Seleccione un servicio</option>
              <option v-for="serv in servicios" :key="serv.id" :value="serv.nombre">{{ serv.nombre }}</option>
            </select>
          </div>
          
          <div class="form-row">
            <div class="form-group">
              <label>Fecha</label>
              <input type="date" v-model="form.fecha" :min="minFecha" required>
            </div>
            <div class="form-group">
              <label>Hora</label>
              <select v-model="form.hora" required>
                <option value="" disabled>Seleccione hora</option>
                <option v-for="hora in horasDisponibles" :key="hora" :value="hora">{{ hora }}</option>
              </select>
            </div>
          </div>
          
          <div class="form-group">
            <label>Comentarios</label>
            <textarea v-model="form.comentario" placeholder="Opcional"></textarea>
          </div>
          
          <div class="form-group">
            <label>Estado</label>
            <select v-model="form.estado" required>
              <option value="pendiente">Pendiente</option>
              <option value="confirmada">Confirmada</option>
              <option value="completada">Completada</option>
              <option value="cancelada">Cancelada</option>
            </select>
          </div>
          
          <div class="form-actions">
            <button type="button" class="btn-secondary" @click="cerrarFormulario">Cancelar</button>
            <button type="submit" class="btn-primary">
              {{ editando ? 'Guardar cambios' : 'Crear cita' }}
            </button>
          </div>
        </form>
      </div>
    </div>

    <!-- Modal de confirmación -->
    <div v-if="showModalEliminar" class="modal-overlay" @click.self="cerrarModalEliminar">
      <div class="confirm-modal">
        <div class="modal-header">
          <h3>Confirmar eliminación</h3>
        </div>
        <div class="modal-body">
          <p>¿Está seguro que desea eliminar esta cita?</p>
          <p class="text-muted">Esta acción no se puede deshacer.</p>
        </div>
        <div class="modal-footer">
          <button class="btn-secondary" @click="cerrarModalEliminar">Cancelar</button>
          <button class="btn-danger" @click="eliminarCitaConfirmada">Eliminar</button>
        </div>
      </div>
    </div>

    <!-- Notificación -->
    <transition name="fade">
      <div v-if="notificacion" class="notification">
        {{ notificacion }}
      </div>
    </transition>
  </div>
</template>

<script>
import { appointmentService } from '../services/api';

export default {
  name: 'Citas',
  data() {
    return {
      citas: [],
      servicios: [
        { id: 1, nombre: 'Corte de Cabello' },
        { id: 2, nombre: 'Afeitado Clásico' },
        { id: 3, nombre: 'Corte y Barba' },
        { id: 4, nombre: 'Arreglo de Barba' },
        { id: 5, nombre: 'Tratamiento Capilar' }
      ],
      horasDisponibles: [
        '09:00', '09:30', '10:00', '10:30', '11:00', '11:30',
        '12:00', '12:30', '15:00', '15:30', '16:00', '16:30',
        '17:00', '17:30', '18:00'
      ],
      form: {
        servicio: '',
        fecha: '',
        hora: '',
        comentario: '',
        estado: 'pendiente'
      },
      editando: false,
      editId: null,
      showForm: false,
      showModalEliminar: false,
      citaAEliminar: null,
      notificacion: ''
    };
  },
  computed: {
    minFecha() {
      return new Date().toISOString().split('T')[0];
    }
  },
  methods: {
    getCookie(name) {
      let value = "; " + document.cookie;
      let parts = value.split("; " + name + "=");
      if (parts.length === 2) return parts.pop().split(";").shift();
    },
    async cargarCitas() {
      try {
        const response = await appointmentService.getMine();
        this.citas = response.data;
      } catch (error) {
        console.error('Error al cargar citas:', error);
        this.mostrarNotificacion('Error al cargar las citas');
      }
    },
    formatFecha(fecha) {
      if (!fecha) return '';
      const d = new Date(fecha);
      return d.toLocaleDateString('es-CO', { year: 'numeric', month: 'short', day: 'numeric' });
    },
    formatEstado(estado) {
      const estados = {
        'pendiente': 'Pendiente',
        'confirmada': 'Confirmada',
        'completada': 'Completada',
        'cancelada': 'Cancelada'
      };
      return estados[estado] || estado;
    },
    mostrarNotificacion(mensaje) {
      this.notificacion = mensaje;
      setTimeout(() => this.notificacion = '', 3000);
    },
    abrirFormularioNuevaCita() {
      this.editando = false;
      this.form = { servicio: '', fecha: '', hora: '', comentario: '', estado: 'pendiente' };
      this.showForm = true;
    },
    abrirFormularioEditarCita(cita) {
      this.editando = true;
      this.editId = cita.id || cita._id;
      this.form = {
        servicio: cita.service || cita.servicio,
        fecha: cita.date ? cita.date.slice(0, 10) : (cita.fecha ? cita.fecha.slice(0, 10) : ''),
        hora: cita.date ? cita.date.slice(11, 16) : (cita.hora || ''),
        comentario: cita.comentario || '',
        estado: cita.status || cita.estado || 'pendiente'
      };
      this.showForm = true;
    },
    cerrarFormulario() {
      this.showForm = false;
    },
    async crearCita() {
      try {
        const csrfToken = this.getCookie('csrftoken');
        const citaData = {
          service: this.form.servicio,
          date: `${this.form.fecha}T${this.form.hora}`,
          status: this.form.estado
        };
        console.log('Enviando datos cita:', citaData);
        await appointmentService.create(citaData, {
          headers: { 'X-CSRFToken': csrfToken },
          withCredentials: true
        });
        this.mostrarNotificacion('Cita creada correctamente');
        await this.cargarCitas();
        this.cerrarFormulario();
      } catch (error) {
        let msg = 'Error al crear la cita';
        // Log detallado para depuración
        console.error('Respuesta error cita:', error?.response?.data || error);
        if (error.response && error.response.data) {
          if (typeof error.response.data === 'string') {
            msg = error.response.data;
          } else if (error.response.data.detail) {
            msg = error.response.data.detail;
          } else if (error.response.data.error) {
            msg = error.response.data.error;
          } else if (typeof error.response.data === 'object') {
            msg = Object.values(error.response.data).join(' ');
          }
        } else if (error.message) {
          msg = error.message;
        }
        this.mostrarNotificacion(msg);
      }
    },
    async actualizarCita() {
      try {
        const citaData = {
          service: this.form.servicio,
          date: `${this.form.fecha}T${this.form.hora}`,
          status: this.form.estado
        };
        await appointmentService.update(this.editId, citaData);
        this.mostrarNotificacion('Cita actualizada correctamente');
        this.cerrarFormulario();
        this.cargarCitas();
      } catch (e) {
        this.mostrarNotificacion('Error al actualizar cita');
      }
    },
    abrirModalEliminarCita(cita) {
      this.citaAEliminar = cita;
      this.showModalEliminar = true;
    },
    cerrarModalEliminar() {
      this.showModalEliminar = false;
    },
    async eliminarCitaConfirmada() {
      try {
        await appointmentService.delete(this.citaAEliminar.id || this.citaAEliminar._id);
        this.mostrarNotificacion('Cita eliminada correctamente');
        this.cerrarModalEliminar();
        this.cargarCitas();
      } catch (e) {
        this.mostrarNotificacion('Error al eliminar cita');
      }
    }
  },
  mounted() {
    this.cargarCitas();
  }
};
</script>
