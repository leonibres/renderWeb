# Documentación de la API REST - Backend BeardStyle

## Visión General

BeardStyle Backend es una API REST construida con Django y Django REST Framework que proporciona la funcionalidad para gestionar usuarios, autenticación y citas en una barbería. La API permite a los clientes registrarse, iniciar sesión, y gestionar sus citas de forma segura.

---

## Tecnologías Utilizadas

- **Django**: Framework web de Python
- **Django REST Framework**: Biblioteca para construir APIs RESTful
- **SQLite/PostgreSQL**: Base de datos (configurable)
- **Autenticación por Sesión**: Para mantener el estado de la sesión del usuario

---

## Estructura de Carpetas

```
backend/
├── barber_app/                # Aplicación principal
│   ├── __init__.py
│   ├── admin.py               # Configuración del panel de administración
│   ├── apps.py                # Configuración de la aplicación
│   ├── models.py              # Definición de modelos de datos
│   ├── serializers.py         # Serializadores para la API REST
│   ├── tests.py               # Tests unitarios y de integración
│   ├── urls.py                # Rutas de la API
│   └── views.py               # Lógica de controladores/vistas
├── barbershop/                # Configuración del proyecto
│   ├── __init__.py
│   ├── asgi.py                # Configuración ASGI
│   ├── settings.py            # Configuraciones del proyecto
│   ├── urls.py                # Rutas del proyecto
│   └── wsgi.py                # Configuración WSGI
├── manage.py                  # Script de gestión de Django
└── requirements.txt           # Dependencias del proyecto
```

---

## Modelos de Datos

### Usuario (`Usuario`)

```python
class Usuario(AbstractUser):
    """
    Modelo personalizado de usuario que extiende AbstractUser.
    """
    email = models.EmailField(unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD = 'username'  # Configurable a 'email' si se prefiere login con email

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.email})"
```

#### Campos

| Campo            | Tipo          | Descripción                                   |
| ---------------- | ------------- | --------------------------------------------- |
| `email`          | EmailField    | Email único del usuario                       |
| `nombre`         | CharField     | Nombre del usuario                            |
| `apellido`       | CharField     | Apellido del usuario                          |
| `fecha_registro` | DateTimeField | Fecha y hora de registro (automática)         |
| `username`       | CharField     | Heredado de AbstractUser, usado para login    |
| `password`       | CharField     | Heredado de AbstractUser, almacenado con hash |

### Cita (`Appointment`)

```python
class Appointment(models.Model):
    """
    Modelo para almacenar las citas de los usuarios.
    """
    ESTADOS = (
        ('pendiente', 'Pendiente'),
        ('confirmada', 'Confirmada'),
        ('completada', 'Completada'),
        ('cancelada', 'Cancelada'),
    )

    user = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='appointments')
    date = models.DateTimeField()
    service = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=ESTADOS, default='pendiente')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.service} - {self.user.nombre} - {self.date}"
```

#### Campos

| Campo        | Tipo          | Descripción                                  |
| ------------ | ------------- | -------------------------------------------- |
| `user`       | ForeignKey    | Referencia al usuario propietario de la cita |
| `date`       | DateTimeField | Fecha y hora de la cita                      |
| `service`    | CharField     | Servicio solicitado                          |
| `status`     | CharField     | Estado de la cita (pendiente, etc.)          |
| `created_at` | DateTimeField | Fecha y hora de creación de la cita          |

---

## Serializadores

### UsuarioSerializer

```python
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('id', 'username', 'email', 'nombre', 'apellido', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # Si no hay username, usar email como username
        if 'username' not in validated_data:
            validated_data['username'] = validated_data['email']

        # Crear usuario con contraseña hasheada
        user = Usuario(
            username=validated_data['username'],
            email=validated_data['email'],
            nombre=validated_data.get('nombre', ''),
            apellido=validated_data.get('apellido', '')
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
```

### AppointmentSerializer

```python
class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ('id', 'user', 'date', 'service', 'status', 'created_at')
        read_only_fields = ('id', 'user', 'created_at')

    def create(self, validated_data):
        # Asignar usuario actual como propietario de la cita
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)
```

---

## Endpoints de la API

### Autenticación y Usuarios

#### 1. Registro de Usuario

- **URL**: `/api/auth/register/`
- **Método**: `POST`
- **CSRF**: Exento
- **Permisos**: Público (No requiere autenticación)

**Cuerpo de la solicitud**:

```json
{
  "email": "usuario@ejemplo.com",
  "password": "ContraseñaSegura123",
  "nombre": "Juan",
  "apellido": "Pérez",
  "username": "juanperez" // Opcional, si no se proporciona se usa el email
}
```

**Respuesta exitosa (201 Created)**:

```json
{
  "id": 1,
  "username": "juanperez",
  "email": "usuario@ejemplo.com",
  "nombre": "Juan",
  "apellido": "Pérez"
}
```

**Posibles errores**:

- `400 Bad Request`: Si el email ya está en uso o los datos son inválidos
- `500 Internal Server Error`: Error interno del servidor

