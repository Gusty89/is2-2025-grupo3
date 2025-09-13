from sqlalchemy.orm import Session
from app.db.models.rol import RolORM as Rol

# ------------------- Crear rol -------------------
def crear_rol(db: Session, nombre: str):
    nuevo_rol = Rol(nombre=nombre)
    db.add(nuevo_rol)
    db.commit()
    db.refresh(nuevo_rol)
    return nuevo_rol

# ------------------- Obtener rol por ID -------------------
def obtener_rol(db: Session, rol_id: int):
    return db.query(Rol).filter(Rol.id == rol_id).first()

# ------------------- Listar todos los roles -------------------
def listar_roles(db: Session):
    return db.query(Rol).all()

# ------------------- Actualizar rol -------------------
def actualizar_rol(db: Session, rol_id: int, nombre: str = None):
    rol = db.query(Rol).filter(Rol.id == rol_id).first()
    if not rol:
        return None
    
    if nombre is not None:
        rol.nombre = nombre

    db.commit()
    db.refresh(rol)
    return rol

# ------------------- Eliminar rol -------------------
def eliminar_rol(db: Session, rol_id: int):
    rol = db.query(Rol).filter(Rol.id == rol_id).first()
    if not rol:
        return None

    db.delete(rol)
    db.commit()
    return rol
