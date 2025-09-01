from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from app.domain.models.producto import Producto
from app.domain.models.deposito import Deposito
from app.domain.models.usuario import Usuario
from enum import Enum

class TipoMovimiento(Enum):
    ENTRADA = "entrada"
    SALIDA = "salida"
    TRANSFERENCIA = "transferencia"

@dataclass
class Movimiento:
    id: Optional[int]
    producto_id: int
    deposito_origen_id: Optional[int]
    deposito_destino_id: Optional[int]
    usuario_id: int
    cantidad: int
    fecha: datetime
    tipo: TipoMovimiento

    producto: Optional[Producto] = None
    deposito_origen: Optional[Deposito] = None
    deposito_destino: Optional[Deposito] = None
    usuario: Optional[Usuario] = None
