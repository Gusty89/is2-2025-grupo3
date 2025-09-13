# domain/models/movimiento.py
from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Optional

class TipoMovimiento(str, Enum):
    ENTRADA = "ENTRADA"
    SALIDA = "SALIDA"
    TRANSFERENCIA = "TRANSFERENCIA"

@dataclass
class Movimiento:
    id: Optional[int]
    producto_id: int
    deposito_origen_id: Optional[int]
    deposito_destino_id: Optional[int]
    usuario_id: int
    cantidad: int
    fecha_registro: datetime
    tipo: TipoMovimiento