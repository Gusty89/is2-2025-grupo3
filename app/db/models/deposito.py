# app/db/models/deposito.py
from sqlalchemy import Column, Integer, String # type: ignore
from sqlalchemy.orm import relationship # type: ignore
from app.db.base import Base

class DepositoORM(Base):
    __tablename__ = "depositos"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    ubicacion = Column(String(150), nullable=False)

    # Relaciones: un depósito puede estar en muchos movimientos
    movimientos_origen = relationship(
        "Movimiento",
        back_populates="deposito_origen",
        foreign_keys="Movimiento.deposito_origen_id"
    )

    movimientos_destino = relationship(
        "Movimiento",
        back_populates="deposito_destino",
        foreign_keys="Movimiento.deposito_destino_id"
    )