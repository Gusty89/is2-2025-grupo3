from sqlalchemy import Column, Integer, DateTime, Enum, ForeignKey, func
from sqlalchemy.orm import relationship
from .base import Base
from datetime import datetime
import enum

class TipoMovimiento(enum.Enum):
    ENTRADA = "ENTRADA"
    SALIDA = "SALIDA"
    TRANSFERENCIA = "TRANSFERENCIA"

class MovimientoORM(Base):
    __tablename__ = "movimientos"

    id = Column(Integer, primary_key=True, index=True)
    producto_id = Column(Integer, ForeignKey("productos.id"))
    deposito_origen_id = Column(Integer, ForeignKey("depositos.id"))
    deposito_destino_id = Column(Integer, ForeignKey("depositos.id"))
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    cantidad = Column(Integer, nullable=False)
    fecha_registro = Column(DateTime(timezone=True), server_default=func.now())  # se genera automáticamente
    tipo = Column(Enum(TipoMovimiento), nullable=False)

    producto = relationship("ProductoORM", back_populates="movimientos")
    deposito_origen = relationship("DepositoORM", back_populates="movimientos_origen", foreign_keys=[deposito_origen_id])
    deposito_destino = relationship("DepositoORM", back_populates="movimientos_destino", foreign_keys=[deposito_destino_id])
    usuario = relationship("UsuarioORM", back_populates="movimientos")

