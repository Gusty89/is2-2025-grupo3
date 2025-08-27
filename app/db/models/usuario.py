from sqlalchemy import Column, Integer, String, Boolean # type: ignore
from sqlalchemy.orm import relationship # type: ignore
from app.db.base import Base

class UsuarioORM(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True)

    # Relaciones
    roles = relationship("Rol", secondary="usuarios_roles", back_populates="usuarios")
    movimientos = relationship("Movimiento", back_populates="usuario")
