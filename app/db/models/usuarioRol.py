from sqlalchemy import Column, Integer, ForeignKey # type: ignore
from sqlalchemy.orm import relationship # type: ignore
from app.db.base import Base

class UsuarioRolORM(Base):
    __tablename__ = "usuarios_roles"

    usuario_id = Column(Integer, ForeignKey("usuarios.id"), primary_key=True)
    rol_id = Column(Integer, ForeignKey("roles.id"), primary_key=True)

    usuario = relationship("Usuario", back_populates="roles")
    rol = relationship("Rol", back_populates="usuarios")
