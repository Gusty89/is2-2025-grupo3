from pydantic import BaseModel, Field


class ProductoBase(BaseModel):
    nombre: str = Field(..., max_length=100)
    sku: str = Field(..., max_length=50)
    descripcion: str | None = None
    stock: int = 0
    stock_minimo: int = 0


class ProductoCreate(ProductoBase):
    pass


class ProductoUpdate(BaseModel):
    nombre: str | None = None
    descripcion: str | None = None
    stock: int | None = None
    stock_minimo: int | None = None


class ProductoRead(ProductoBase):
    id: int

    class Config:
        orm_mode = True
