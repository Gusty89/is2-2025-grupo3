from sqlalchemy.orm import sessionmaker
from app.db.engine import engine

# Configuración de la sesión
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Función de utilidad para obtener la sesión en un contexto "with"
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()