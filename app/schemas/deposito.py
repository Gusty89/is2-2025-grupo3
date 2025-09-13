# app/schemas/deposito.py
from pydantic import BaseModel

class DepositoBase(BaseModel):
    nombre: str
    ubicacion: str

class DepositoCreate(DepositoBase):
    pass

class DepositoResponse(DepositoBase):
    id: int

    class Config:
        from_attributes = True