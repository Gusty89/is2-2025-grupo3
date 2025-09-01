from dataclasses import dataclass
from typing import List, Optional
from app.domain.models.usuario import Usuario

@dataclass
class Rol:
    id: Optional[int]
    nombre: str
    usuarios: List[Usuario] = None
