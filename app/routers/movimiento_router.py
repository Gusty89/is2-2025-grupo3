from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.db import models
from app.schemas.movimiento import MovimientoCreate, MovimientoResponse

router = APIRouter(prefix="/movimientos", tags=["Movimientos"])

# ------------------- Crear movimiento -------------------
@router.post("/", response_model=MovimientoResponse)
def crear_movimiento(movimiento: MovimientoCreate, db: Session = Depends(get_db)):
    nuevo_movimiento = models.MovimientoORM(**movimiento.dict())
    db.add(nuevo_movimiento)
    db.commit()
    db.refresh(nuevo_movimiento)
    return nuevo_movimiento


# ------------------- Listar movimientos -------------------
@router.get("/", response_model=list[MovimientoResponse])
def listar_movimientos(db: Session = Depends(get_db)):
    return db.query(models.MovimientoORM).all()


# ------------------- Obtener movimiento por ID -------------------
@router.get("/{movimiento_id}", response_model=MovimientoResponse)
def obtener_movimiento(movimiento_id: int, db: Session = Depends(get_db)):
    mov = db.query(models.MovimientoORM).filter(models.MovimientoORM.id == movimiento_id).first()
    if not mov:
        raise HTTPException(status_code=404, detail="Movimiento no encontrado")
    return mov


# ------------------- Actualizar movimiento -------------------
@router.put("/{movimiento_id}", response_model=MovimientoResponse)
def actualizar_movimiento(movimiento_id: int, movimiento: MovimientoCreate, db: Session = Depends(get_db)):
    mov = db.query(models.MovimientoORM).filter(models.MovimientoORM.id == movimiento_id).first()
    if not mov:
        raise HTTPException(status_code=404, detail="Movimiento no encontrado")

    for key, value in movimiento.dict().items():
        setattr(mov, key, value)

    db.commit()
    db.refresh(mov)
    return mov


# ------------------- Eliminar movimiento -------------------
@router.delete("/{movimiento_id}")
def eliminar_movimiento(movimiento_id: int, db: Session = Depends(get_db)):
    mov = db.query(models.MovimientoORM).filter(models.MovimientoORM.id == movimiento_id).first()
    if not mov:
        raise HTTPException(status_code=404, detail="Movimiento no encontrado")

    db.delete(mov)
    db.commit()
    return {"detail": f"Movimiento con id {movimiento_id} eliminado"}
