from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from ..base import Base
from .usuario_rol import usuarios_roles

class UsuarioORM(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)

    roles = relationship("RolORM", secondary=usuarios_roles, back_populates="usuarios")
    movimientos = relationship("MovimientoORM", back_populates="usuario")