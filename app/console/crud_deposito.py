from sqlalchemy.orm import Session
from app.db.models.deposito import DepositoORM as Deposito

# ------------------- Crear depósito -------------------
def crear_deposito(db: Session, nombre: str, ubicacion: str):
    nuevo_deposito = Deposito(
        nombre=nombre,
        ubicacion=ubicacion
    )
    db.add(nuevo_deposito)
    db.commit()
    db.refresh(nuevo_deposito)
    return nuevo_deposito

# ------------------- Obtener depósito por ID -------------------
def obtener_deposito(db: Session, deposito_id: int):
    return db.query(Deposito).filter(Deposito.id == deposito_id).first()

# ------------------- Listar todos los depósitos -------------------
def listar_depositos(db: Session):
    return db.query(Deposito).all()

# ------------------- Actualizar depósito -------------------
def actualizar_deposito(
    db: Session, 
    deposito_id: int, 
    nombre: str = None, 
    ubicacion: str = None
):
    deposito = db.query(Deposito).filter(Deposito.id == deposito_id).first()
    if not deposito:
        return None
    
    if nombre is not None:
        deposito.nombre = nombre
    if ubicacion is not None:
        deposito.ubicacion = ubicacion

    db.commit()
    db.refresh(deposito)
    return deposito

# ------------------- Eliminar depósito -------------------
def eliminar_deposito(db: Session, deposito_id: int):
    deposito = db.query(Deposito).filter(Deposito.id == deposito_id).first()
    if not deposito:
        return None

    # ⚠️ Revisar si hay movimientos asociados antes de eliminar
    if deposito.movimientos:  # Suponiendo que la relación ORM es: movimientos = relationship("MovimientoORM", back_populates="deposito")
        raise Exception("No se puede eliminar el depósito porque tiene movimientos asociados.")

    db.delete(deposito)
    db.commit()
    return deposito
