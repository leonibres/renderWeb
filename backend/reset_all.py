import os
import shutil
from pathlib import Path

def reset_database():
    # Detener procesos que usen la base de datos
    try:
        import psutil
        for proc in psutil.process_iter():
            try:
                if 'python' in proc.name().lower():
                    for file in proc.open_files():
                        if 'db.sqlite3' in file.path:
                            proc.kill()
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass
    except ImportError:
        print("psutil no está instalado. Continuando...")

    try:
        # Eliminar base de datos
        db_path = Path('db.sqlite3')
        if db_path.exists():
            os.remove(db_path)
            print("✓ Base de datos eliminada")

        # Eliminar migraciones
        migrations_dir = Path('barber_app/migrations')
        if migrations_dir.exists():
            shutil.rmtree(migrations_dir)
            print("✓ Carpeta de migraciones eliminada")

        # Crear carpeta de migraciones y __init__.py
        migrations_dir.mkdir(exist_ok=True)
        init_file = migrations_dir / '__init__.py'
        init_file.touch()
        print("✓ Nueva carpeta de migraciones creada")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    reset_database()
