# app/schemas/usuario.py
from pydantic import BaseModel, EmailStr
from typing import List, Optional
#from datetime import datetime
from app.schemas.rol import RolBase as RolSchema
from app.schemas.movimiento import MovimientoBase as MovimientoSchema

# --- Schema para CREAR usuario ---
class UsuarioBase(BaseModel):
    username: str
    email: EmailStr
    hashed_password: str
    is_active: bool = True
    roles: Optional[List[RolSchema]] = []
    movimientos: Optional[List[MovimientoSchema]] = []

# --- Schema para RESPONDER usuario ---
class UsuarioCreate(UsuarioBase):
    pass

class UsuarioResponse(UsuarioBase):
    id: int

    class Config:
        from_attributes = True     
