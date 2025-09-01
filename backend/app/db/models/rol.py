from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base
from app.db.models.usuario import UsuarioORM

# Tabla asociativa Usuario <-> Rol
usuario_roles = Table(
    "usuario_roles",
    Base.metadata,
    Column("usuario_id", Integer, ForeignKey("usuarios.id"), primary_key=True),
    Column("rol_id", Integer, ForeignKey("roles.id"), primary_key=True)
)

class RolORM(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50), unique=True, nullable=False)

    usuarios = relationship("UsuarioORM", secondary=usuario_roles, back_populates="roles")
