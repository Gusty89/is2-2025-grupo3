from sqlalchemy.orm import Session
from app.db.models.producto import ProductoORM
from app.schemas.producto import ProductoCreate, ProductoUpdate


class ProductoRepository:

    @staticmethod
    def listar(db: Session):
        return db.query(ProductoORM).all()

    @staticmethod
    def obtener_por_id(db: Session, producto_id: int):
        return db.query(ProductoORM).filter(ProductoORM.id == producto_id).first()

    @staticmethod
    def crear(db: Session, producto: ProductoCreate):
        db_producto = ProductoORM(**producto.dict())
        db.add(db_producto)
        db.commit()
        db.refresh(db_producto)
        return db_producto

    @staticmethod
    def actualizar(db: Session, producto_id: int, producto: ProductoUpdate):
        db_producto = db.query(ProductoORM).filter(ProductoORM.id == producto_id).first()
        if db_producto:
            for key, value in producto.dict(exclude_unset=True).items():
                setattr(db_producto, key, value)
            db.commit()
            db.refresh(db_producto)
        return db_producto

    @staticmethod
    def eliminar(db: Session, producto_id: int):
        db_producto = db.query(ProductoORM).filter(ProductoORM.id == producto_id).first()
        if db_producto:
            db.delete(db_producto)
            db.commit()
        return db_producto