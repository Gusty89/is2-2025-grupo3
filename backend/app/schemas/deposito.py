from pydantic import BaseModel
from typing import Optional, List

class DepositoBase(BaseModel):
    nombre: str
    ubicacion: Optional[str] = None

class DepositoCreate(DepositoBase):
    pass

class DepositoUpdate(BaseModel):
    nombre: Optional[str] = None
    ubicacion: Optional[str] = None

class DepositoDelete(BaseModel):
    id: int

class Deposito(DepositoBase):
    id: int
    movimientos_origen: List[int] = []
    movimientos_destino: List[int] = []

    model_config = {
        "from_attributes": True
    }