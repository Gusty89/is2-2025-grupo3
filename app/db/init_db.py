from backend.app.db.models.base import Base
from .session import engine

# Función para inicializar la base de datos
def init_db():
    print("Creando las tablas en la base de datos...")
    Base.metadata.create_all(bind=engine)
    print("Tablas creadas con éxito.")

#Funcion que se ejecuta como modulo python -m app.db.init_db
if __name__ == "__main__":
    init_db()
