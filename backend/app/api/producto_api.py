from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.producto import ProductoCreate, ProductoRead, ProductoUpdate
from app.repositories.producto_repository import ProductoRepository

router = APIRouter(prefix="/productos", tags=["Productos"])


@router.get("/", response_model=list[ProductoRead])
def listar_productos(db: Session = Depends(get_db)):
    return ProductoRepository.listar(db)


@router.get("/{producto_id}", response_model=ProductoRead)
def obtener_producto(producto_id: int, db: Session = Depends(get_db)):
    producto = ProductoRepository.obtener_por_id(db, producto_id)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto


@router.post("/", response_model=ProductoRead)
def crear_producto(producto: ProductoCreate, db: Session = Depends(get_db)):
    return ProductoRepository.crear(db, producto)


@router.put("/{producto_id}", response_model=ProductoRead)
def actualizar_producto(producto_id: int, producto: ProductoUpdate, db: Session = Depends(get_db)):
    actualizado = ProductoRepository.actualizar(db, producto_id, producto)
    if not actualizado:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return actualizado


@router.delete("/{producto_id}", response_model=ProductoRead)
def eliminar_producto(producto_id: int, db: Session = Depends(get_db)):
    eliminado = ProductoRepository.eliminar(db, producto_id)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return eliminado