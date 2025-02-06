import sys
import os

# Agregar la ruta raíz del proyecto al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.database import engine, Base

print("Creando las tablas en la base de datos...")
Base.metadata.create_all(bind=engine)
print("¡Tablas creadas exitosamente!")
