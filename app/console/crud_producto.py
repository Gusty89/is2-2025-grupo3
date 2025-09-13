from sqlalchemy.orm import Session
from app.db.models.producto import ProductoORM as Producto

# Crear producto
def crear_producto(db: Session, nombre: str, descripcion: str, sku: str, stock: int, stock_minimo: int):
    nuevo_producto = Producto(
        nombre=nombre,
        descripcion=descripcion,
        sku=sku,  # usar el SKU que pasó el usuario o generado previamente
        stock=stock,
        stock_minimo=stock_minimo  # usar el valor real
    )
    db.add(nuevo_producto)
    db.commit()
    db.refresh(nuevo_producto)
    return nuevo_producto

# Obtener producto por ID
def obtener_producto(db: Session, producto_id: int):
    return db.query(Producto).filter(Producto.id == producto_id).first()

# Listar todos los productos
def listar_productos(db: Session):
    return db.query(Producto).all()

# Actualizar producto
def actualizar_producto(
    db: Session, 
    producto_id: int, 
    nombre: str = None, 
    descripcion: str = None, 
    sku: str = None, 
    stock: int = None, 
    stock_minimo: int = None):
    
    producto = db.query(Producto).filter(Producto.id == producto_id).first()
    if not producto:
        return None
    if nombre is not None:
        producto.nombre = nombre
    if descripcion is not None:
        producto.descripcion = descripcion
    if sku is not None:
        producto.sku = sku
    if stock is not None:
        producto.stock = stock
    if stock_minimo is not None:
        producto.stock_minimo = stock_minimo
    db.commit()
    db.refresh(producto)
    return producto

# Eliminar producto
def eliminar_producto(db: Session, producto_id: int):
    producto = db.query(Producto).filter(Producto.id == producto_id).first()
    if not producto:
        return None
    db.delete(producto)
    db.commit()
    return producto
