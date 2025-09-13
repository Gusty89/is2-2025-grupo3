from sqlalchemy.orm import Session
from app.db.models.usuario import UsuarioORM as Usuario

# ------------------- Crear usuario -------------------
def crear_usuario(db: Session, username: str, email: str, hashed_password: str, is_active: bool = True):
    nuevo_usuario = Usuario(
        username=username,
        email=email,
        hashed_password=hashed_password,
        is_active=is_active
    )
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    return nuevo_usuario

# ------------------- Obtener usuario por ID -------------------
def obtener_usuario(db: Session, usuario_id: int):
    return db.query(Usuario).filter(Usuario.id == usuario_id).first()

# ------------------- Listar todos los usuarios -------------------
def listar_usuarios(db: Session):
    return db.query(Usuario).all()

# ------------------- Actualizar usuario -------------------
def actualizar_usuario(
    db: Session, 
    usuario_id: int, 
    username: str = None, 
    email: str = None, 
    hashed_password: str = None,
    is_active: bool = None
):
    usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if not usuario:
        return None
    
    if username is not None:
        usuario.username = username
    if email is not None:
        usuario.email = email
    if hashed_password is not None:
        usuario.hashed_password = hashed_password
    if is_active is not None:
        usuario.is_active = is_active

    db.commit()
    db.refresh(usuario)
    return usuario

# ------------------- Eliminar usuario -------------------
def eliminar_usuario(db: Session, usuario_id: int):
    usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if not usuario:
        return None

    db.delete(usuario)
    db.commit()
    return usuario
