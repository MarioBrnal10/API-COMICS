from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from DB.base import Base  # Usamos Base desde archivo separado

# Datos de conexión
USER = "root"
PASSWORD = "YUXnonFHtyVmERdMECmNmlFsYVQXWtAL"  # Si tienes contraseña, colócala aquí
HOST = "shortline.proxy.rlwy.net"
PORT = "20787"
DB_NAME = "railway"

# URL de conexión a MySQL con PyMySQL
DATABASE_URL = f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}"

# Crear el motor de conexión
engine = create_engine(DATABASE_URL, echo=True)

# Crear la sesión local
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()
