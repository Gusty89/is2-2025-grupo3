from sqlalchemy.orm import Session
from app.db.models import DepositoORM


def crear_deposito(db: Session, nombre: str, ubicacion: str | None = None):
    deposito = DepositoORM(nombre=nombre, ubicacion=ubicacion)
    db.add(deposito)
    db.commit()
    db.refresh(deposito)
    return deposito


def listar_depositos(db: Session):
    return db.query(DepositoORM).all()


def obtener_deposito(db: Session, deposito_id: int):
    return db.query(DepositoORM).filter(DepositoORM.id == deposito_id).first()


def actualizar_deposito(
    db: Session, deposito_id: int, nombre: str | None = None, ubicacion: str | None = None
):
    deposito = obtener_deposito(db, deposito_id)
    if not deposito:
        return None
    if nombre is not None:
        deposito.nombre = nombre
    if ubicacion is not None:
        deposito.ubicacion = ubicacion
    db.commit()
    db.refresh(deposito)
    return deposito


def eliminar_deposito(db: Session, deposito_id: int):
    deposito = obtener_deposito(db, deposito_id)
    if not deposito:
        return None
    db.delete(deposito)
    db.commit()
    return deposito