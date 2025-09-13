# app/routers/rol_router.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.db import models
from app.schemas.rol import RolCreate, RolResponse

router = APIRouter(prefix="/roles", tags=["Roles"])

@router.post("/", response_model=RolResponse)
def crear_rol(rol: RolCreate, db: Session = Depends(get_db)):
    nuevo = models.RolORM(**rol.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

@router.get("/", response_model=list[RolResponse])
def listar_roles(db: Session = Depends(get_db)):
    return db.query(models.RolORM).all()

@router.get("/{rol_id}", response_model=RolResponse)
def obtener_rol(rol_id: int, db: Session = Depends(get_db)):
    rol = db.query(models.RolORM).get(rol_id)
    if not rol:
        raise HTTPException(status_code=404, detail="Rol no encontrado")
    return rol

@router.put("/{rol_id}", response_model=RolResponse)
def actualizar_rol(rol_id: int, datos: RolCreate, db: Session = Depends(get_db)):
    rol = db.query(models.RolORM).get(rol_id)
    if not rol:
        raise HTTPException(status_code=404, detail="Rol no encontrado")
    for key, value in datos.dict().items():
        setattr(rol, key, value)
    db.commit()
    db.refresh(rol)
    return rol

@router.delete("/{rol_id}")
def eliminar_rol(rol_id: int, db: Session = Depends(get_db)):
    rol = db.query(models.RolORM).get(rol_id)
    if not rol:
        raise HTTPException(status_code=404, detail="Rol no encontrado")
    db.delete(rol)
    db.commit()
    return {"detail": "Rol eliminado"}
