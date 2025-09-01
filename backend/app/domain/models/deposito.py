from dataclasses import dataclass
from typing import Optional

@dataclass
class Deposito:
    id: Optional[int]
    nombre: str
    direccion: str
    capacidad_maxima: int

    def tiene_espacio(self, cantidad: int) -> bool:
        """Verifica si hay espacio suficiente para almacenar la cantidad indicada."""
        return cantidad <= self.capacidad_maxima

    def puede_almacenar(self, cantidad: int) -> bool:
        """Alias para consistencia semántica, retorna True si se puede almacenar."""
        return self.tiene_espacio(cantidad)