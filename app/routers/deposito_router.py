# app/routers/deposito_router.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.db import models
from app.schemas.deposito import DepositoCreate, DepositoResponse

router = APIRouter(prefix="/depositos", tags=["Depósitos"])

@router.post("/", response_model=DepositoResponse)
def crear_deposito(deposito: DepositoCreate, db: Session = Depends(get_db)):
    nuevo = models.DepositoORM(**deposito.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

@router.get("/", response_model=list[DepositoResponse])
def listar_depositos(db: Session = Depends(get_db)):
    return db.query(models.DepositoORM).all()

@router.get("/{deposito_id}", response_model=DepositoResponse)
def obtener_deposito(deposito_id: int, db: Session = Depends(get_db)):
    deposito = db.query(models.DepositoORM).get(deposito_id)
    if not deposito:
        raise HTTPException(status_code=404, detail="Depósito no encontrado")
    return deposito

@router.put("/{deposito_id}", response_model=DepositoResponse)
def actualizar_deposito(deposito_id: int, datos: DepositoCreate, db: Session = Depends(get_db)):
    deposito = db.query(models.DepositoORM).get(deposito_id)
    if not deposito:
        raise HTTPException(status_code=404, detail="Depósito no encontrado")
    for key, value in datos.dict().items():
        setattr(deposito, key, value)
    db.commit()
    db.refresh(deposito)
    return deposito

@router.delete("/{deposito_id}")
def eliminar_deposito(deposito_id: int, db: Session = Depends(get_db)):
    deposito = db.query(models.DepositoORM).get(deposito_id)
    if not deposito:
        raise HTTPException(status_code=404, detail="Depósito no encontrado")
    db.delete(deposito)
    db.commit()
    return {"detail": "Depósito eliminado"}
