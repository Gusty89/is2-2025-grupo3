from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..base import Base

class ProductoORM(Base):
    __tablename__ = "productos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String, nullable=False)
    sku = Column(String, unique=True, nullable=False)
    descripcion = Column(String)
    stock = Column(Integer, default=0, nullable=False)

    movimientos = relationship("MovimientoORM", back_populates="producto")