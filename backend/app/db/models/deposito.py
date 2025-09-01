# backend/app/db/models/deposito.py
from sqlalchemy import Column, Integer, String
from app.db.session import Base

class DepositoORM(Base):
    __tablename__ = "deposito"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String(100), nullable=False, unique=True)
    direccion = Column(String(255))
    capacidad_maxima = Column(Integer, default=0)
