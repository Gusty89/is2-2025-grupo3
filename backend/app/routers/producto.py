# backend/app/api/producto_api.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.db.models.producto import ProductoORM

router = APIRouter(prefix="/productos", tags=["productos"])

@router.get("/")
def listar_productos(db: Session = Depends(get_db)):
    return db.query(ProductoORM).all()

@router.post("/")
def crear_producto(nombre: str, sku: str, db: Session = Depends(get_db)):
    if db.query(ProductoORM).filter(ProductoORM.sku == sku).first():
        raise HTTPException(status_code=400, detail="SKU ya existe")
    producto = ProductoORM(nombre=nombre, sku=sku)
    db.add(producto)
    db.commit()
    db.refresh(producto)
    return producto
