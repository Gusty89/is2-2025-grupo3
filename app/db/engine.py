from sqlalchemy import create_engine

# URL de la base de datos SQLite
DATABASE_URL = "sqlite:///./app/db/inventario_test.db"

# Creación del engine de SQLAlchemy
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}  # Necesario solo para SQLite
)