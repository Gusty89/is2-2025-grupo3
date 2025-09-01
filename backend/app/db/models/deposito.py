from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.base import Base

class DepositoORM(Base):
    __tablename__ = "depositos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    ubicacion = Column(String(255))

    movimientos_origen = relationship("MovimientoORM", back_populates="deposito_origen", foreign_keys="MovimientoORM.deposito_origen_id")
    movimientos_destino = relationship("MovimientoORM", back_populates="deposito_destino", foreign_keys="MovimientoORM.deposito_destino_id")
