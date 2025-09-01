from dataclasses import dataclass
from typing import List, Optional
from app.domain.models.movimiento import Movimiento
from app.domain.models.rol import Rol

@dataclass
class Usuario:
    id: Optional[int]
    username: str
    email: str
    hashed_password: str
    is_active: bool = True
    roles: List[Rol] = None
    movimientos: List[Movimiento] = None
