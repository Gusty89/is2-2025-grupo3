from sqlalchemy.orm import sessionmaker
from .engine import engine

# Crear la clase de sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Función helper para usar sesiones con "with"
def get_session():
    """
    Devuelve una sesión de SQLAlchemy lista para usar con 'with'.
    Cierra la sesión automáticamente al finalizar.
    """
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()