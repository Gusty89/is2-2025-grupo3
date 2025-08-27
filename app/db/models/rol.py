from sqlalchemy import Column, Integer, String # type: ignore
from sqlalchemy.orm import relationship # type: ignore
from app.db.base import Base

class RolORM(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50), unique=True, nullable=False)

    usuarios = relationship("Usuario", secondary="usuarios_roles", back_populates="roles")
