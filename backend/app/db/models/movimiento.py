from sqlalchemy import Column, Integer, DateTime, Enum, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base
from datetime import datetime
import enum

class TipoMovimiento(enum.Enum):
    ENTRADA = "entrada"
    SALIDA = "salida"
    TRASPASO = "traspaso"

class MovimientoORM(Base):
    __tablename__ = "movimientos"

    id = Column(Integer, primary_key=True, index=True)
    producto_id = Column(Integer, ForeignKey("productos.id"))
    deposito_origen_id = Column(Integer, ForeignKey("depositos.id"))
    deposito_destino_id = Column(Integer, ForeignKey("depositos.id"))
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    cantidad = Column(Integer, nullable=False)
    fecha = Column(DateTime, default=datetime.utcnow)
    tipo = Column(Enum(TipoMovimiento), nullable=False)

    producto = relationship("ProductoORM", back_populates="movimientos")
    deposito_origen = relationship("DepositoORM", back_populates="movimientos_origen", foreign_keys=[deposito_origen_id])
    deposito_destino = relationship("DepositoORM", back_populates="movimientos_destino", foreign_keys=[deposito_destino_id])
    usuario = relationship("UsuarioORM", back_populates="movimientos")

