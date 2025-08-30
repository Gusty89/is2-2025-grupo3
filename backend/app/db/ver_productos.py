from app.db.engine import engine
from sqlalchemy.orm import sessionmaker
from app.db.models.producto import ProductoORM

SessionLocal = sessionmaker(bind=engine)
db = SessionLocal()

productos = db.query(ProductoORM).all()
for p in productos:
    print(p.id, p.nombre, p.sku, p.stock, p.stock_minimo)

db.close()