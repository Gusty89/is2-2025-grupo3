from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.engine import engine
from app.db.session import sessionmaker
from app.schemas.producto import Producto, ProductoCreate, ProductoUpdate
from app.schemas.deposito import Deposito, DepositoCreate, DepositoUpdate
from app.schemas.movimiento import Movimiento, MovimientoCreate, MovimientoUpdate
from app.schemas.rol import Rol, RolCreate, RolUpdate
from app.schemas.usuario import Usuario, UsuarioCreate, UsuarioUpdate
from app.db.models.producto import ProductoORM
from app.db.models.movimiento import MovimientoORM
from app.db.models.deposito import DepositoORM
from app.db.models.rol import RolORM
from app.db.models.usuario import UsuarioORM

app = FastAPI()
SessionLocal = sessionmaker(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ENDPOINTS PRODUCTOS

@app.post("/productos/", response_model=Producto)
def crear_producto(producto: ProductoCreate, db: Session = Depends(get_db)):
    db_producto = ProductoORM(**producto.dict())
    db.add(db_producto)
    db.commit()
    db.refresh(db_producto)
    return db_producto

@app.get("/productos/", response_model=list[Producto])
def listar_productos(db: Session = Depends(get_db)):
    productos = db.query(ProductoORM).all()
    return productos

@app.put("/productos/{producto_id}", response_model=Producto)
def actualizar_producto(producto_id: int, producto: ProductoUpdate, db: Session = Depends(get_db)):
    db_producto = db.query(ProductoORM).get(producto_id)
    if not db_producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    for key, value in producto.dict(exclude_unset=True).items():
        setattr(db_producto, key, value)
    db.commit()
    db.refresh(db_producto)
    return db_producto

@app.delete("/productos/{producto_id}", response_model=Producto)
def eliminar_producto(producto_id: int, db: Session = Depends(get_db)):
    producto = db.query(ProductoORM).get(producto_id)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    db.delete(producto)
    db.commit()
    return producto

#ENDPOINTS DEPOSITO

@app.post("/depositos/", response_model=Deposito)
def crear_deposito(deposito: DepositoCreate, db: Session = Depends(get_db)):
    db_deposito = DepositoORM(**deposito.dict())
    db.add(db_deposito)
    db.commit()
    db.refresh(db_deposito)
    return db_deposito

@app.get("/depositos/", response_model=list[Deposito])
def listar_depositos(db: Session = Depends(get_db)):
    depositos = db.query(DepositoORM).all()
    return depositos

@app.put("/depositos/{deposito_id}", response_model=Deposito)
def actualizar_deposito(deposito_id: int, deposito: DepositoUpdate, db: Session = Depends(get_db)):
    db_deposito = db.query(DepositoORM).get(deposito_id)
    if not db_deposito:
        raise HTTPException(status_code=404, detail="Deposito no encontrado")
    for key, value in deposito.dict(exclude_unset=True).items():
        setattr(db_deposito, key, value)
    db.commit()
    db.refresh(db_deposito)
    return db_deposito

@app.delete("/depositos/{deposito_id}", response_model=Deposito)
def eliminar_deposito(deposito_id: int, db: Session = Depends(get_db)):
    deposito = db.query(DepositoORM).get(deposito_id)
    if not deposito:
        raise HTTPException(status_code=404, detail="Depósito no encontrado")
    db.delete(deposito)
    db.commit()
    return deposito

#ENDPOINTS MOVIMIENTO 

@app.post("/movimientos/", response_model=Movimiento)
def crear_movimiento(movimiento: MovimientoCreate, db: Session = Depends(get_db)):
    db_movimiento = MovimientoORM(**movimiento.dict())
    db.add(db_movimiento)
    db.commit()
    db.refresh(db_movimiento)
    return db_movimiento

@app.get("/movimientos/", response_model=list[Movimiento])
def listar_movimientos(db: Session = Depends(get_db)):
    movimientos = db.query(MovimientoORM).all()
    return movimientos

@app.put("/movimientos/{movimiento_id}", response_model=Movimiento)
def actualizar_movimiento(movimiento_id: int, movimiento: MovimientoUpdate, db: Session = Depends(get_db)):
    db_movimiento = db.query(MovimientoORM).get(movimiento_id)
    if not db_movimiento:
        raise HTTPException(status_code=404, detail="Movimiento no encontrado")
    for key, value in movimiento.dict(exclude_unset=True).items():
        setattr(db_movimiento, key, value)
    db.commit()
    db.refresh(db_movimiento)
    return db_movimiento

@app.delete("/movimientos/{movimiento_id}", response_model=Movimiento)
def eliminar_movimiento(movimiento_id: int, db: Session = Depends(get_db)):
    movimiento = db.query(MovimientoORM).get(movimiento_id)
    if not movimiento:
        raise HTTPException(status_code=404, detail="Movimiento no encontrado")
    db.delete(movimiento)
    db.commit()
    return movimiento

#ENDPOINTS ROL

@app.post("/roles/", response_model=Rol)
def crear_rol(rol: RolCreate, db: Session = Depends(get_db)):
    db_rol = RolORM(**rol.dict())
    db.add(db_rol)
    db.commit()
    db.refresh(db_rol)
    return db_rol

@app.get("/roles/", response_model=list[Rol])
def listar_roles(db: Session = Depends(get_db)):
    roles = db.query(RolORM).all()
    return roles

@app.put("/roles/{rol_id}", response_model=Rol)
def actualizar_rol(rol_id: int, rol: RolUpdate, db: Session = Depends(get_db)):
    db_rol = db.query(RolORM).get(rol_id)
    if not db_rol:
        raise HTTPException(status_code=404, detail="Rol no encontrado")
    for key, value in rol.dict(exclude_unset=True).items():
        setattr(db_rol, key, value)
    db.commit()
    db.refresh(db_rol)
    return db_rol

@app.delete("/roles/{rol_id}", response_model=Rol)
def eliminar_rol(rol_id: int, db: Session = Depends(get_db)):
    rol = db.query(RolORM).get(rol_id)
    if not rol:
        raise HTTPException(status_code=404, detail="Rol no encontrado")
    db.delete(rol)
    db.commit()
    return rol

#ENDPOINTS USUARIO

@app.post("/usuarios/", response_model=Usuario)
def crear_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    db_usuario = UsuarioORM(**usuario.dict())
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

@app.get("/usuarios/", response_model=list[Usuario])
def listar_usuarios(db: Session = Depends(get_db)):
    usuarios = db.query(UsuarioORM).all()
    return usuarios

@app.put("/usuarios/{usuario_id}", response_model=Usuario)
def actualizar_usuario(usuario_id: int, usuario: UsuarioUpdate, db: Session = Depends(get_db)):
    db_usuario = db.query(UsuarioORM).get(usuario_id)
    if not db_usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    for key, value in usuario.dict(exclude_unset=True).items():
        setattr(db_usuario, key, value)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

@app.delete("/usuarios/{usuario_id}", response_model=Usuario)
def eliminar_usuario(usuario_id: int, db: Session = Depends(get_db)):
    usuario = db.query(UsuarioORM).get(usuario_id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    db.delete(usuario)
    db.commit()
    return usuario


