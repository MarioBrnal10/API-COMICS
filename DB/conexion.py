from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from DB.base import Base  # Usamos Base desde archivo separado
import os

# Nombre del archivo de base de datos SQLite
DB_NAME = "tienda_comics.sqlite"

# Ruta del archivo (opcionalmente puedes usar os.path para rutas absolutas)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE_URL = f"sqlite:///{os.path.join(BASE_DIR, DB_NAME)}"

# Crear el motor de conexión
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},  # Necesario para SQLite con FastAPI
    echo=True
)

# Crear la sesión local
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
