# app/db/base.py
from sqlalchemy.orm import declarative_base # type: ignore

Base = declarative_base()

# Importar los modelos para que Alembic los detecte
from app.db.models.usuario import UsuarioORM
from app.db.models.usuarioRol import UsuarioRolORM
from app.db.models.rol import RolORM
from app.db.models.producto import ProductoORM
from app.db.models.deposito import DepositoORM
from app.db.models.movimiento import MovimientoORM