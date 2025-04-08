# conexion.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

USER = "root"
PASSWORD = "YUXnonFHtyVmERdMECmNmlFsYVQXWtAL"
HOST = "shortline.proxy.rlwy.net"
PORT = "20787"
DB_NAME = "railway"

DATABASE_URL = f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL, echo=True)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()
