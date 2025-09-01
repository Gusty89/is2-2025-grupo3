from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.base import Base

class ProductoORM(Base):
    __tablename__ = "productos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    sku = Column(String(50), unique=True, nullable=False)
    descripcion = Column(String(255))
    stock = Column(Integer, default=0)
    stock_minimo = Column(Integer, default=0)

    movimientos = relationship("MovimientoORM", back_populates="producto")
