from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from DB.base import Base  # Usamos Base desde archivo separado

# Datos de conexión
USER = "root"
PASSWORD = ""  # Si tienes contraseña, colócala aquí
HOST = "localhost"
PORT = "3306"
DB_NAME = "tienda_comics"

# URL de conexión a MySQL con PyMySQL
DATABASE_URL = f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}"

# Crear el motor de conexión
engine = create_engine(DATABASE_URL, echo=True)

# Crear la sesión local
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
