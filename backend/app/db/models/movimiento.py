from sqlalchemy import Column, Integer, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
import enum
from ..base import Base

class TipoMovimiento(enum.Enum):
    ENTRADA = "ENTRADA"
    SALIDA = "SALIDA"
    TRANSFERENCIA = "TRANSFERENCIA"

class MovimientoORM(Base):
    __tablename__ = "movimientos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    producto_id = Column(Integer, ForeignKey("productos.id"), nullable=False)
    deposito_origen_id = Column(Integer, ForeignKey("depositos.id"))
    deposito_destino_id = Column(Integer, ForeignKey("depositos.id"))
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    cantidad = Column(Integer, nullable=False)
    fecha = Column(DateTime, default=datetime.utcnow, nullable=False)
    tipo = Column(Enum(TipoMovimiento), nullable=False)

    producto = relationship("ProductoORM", back_populates="movimientos")
    usuario = relationship("UsuarioORM", back_populates="movimientos")
    deposito_origen = relationship("DepositoORM", foreign_keys=[deposito_origen_id], back_populates="movimientos_origen")
    deposito_destino = relationship("DepositoORM", foreign_keys=[deposito_destino_id], back_populates="movimientos_destino")