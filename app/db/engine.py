# app/db/engine.py
from sqlalchemy import create_engine # type: ignore

#Creación de la base de datos SQLite
DATABASE_URL = "sqlite:///./app/db/inventario_test.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}  # Necesario en SQLite
)
