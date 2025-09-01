from sqlalchemy import Column, Integer, DateTime, Enum, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base
import enum
from datetime import datetime

# Enum para el tipo de movimiento
class TipoMovimiento(enum.Enum):
    ENTRADA = "entrada"
    SALIDA = "salida"
    TRASPASO = "traspaso"

class MovimientoORM(Base):
    __tablename__ = "movimientos"

    id = Column(Integer, primary_key=True, index=True)              # +int id
    producto_id = Column(Integer, ForeignKey("productos.id"))       # +int producto_id
    deposito_origen_id = Column(Integer, ForeignKey("depositos.id"))  # +int deposito_origen_id
    deposito_destino_id = Column(Integer, ForeignKey("depositos.id")) # +int deposito_destino_id
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))         # +int usuario_id
    cantidad = Column(Integer, nullable=False)                      # +int cantidad
    fecha = Column(DateTime, default=datetime.utcnow)               # +datetime fecha
    tipo = Column(Enum(TipoMovimiento), nullable=False)             # +enum tipo

    # Relaciones ORM
    producto = relationship("ProductoORM", back_populates="movimientos")          # +Producto producto
    deposito_origen = relationship("DepositoORM", foreign_keys=[deposito_origen_id]) # +Deposito deposito_origen
    deposito_destino = relationship("DepositoORM", foreign_keys=[deposito_destino_id]) # +Deposito deposito_destino
    usuario = relationship("UsuarioORM")                                         # +Usuario usuario