#### 2. Inicio de Sesión

- **URL**: `/api/auth/login/`
- **Método**: `POST`
- **CSRF**: Exento
- **Permisos**: Público (No requiere autenticación)

**Cuerpo de la solicitud**:

```json
{
  "email": "usuario@ejemplo.com",
  "password": "ContraseñaSegura123"
}
```

**Respuesta exitosa (200 OK)**:

```json
{
  "id": 1,
  "username": "juanperez",
  "email": "usuario@ejemplo.com",
  "nombre": "Juan",
  "apellido": "Pérez"
}
```

**Cookies establecidas**:

- `sessionid`: Cookie de sesión para mantener la autenticación
- `csrftoken`: Token CSRF para protección contra ataques CSRF

**Posibles errores**:

- `400 Bad Request`: Credenciales inválidas
- `500 Internal Server Error`: Error interno del servidor

#### 3. Cierre de Sesión

- **URL**: `/api/auth/logout/`
- **Método**: `POST`
- **CSRF**: Exento
- **Permisos**: Usuario autenticado

**Respuesta exitosa (200 OK)**:

```json
{
  "message": "Sesión finalizada correctamente"
}
```

**Posibles errores**:

- `401 Unauthorized`: Si el usuario no está autenticado
- `500 Internal Server Error`: Error interno del servidor

### Gestión de Citas

#### 4. Listar y Crear Citas

- **URL**: `/api/appointments/`
- **Métodos**: `GET` (listar), `POST` (crear)
- **CSRF**: Requiere token
- **Permisos**: Usuario autenticado

**GET - Listar citas del usuario**

**Respuesta exitosa (200 OK)**:

```json
[
  {
    "id": 1,
    "date": "2023-06-20T15:00:00Z",
    "service": "Corte de Cabello",
    "status": "pendiente",
    "created_at": "2023-06-15T10:30:00Z"
  },
  {
    "id": 2,
    "date": "2023-06-22T16:30:00Z",
    "service": "Arreglo de Barba",
    "status": "confirmada",
    "created_at": "2023-06-15T11:45:00Z"
  }
]
```

**POST - Crear nueva cita**

**Cuerpo de la solicitud**:

```json
{
  "date": "2023-06-25T14:00:00Z",
  "service": "Corte y Barba",
  "status": "pendiente"
}
```

**Respuesta exitosa (201 Created)**:

```json
{
  "id": 3,
  "user": 1,
  "date": "2023-06-25T14:00:00Z",
  "service": "Corte y Barba",
  "status": "pendiente",
  "created_at": "2023-06-16T09:20:00Z"
}
```

**Posibles errores**:

- `400 Bad Request`: Datos inválidos
- `401 Unauthorized`: Usuario no autenticado
- `403 Forbidden`: CSRF token inválido
- `500 Internal Server Error`: Error interno del servidor

#### 5. Ver, Editar y Eliminar Cita Específica

- **URL**: `/api/appointments/{id}/`
- **Métodos**: `GET` (ver), `PUT` (actualizar), `DELETE` (eliminar)
- **CSRF**: Requiere token
- **Permisos**: Usuario autenticado (solo sus propias citas)

**GET - Ver una cita específica**

**Respuesta exitosa (200 OK)**:

```json
{
  "id": 1,
  "user": 1,
  "date": "2023-06-20T15:00:00Z",
  "service": "Corte de Cabello",
  "status": "pendiente",
  "created_at": "2023-06-15T10:30:00Z"
}
```

**PUT - Actualizar una cita**

**Cuerpo de la solicitud**:

```json
{
  "date": "2023-06-21T16:00:00Z",
  "service": "Corte de Cabello",
  "status": "confirmada"
}
```

**Respuesta exitosa (200 OK)**:

```json
{
  "id": 1,
  "user": 1,
  "date": "2023-06-21T16:00:00Z",
  "service": "Corte de Cabello",
  "status": "confirmada",
  "created_at": "2023-06-15T10:30:00Z"
}
```

**DELETE - Eliminar una cita**

**Respuesta exitosa (204 No Content)**
(No hay cuerpo en la respuesta)

**Posibles errores**:

- `400 Bad Request`: Datos inválidos en la actualización
- `401 Unauthorized`: Usuario no autenticado
- `403 Forbidden`: Intento de acceder a cita de otro usuario o CSRF token inválido
- `404 Not Found`: ID de cita inexistente
- `500 Internal Server Error`: Error interno del servidor

#### 6. Listar Mis Citas

- **URL**: `/api/appointments/my/`
- **Método**: `GET`
- **CSRF**: Requiere token
- **Permisos**: Usuario autenticado

**Respuesta exitosa (200 OK)**:

```json
[
  {
    "id": 1,
    "date": "2023-06-20T15:00:00Z",
    "service": "Corte de Cabello",
    "status": "pendiente",
    "created_at": "2023-06-15T10:30:00Z"
  },
  {
    "id": 2,
    "date": "2023-06-22T16:30:00Z",
    "service": "Arreglo de Barba",
    "status": "confirmada",
    "created_at": "2023-06-15T11:45:00Z"
  }
]
```

