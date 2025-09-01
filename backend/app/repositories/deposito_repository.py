from sqlalchemy.orm import Session
from app.db.models.deposito import DepositoORM
from app.schemas.deposito import DepositoCreate, DepositoUpdate


class DepositoRepository:

    @staticmethod
    def listar(db: Session):
        return db.query(DepositoORM).all()

    @staticmethod
    def obtener_por_id(db: Session, deposito_id: int):
        return db.query(DepositoORM).filter(DepositoORM.id == deposito_id).first()

    @staticmethod
    def crear(db: Session, deposito: DepositoCreate):
        db_deposito = DepositoORM(**deposito.dict())
        db.add(db_deposito)
        db.commit()
        db.refresh(db_deposito)
        return db_deposito

    @staticmethod
    def actualizar(db: Session, deposito_id: int, deposito: DepositoUpdate):
        db_deposito = db.query(DepositoORM).filter(DepositoORM.id == deposito_id).first()
        if db_deposito:
            for key, value in deposito.dict(exclude_unset=True).items():
                setattr(db_deposito, key, value)
            db.commit()
            db.refresh(db_deposito)
        return db_deposito

    @staticmethod
    def eliminar(db: Session, deposito_id: int):
        db_deposito = db.query(DepositoORM).filter(DepositoORM.id == deposito_id).first()
        if db_deposito:
            db.delete(db_deposito)
            db.commit()
        return db_deposito
