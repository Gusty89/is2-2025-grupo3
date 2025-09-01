# backend/app/api/deposito_api.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.db.models.deposito import DepositoORM

router = APIRouter(prefix="/depositos", tags=["depositos"])

@router.get("/")
def listar_depositos(db: Session = Depends(get_db)):
    return db.query(DepositoORM).all()

@router.post("/")
def crear_deposito(nombre: str, direccion: str = "", db: Session = Depends(get_db)):
    if db.query(DepositoORM).filter(DepositoORM.nombre == nombre).first():
        raise HTTPException(status_code=400, detail="Depósito ya existe")
    deposito = DepositoORM(nombre=nombre, direccion=direccion)
    db.add(deposito)
    db.commit()
    db.refresh(deposito)
    return deposito