**Posibles errores**:

- `401 Unauthorized`: Usuario no autenticado
- `500 Internal Server Error`: Error interno del servidor

#### 7. Raíz de la API

- **URL**: `/api/`
- **Método**: `GET`
- **CSRF**: No aplica
- **Permisos**: Público

**Respuesta exitosa (200 OK)**:

```json
{
  "auth": "http://localhost:8000/api/auth/",
  "appointments": "http://localhost:8000/api/appointments/",
  "my_appointments": "http://localhost:8000/api/appointments/my/"
}
```

---

## Configuración de Seguridad

### CORS (Cross-Origin Resource Sharing)

```python
# settings.py
CORS_ALLOWED_ORIGINS = [
    "http://localhost:8080",
    "http://127.0.0.1:8080",
    # Agregar aquí otros orígenes permitidos
]

CORS_ALLOW_CREDENTIALS = True  # Permite enviar cookies en solicitudes CORS
```

### CSRF (Cross-Site Request Forgery)

La API utiliza protección CSRF para todos los endpoints excepto login, registro y logout:

```python
# views.py
@method_decorator(csrf_exempt, name='dispatch')
class LoginView(APIView):
    # Implementación...

@method_decorator(csrf_exempt, name='dispatch')
class RegisterView(APIView):
    # Implementación...

@method_decorator(csrf_exempt, name='dispatch')
class LogoutView(APIView):
    # Implementación...
```

Para endpoints protegidos, el frontend debe enviar el token CSRF en el encabezado `X-CSRFToken`.

### Autenticación

La API utiliza autenticación basada en sesión (`SessionAuthentication` de Django REST Framework):

```python
# settings.py
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
    ],
}
```

---

## Guía de Desarrollo

### Extensión de la API

Para añadir nuevos endpoints:

1. Definir nuevos modelos en `models.py` si es necesario
2. Crear serializadores en `serializers.py`
3. Implementar vistas en `views.py`
4. Añadir URLs en `urls.py`

Ejemplo de extensión para servicios de barbería:

```python
# models.py
class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    duration = models.IntegerField(help_text="Duración en minutos")
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

# serializers.py
class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

# views.py
class ServiceList(generics.ListCreateAPIView):
    queryset = Service.objects.filter(active=True)
    serializer_class = ServiceSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class ServiceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [IsAdminUser]

# urls.py
urlpatterns += [
    path('services/', ServiceList.as_view(), name='service-list'),
    path('services/<int:pk>/', ServiceDetail.as_view(), name='service-detail'),
]
```

### Testing

Para ejecutar los tests:

```bash
python manage.py test barber_app
```

### Configuración de Variables de Entorno

Para mayor seguridad, utiliza variables de entorno para:

- `SECRET_KEY`
- Credenciales de base de datos
- Configuración de CORS
- Configuración de email

Ejemplo de `.env` para desarrollo:

```
DEBUG=True
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///db.sqlite3
ALLOWED_HOSTS=localhost,127.0.0.1
CORS_ALLOWED_ORIGINS=http://localhost:8080,http://127.0.0.1:8080
```

---

## Despliegue en Producción

Para producción, considera:

1. **Usar HTTPS**: Configura certificados SSL
2. **Base de datos robusta**: PostgreSQL es recomendado
3. **Configura cookies seguras**:
   ```python
   SESSION_COOKIE_SECURE = True
   CSRF_COOKIE_SECURE = True
   ```
4. **Servidor WSGI**: Gunicorn o uWSGI detrás de Nginx
5. **Monitoreo y logs**: Implementa logging adecuado
6. **Rate limiting**: Configura límites de tasa para prevenir abusos

---

## Troubleshooting

### Problemas Comunes

1. **Error CSRF**:

   - Asegúrate de incluir el token CSRF en las peticiones no exentas
   - Verifica que las cookies se envíen correctamente

2. **401 Unauthorized**:

   - Comprueba que la sesión esté activa
   - Intenta hacer login nuevamente

3. **CORS Issues**:

   - Verifica que el origen de tu frontend esté en CORS_ALLOWED_ORIGINS
   - Asegúrate de que CORS_ALLOW_CREDENTIALS sea True

4. **500 Internal Server Error**:
   - Revisa los logs del servidor para más detalles
   - Verifica la configuración de la base de datos

---

## Recursos Adicionales

- [Django REST Framework Documentation](https://www.django-rest-framework.org/)
- [Django Documentation](https://docs.djangoproject.com/)
- [Postman Collection para testing](https://www.postman.com/) (Crear y compartir una colección)

---

## Contribuciones

Si deseas contribuir a la API:

1. Crea un fork del repositorio
2. Crea una nueva rama para tu feature
3. Implementa tus cambios siguiendo las convenciones de estilo
4. Escribe tests para tu código
5. Envía un pull request

---

## Licencia

Este proyecto está bajo la Licencia MIT.

---

## Contacto

Para preguntas o soporte, contacta a:

- **Desarrollador:** LeoniBres
- **Email:** [contacto@ejemplo.com]
