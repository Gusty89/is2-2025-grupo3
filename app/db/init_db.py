from app.db.base import Base
from app.db.session import engine
from sqlalchemy.orm import Session # type: ignore
from app.db.session import SessionLocal # type: ignore

def init_db():
    print("Creando las tablas en la base de datos...")
    Base.metadata.create_all(bind=engine)
    print("Tablas creadas con éxito.")

if __name__ == "__main__":
    init_db()


# app/console/script.py

from app.db.session import SessionLocal

# Importa solo el modelo ProductoORM
from app.db.models.producto import ProductoORM

# Importa solo el modelo UsuarioORM
from app.db.models.usuario import UsuarioORM

# Importa solo el modelo DepositoORM
from app.db.models.deposito import DepositoORM

# Importa solo el modelo MovimientoORM y el enum TipoMovimiento
from app.db.models.movimiento import MovimientoORM, TipoMovimiento as TipoMovimientoEnum

# Importa solo el modelo RolORM
from app.db.models.rol import RolORM

# Importa solo el modelo UsuarioRolORM
from app.db.models.usuarioRol import UsuarioRolORM


# 5. Insertar datos

# Función para insertar un producto de prueba
def insertarProducto():
    db = SessionLocal()
    try:
        print("Iniciando inserción de producto de prueba...")
        
        nuevo_producto = ProductoORM(
            nombre="Producto Ejemplo", 
            sku="0001", 
            descripcion="Test", 
            stock=10, 
            stock_minimo=2
        )
        
        db.add(nuevo_producto)
        db.commit()
        db.refresh(nuevo_producto)
        
        print(f"Producto '{nuevo_producto.nombre}' insertado con ID: {nuevo_producto.id}")
        
    except Exception as e:
        db.rollback()
        print(f"Ocurrió un error: {e}")
    finally:
        db.close()

# Función para insertar un usuario de prueba
def insertarUsuario():
    db = SessionLocal()
    try:
        print("Iniciando inserción de usuario de prueba...")
        
        # Crea una nueva instancia de la clase Usuario
        nuevo_usuario = UsuarioORM(
            username="nuevo_usuario", 
            email="nuevo_usuario@ejemplo.com", 
            hashed_password="contraseña_cifrada_aqui",  # Utiliza un hash real en producción
            is_active=True
        )
        
        # Agrega el objeto a la sesión
        db.add(nuevo_usuario)
        
        # Confirma la transacción
        db.commit()
        
        # Actualiza el objeto para obtener el ID generado por la base de datos
        db.refresh(nuevo_usuario)
        
        print(f"Usuario '{nuevo_usuario.username}' insertado con ID: {nuevo_usuario.id}")
        
    except Exception as e:
        db.rollback()
        print(f"Ocurrió un error: {e}")
    finally:
        db.close()

# Función para insertar un depósito de prueba
def insertarDeposito():
    db = SessionLocal()
    try:
        print("Iniciando inserción de depósito de prueba...")
        
        # Crea una nueva instancia de la clase Deposito
        nuevo_deposito = DepositoORM(
            nombre="Depósito Central", 
            ubicacion="Avenida Principal 123"
        )
        
        # Agrega el objeto a la sesión
        db.add(nuevo_deposito)
        
        # Confirma la transacción
        db.commit()
        
        # Actualiza el objeto para obtener el ID generado por la base de datos
        db.refresh(nuevo_deposito)
        
        print(f"Depósito '{nuevo_deposito.nombre}' insertado con ID: {nuevo_deposito.id}")
        
    except Exception as e:
        db.rollback()
        print(f"Ocurrió un error: {e}")
    finally:
        db.close()

# Función para insertar un movimiento de prueba
def insertarMovimiento():
    db = SessionLocal()
    try:
        print("Iniciando inserción de movimiento de prueba...")
        
        # Primero, asegúrate de que existen los IDs a los que harás referencia
        # (producto, depósitos y usuario)
        producto_ejemplo = db.query(ProductoORM).filter(ProductoORM.id == 1).first()
        deposito_origen_ejemplo = db.query(DepositoORM.movimientos_origen).filter(DepositoORM.id == 1).first()
        deposito_destino_ejemplo = db.query(DepositoORM.movimientos_destino).filter(DepositoORM.id == 2).first()
        usuario_ejemplo = db.query(UsuarioORM).filter(UsuarioORM.id == 1).first()

        if not all([producto_ejemplo, deposito_origen_ejemplo, deposito_destino_ejemplo, usuario_ejemplo]):
            print("Error: Asegúrate de que los IDs referenciados existen en sus respectivas tablas.")
            return

        # Crea una nueva instancia de la clase Movimiento
        nuevo_movimiento = MovimientoORM(
            producto_id=producto_ejemplo.id,
            deposito_origen_id=deposito_origen_ejemplo.id,
            deposito_destino_id=deposito_destino_ejemplo.id,
            usuario_id=usuario_ejemplo.id,
            cantidad=5,
            tipo=TipoMovimientoEnum.TRANSFERENCIA
        )
        
        # Agrega el objeto a la sesión
        db.add(nuevo_movimiento)
        
        # Confirma la transacción
        db.commit()
        
        # Actualiza el objeto para obtener el ID generado
        db.refresh(nuevo_movimiento)
        
        print(f"Movimiento con ID {nuevo_movimiento.id} insertado exitosamente.")
        
    except Exception as e:
        db.rollback()
        print(f"Ocurrió un error: {e}")
    finally:
        db.close()

# Función para asignar un rol a un usuario existente
def asignarRolAUsuario():
    db = SessionLocal()
    try:
        print("Iniciando asignación de rol a usuario...")
        
        # 1. Obtener el usuario y el rol existentes de la base de datos
        usuario_a_actualizar = db.query(UsuarioRolORM).filter(UsuarioRolORM.id == 1).first()
        rol_a_asignar = db.query(RolORM).filter(RolORM.id == 1).first()

        if not usuario_a_actualizar or not rol_a_asignar:
            print("Error: Asegúrate de que el usuario y el rol con esos IDs existen.")
            return

        # 2. Asignar el rol al usuario
        # SQLAlchemy gestiona la inserción en la tabla de asociación automáticamente.
        usuario_a_actualizar.roles.append(rol_a_asignar)
        
        # 3. Confirmar la transacción
        db.commit()
        
        print(f"Rol '{rol_a_asignar.nombre}' asignado al usuario '{usuario_a_actualizar.username}' exitosamente.")
        
    except Exception as e:
        db.rollback()
        print(f"Ocurrió un error: {e}")
    finally:
        db.close()


# Función para insertar un rol de prueba
def insertarRol():
    db = SessionLocal()
    try:
        print("Iniciando inserción de rol de prueba...")
        
        # Crea una nueva instancia de la clase Rol
        nuevo_rol = RolORM(
            nombre="Administrador"
        )
        
        # Agrega el objeto a la sesión
        db.add(nuevo_rol)
        
        # Confirma la transacción
        db.commit()
        
        # Actualiza el objeto para obtener el ID generado por la base de datos
        db.refresh(nuevo_rol)
        
        print(f"Rol '{nuevo_rol.nombre}' insertado con ID: {nuevo_rol.id}")
        
    except Exception as e:
        db.rollback()
        print(f"Ocurrió un error: {e}")
    finally:
        db.close()

# Este bloque asegura que la función solo se ejecute cuando el archivo se corra directamente
if __name__ == "__main__":
    insertarProducto()
    insertarUsuario()
    insertarDeposito()
    insertarMovimiento()
    asignarRolAUsuario()
    insertarRol()
