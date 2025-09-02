from app.db.session import SessionLocal
from app.db.models.producto import ProductoORM
from app.db.models.deposito import DepositoORM

db = SessionLocal()

# Crear producto de prueba
producto = ProductoORM(nombre="Producto Test", sku="0001", descripcion="Prueba", stock=10, stock_minimo=2)
db.add(producto)
# Crear depósito de prueba
deposito = DepositoORM(nombre="Depósito Central", direccion="Calle Falsa 123", capacidad_maxima=100)
db.add(deposito)

db.commit()

# Consultar y mostrar
print(db.query(ProductoORM).all())
print(db.query(DepositoORM).all())

db.close()
