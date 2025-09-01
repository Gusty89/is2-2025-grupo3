from pydantic import BaseModel, Field


class DepositoBase(BaseModel):
    nombre: str = Field(..., max_length=100)
    direccion: str | None = None
    capacidad_maxima: int = 0


class DepositoCreate(DepositoBase):
    pass


class DepositoUpdate(BaseModel):
    nombre: str | None = None
    direccion: str | None = None
    capacidad_maxima: int | None = None


class DepositoRead(DepositoBase):
    id: int

    class Config:
        orm_mode = True