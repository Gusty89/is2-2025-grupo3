from pydantic import BaseModel
from typing import Optional

class ProductoBase(BaseModel):
    nombre: str
    sku: str
    descripcion: Optional[str] = None
    stock: int = 0
    stock_minimo: int = 0

class ProductoCreate(ProductoBase):
    pass

class ProductoUpdate(BaseModel):
    nombre: Optional[str] = None
    sku: Optional[str] = None
    descripcion: Optional[str] = None
    stock: Optional[int] = None
    stock_minimo: Optional[int] = None

class ProductoDelete(BaseModel):
    id: int

class Producto(ProductoBase):
    id: int

    class Config:
        from_attributes = True
