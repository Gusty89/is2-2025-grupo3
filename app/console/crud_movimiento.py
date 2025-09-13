from sqlalchemy.orm import Session
from app.db.models.movimiento import MovimientoORM as Movimiento

# ------------------- Crear movimiento -------------------
def crear_movimiento(db: Session, tipo: str, cantidad: int, usuario_id: int, deposito_id: int):
    nuevo_movimiento = Movimiento(
        tipo=tipo,
        cantidad=cantidad,
        usuario_id=usuario_id,
        deposito_id=deposito_id
    )
    db.add(nuevo_movimiento)
    db.commit()
    db.refresh(nuevo_movimiento)
    return nuevo_movimiento

# ------------------- Obtener movimiento por ID -------------------
def obtener_movimiento(db: Session, movimiento_id: int):
    return db.query(Movimiento).filter(Movimiento.id == movimiento_id).first()

# ------------------- Listar todos los movimientos -------------------
def listar_movimientos(db: Session):
    return db.query(Movimiento).all()

# ------------------- Actualizar movimiento -------------------
def actualizar_movimiento(
    db: Session,
    movimiento_id: int,
    tipo: str = None,
    cantidad: int = None,
    usuario_id: int = None,
    deposito_id: int = None
):
    movimiento = db.query(Movimiento).filter(Movimiento.id == movimiento_id).first()
    if not movimiento:
        return None

    if tipo is not None:
        movimiento.tipo = tipo
    if cantidad is not None:
        movimiento.cantidad = cantidad
    if usuario_id is not None:
        movimiento.usuario_id = usuario_id
    if deposito_id is not None:
        movimiento.deposito_id = deposito_id

    db.commit()
    db.refresh(movimiento)
    return movimiento

# ------------------- Eliminar movimiento -------------------
def eliminar_movimiento(db: Session, movimiento_id: int):
    movimiento = db.query(Movimiento).filter(Movimiento.id == movimiento_id).first()
    if not movimiento:
        return None

    db.delete(movimiento)
    db.commit()
    return movimiento
