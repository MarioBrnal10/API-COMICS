from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Datos de conexión
USER = "root"
PASSWORD = "YUXnonFHtyVmERdMECmNmlFsYVQXWtAL"
HOST = "shortline.proxy.rlwy.net"
PORT = "20787"
DB_NAME = "railway"

# URL de conexión con PyMySQL
DATABASE_URL = f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}"

# Crear el motor de SQLAlchemy
engine = create_engine(DATABASE_URL, echo=True)

# Crear sesión local
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Generador de sesión (para usar en dependencias de FastAPI)
def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()
