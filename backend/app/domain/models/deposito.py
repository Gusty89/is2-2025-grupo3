from dataclasses import dataclass
from typing import List, Optional
from app.domain.models.movimiento import Movimiento

@dataclass
class Deposito:
    id: Optional[int]
    nombre: str
    ubicacion: Optional[str]
    movimientos_origen: List[Movimiento] = None
    movimientos_destino: List[Movimiento] = None
