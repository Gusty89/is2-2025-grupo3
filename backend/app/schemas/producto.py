from typing import Optional
from pydantic import BaseModel, Field, validator

class ProductoSchema(BaseModel):
    id: Optional[int] = None
    nombre: str
    sku: str
    descripcion: Optional[str] = None
    stock: int
    stock_minimo: int = Field(..., alias="stockMinimo")  # alias opcional para JSON

    @validator('stock', 'stock_minimo')
    def no_negativos(cls, v):
        if v < 0:
            raise ValueError('El valor no puede ser negativo')
        return v

    # Métodos opcionales del dataclass
    def hay_stock(self, cantidad: int) -> bool:
        return self.stock >= cantidad

    def necesita_reposicion(self) -> bool:
        return self.stock < self.stock_minimo

    class Config:
        allow_population_by_field_name = True
