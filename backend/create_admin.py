import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'barbershop.settings')
django.setup()

from barber_app.models import Usuario

def create_superuser():
    try:
        Usuario.objects.create_superuser(
            username='admin',
            email='admin@beardstyle.com',
            password='Admin123456',
            nombre='Admin',
            apellido='System'
        )
        print("Superusuario creado exitosamente")
    except Exception as e:
        print(f"Error al crear superusuario: {e}")

if __name__ == '__main__':
    create_superuser()
