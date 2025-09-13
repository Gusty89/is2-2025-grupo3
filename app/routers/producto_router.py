# app/routers/producto_router.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.db import models
from app.schemas.producto import ProductoCreate, ProductoResponse

router = APIRouter(prefix="/productos", tags=["Productos"])

@router.post("/", response_model=ProductoResponse)
def crear_producto(producto: ProductoCreate, db: Session = Depends(get_db)):
    nuevo = models.ProductoORM(**producto.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

@router.get("/", response_model=list[ProductoResponse])
def listar_productos(db: Session = Depends(get_db)):
    return db.query(models.ProductoORM).all()

@router.get("/{producto_id}", response_model=ProductoResponse)
def obtener_producto(producto_id: int, db: Session = Depends(get_db)):
    prod = db.query(models.ProductoORM).get(producto_id)
    if not prod:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return prod

@router.put("/{producto_id}", response_model=ProductoResponse)
def actualizar_producto(producto_id: int, datos: ProductoCreate, db: Session = Depends(get_db)):
    prod = db.query(models.ProductoORM).get(producto_id)
    if not prod:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    for key, value in datos.dict().items():
        setattr(prod, key, value)
    db.commit()
    db.refresh(prod)
    return prod

@router.delete("/{producto_id}")
def eliminar_producto(producto_id: int, db: Session = Depends(get_db)):
    prod = db.query(models.ProductoORM).get(producto_id)
    if not prod:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    db.delete(prod)
    db.commit()
    return {"detail": "Producto eliminado"}
