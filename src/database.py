from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://rust_user:Aust6canc@localhost/syncHero"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Función para obtener una sesión de BD
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
