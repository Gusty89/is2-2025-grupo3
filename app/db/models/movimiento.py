from sqlalchemy import Column, Integer, ForeignKey, DateTime, Enum # type: ignore
from sqlalchemy.orm import relationship # type: ignore
from app.db.base import Base
import enum
from datetime import datetime

class TipoMovimiento(str, enum.Enum):
    ENTRADA = "entrada"
    SALIDA = "salida"
    TRANSFERENCIA = "transferencia"

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

    # Relaciones
    producto = relationship("Producto", back_populates="movimientos")
    deposito_origen = relationship("Deposito", back_populates="movimientos_origen", foreign_keys=[deposito_origen_id])
    deposito_destino = relationship("Deposito", back_populates="movimientos_destino", foreign_keys=[deposito_destino_id])
    usuario = relationship("Usuario", back_populates="movimientos")
