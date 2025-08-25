from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..base import Base
from .usuario_rol import usuarios_roles

class RolORM(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String, unique=True, nullable=False)

    usuarios = relationship("UsuarioORM", secondary=usuarios_roles, back_populates="roles")