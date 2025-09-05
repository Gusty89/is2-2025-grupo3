from pydantic import BaseModel
from typing import Optional
from datetime import datetime
import enum

class TipoMovimiento(str, enum.Enum):
    ENTRADA = "entrada"
    SALIDA = "salida"
    TRASPASO = "traspaso"

class MovimientoBase(BaseModel):
    producto_id: int
    deposito_origen_id: Optional[int] = None
    deposito_destino_id: Optional[int] = None
    usuario_id: int
    cantidad: int
    fecha: Optional[datetime] = None
    tipo: TipoMovimiento

class MovimientoCreate(MovimientoBase):
    pass

class MovimientoUpdate(BaseModel):
    producto_id: Optional[int] = None
    deposito_origen_id: Optional[int] = None
    deposito_destino_id: Optional[int] = None
    usuario_id: Optional[int] = None
    cantidad: Optional[int] = None
    fecha: Optional[datetime] = None
    tipo: Optional[TipoMovimiento] = None

class MovimientoDelete(BaseModel):
    id: int

class Movimiento(MovimientoBase):
    id: int

    class Config:
        from_attributes = True