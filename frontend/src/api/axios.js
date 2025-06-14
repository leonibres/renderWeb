import axios from 'axios';

const api = axios.create({
    baseURL: 'http://localhost:8000',  // Ajusta según tu URL base
    timeout: 15000,  // Aumentamos el timeout a 15 segundos
    headers: {
        'Content-Type': 'application/json'
    }
});

// Interceptor para manejar errores
api.interceptors.response.use(
    response => response,
    error => {
        if (error.code === 'ECONNABORTED') {
            return Promise.reject({
                message: 'La solicitud tardó demasiado tiempo. Por favor, inténtelo de nuevo.'
            });
        }
        return Promise.reject(error);
    }
);

export default api;
