from app.db.base import Base
from app.db.session import engine
from sqlalchemy.orm import Session
from app.db.session import SessionLocal

def init_db():
    print("Creando las tablas en la base de datos...")
    Base.metadata.create_all(bind=engine)
    print("Tablas creadas con éxito.")

if __name__ == "__main__":
    init_db()


# app/console/script.py

from app.db.session import SessionLocal

# Importa solo el modelo ProductoORM
from app.db.models.producto import ProductoORM

# 5. Insertar datos

# Función para insertar un producto de prueba
def insertarProducto():
    db = SessionLocal()
    try:
        print("Iniciando inserción de producto de prueba...")
        
        nuevo_producto = ProductoORM(
            nombre="Producto Ejemplo", 
            sku="0001", 
            descripcion="Test", 
            stock=10, 
            stock_minimo=2
        )
        
        db.add(nuevo_producto)
        db.commit()
        db.refresh(nuevo_producto)
        
        print(f"Producto '{nuevo_producto.nombre}' insertado con ID: {nuevo_producto.id}")
        
    except Exception as e:
        db.rollback()
        print(f"Ocurrió un error: {e}")
    finally:
        db.close()

# Este bloque asegura que la función solo se ejecute cuando el archivo se corra directamente
if __name__ == "__main__":
    insertarProducto()
    