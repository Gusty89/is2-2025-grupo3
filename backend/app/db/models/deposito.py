from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..base import Base

class DepositoORM(Base):
    __tablename__ = "depositos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String, nullable=False)
    ubicacion = Column(String)

    movimientos_origen = relationship(
        "MovimientoORM", foreign_keys="MovimientoORM.deposito_origen_id", back_populates="deposito_origen"
    )
    movimientos_destino = relationship(
        "MovimientoORM", foreign_keys="MovimientoORM.deposito_destino_id", back_populates="deposito_destino"
    )