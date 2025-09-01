from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.deposito import DepositoCreate, DepositoRead, DepositoUpdate
from app.repositories.deposito_repository import DepositoRepository

router = APIRouter(prefix="/depositos", tags=["Depósitos"])


@router.get("/", response_model=list[DepositoRead])
def listar_depositos(db: Session = Depends(get_db)):
    return DepositoRepository.listar(db)


@router.get("/{deposito_id}", response_model=DepositoRead)
def obtener_deposito(deposito_id: int, db: Session = Depends(get_db)):
    deposito = DepositoRepository.obtener_por_id(db, deposito_id)
    if not deposito:
        raise HTTPException(status_code=404, detail="Depósito no encontrado")
    return deposito


@router.post("/", response_model=DepositoRead)
def crear_deposito(deposito: DepositoCreate, db: Session = Depends(get_db)):
    return DepositoRepository.crear(db, deposito)


@router.put("/{deposito_id}", response_model=DepositoRead)
def actualizar_deposito(deposito_id: int, deposito: DepositoUpdate, db: Session = Depends(get_db)):
    actualizado = DepositoRepository.actualizar(db, deposito_id, deposito)
    if not actualizado:
        raise HTTPException(status_code=404, detail="Depósito no encontrado")
    return actualizado


@router.delete("/{deposito_id}", response_model=DepositoRead)
def eliminar_deposito(deposito_id: int, db: Session = Depends(get_db)):
    eliminado = DepositoRepository.eliminar(db, deposito_id)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Depósito no encontrado")
    return eliminado