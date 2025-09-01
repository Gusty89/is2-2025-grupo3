from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from app.db.base import Base
from app.db.models.rol import RolORM  # asumimos que existe

class UsuarioORM(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True)

    roles = relationship("RolORM", secondary="usuario_roles", back_populates="usuarios")  # tabla asociativa usuario_roles
    movimientos = relationship("MovimientoORM", back_populates="usuario")
