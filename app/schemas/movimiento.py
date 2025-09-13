from pydantic import BaseModel
from datetime import datetime
from typing import Optional
import enum

class TipoMovimiento(str, enum.Enum):
    ENTRADA = "ENTRADA"
    SALIDA = "SALIDA"
    TRANSFERENCIA = "TRANSFERENCIA"

# ------------------- Base -------------------
class MovimientoBase(BaseModel):
    producto_id: int
    deposito_origen_id: Optional[int] = None
    deposito_destino_id: Optional[int] = None
    usuario_id: int
    cantidad: int
    tipo: TipoMovimiento

# ------------------- Entrada (POST) -------------------
class MovimientoCreate(MovimientoBase):
    """Para crear un movimiento, no se manda ni id ni fecha_registro"""
    pass

# ------------------- Salida (Response) -------------------
class MovimientoResponse(MovimientoBase):
    id: int
    fecha_registro: datetime   # la BD lo genera automáticamente

    class Config:
        from_attributes = True  # si usás Pydantic v2
        # orm_mode = True  # si usás Pydantic v1
