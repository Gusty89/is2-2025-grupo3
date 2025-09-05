from pydantic import BaseModel, EmailStr
from typing import List, Optional

class UsuarioBase(BaseModel):
    username: str
    email: EmailStr
    is_active: bool = True

class UsuarioCreate(UsuarioBase):
    hashed_password: str

class UsuarioUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = None
    hashed_password: Optional[str] = None

class UsuarioDelete(BaseModel):
    id: int

class Usuario(UsuarioBase):
    id: int

    class Config:
        from_attributes = True
