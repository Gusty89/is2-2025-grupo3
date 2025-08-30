from dataclasses import dataclass
from typing import Optional

@dataclass
class Producto:
    id: Optional[int]
    nombre: str
    sku: str
    descripcion: Optional[str]
    stock: int
    stock_minimo: int

    def hay_stock(self, cantidad: int) -> bool:
        return self.stock >= cantidad

    def necesita_reposicion(self) -> bool:
        return self.stock < self.stock_minimo
