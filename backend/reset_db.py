import os
import shutil
from pathlib import Path

def reset_database():
    try:
        # Eliminar base de datos
        if os.path.exists('db.sqlite3'):
            os.remove('db.sqlite3')
            print("Base de datos eliminada")
        
        # Eliminar migraciones
        migrations_dir = Path('barber_app/migrations')
        if migrations_dir.exists():
            shutil.rmtree(migrations_dir)
            print("Carpeta de migraciones eliminada")
        
        # Crear carpeta de migraciones y __init__.py
        migrations_dir.mkdir(exist_ok=True)
        init_file = migrations_dir / '__init__.py'
        init_file.touch()
        print("Carpeta de migraciones reinicializada")
        
        print("\nAhora ejecuta:")
        print("1. python manage.py makemigrations barber_app")
        print("2. python manage.py migrate")
        print("3. python manage.py createsuperuser")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    reset_database()
