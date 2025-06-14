from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    email = models.EmailField('email address', unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    
    USERNAME_FIELD = 'username'  # Cambiado a username
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email', 'nombre', 'apellido']

    class Meta:
        db_table = 'usuarios'
        swappable = 'AUTH_USER_MODEL'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

class Appointment(models.Model):
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    date = models.DateTimeField()
    service = models.CharField(max_length=100)
    status = models.CharField(max_length=20, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
