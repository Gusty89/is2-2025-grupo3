from sqlalchemy.orm import Session # type: ignore
from app.db.base import Base # type: ignore
from app.db.session import engine, SessionLocal # type: ignore

# Importar todos los modelos para que se registren en Base.metadata
from app.db.models.UsuarioORM import UsuarioORM
from app.db.models.rol import RolORM
from app.db.models.producto import ProductoORM
from app.db.models.deposito import DepositoORM
from app.db.models.movimiento import MovimientoORM, TipoMovimiento as TipoMovimientoEnum

# NOTA: No es necesario importar UsuarioRolORM aquí,
# ya que SQLAlchemy gestiona la tabla de asociación.

def init_db():
    print("Creando las tablas en la base de datos...")
    Base.metadata.create_all(bind=engine)
    print("Tablas creadas con éxito.")

# ----------------- Funciones de Inserción de Datos -----------------

def insertar_datos_iniciales():
    db: Session = SessionLocal()
    try:
        print("\n--- Iniciando inserción de datos iniciales ---")

        # 1. Insertar un Rol de prueba (necesario para la relación con el usuario)
        nuevo_rol = RolORM(nombre="Administrador")
        db.add(nuevo_rol)
        db.commit()
        db.refresh(nuevo_rol)
        print(f"✅ Rol '{nuevo_rol.nombre}' insertado.")

        # 2. Insertar un Usuario de prueba
        nuevo_usuario = UsuarioORM(
            username="nuevo_usuario",
            email="nuevo_usuario@ejemplo.com",
            hashed_password="contraseña_cifrada_aqui",
            is_active=True
        )
        db.add(nuevo_usuario)
        db.commit()
        db.refresh(nuevo_usuario)
        print(f"✅ Usuario '{nuevo_usuario.username}' insertado.")

        # 3. Asignar el Rol al Usuario (establecer la relación muchos a muchos)
        nuevo_usuario.roles.append(nuevo_rol)
        db.commit()
        print(f"✅ Rol '{nuevo_rol.nombre}' asignado a '{nuevo_usuario.username}'.")

        # 4. Insertar un Producto y dos Depósitos
        nuevo_producto = ProductoORM(nombre="Producto Ejemplo", sku="0001", descripcion="Test", stock=10, stock_minimo=2)
        deposito_origen = DepositoORM(nombre="Depósito Principal", ubicacion="Ubicación 1")
        deposito_destino = DepositoORM(nombre="Depósito Secundario", ubicacion="Ubicación 2")

        db.add_all([nuevo_producto, deposito_origen, deposito_destino])
        db.commit()
        db.refresh(nuevo_producto)
        db.refresh(deposito_origen)
        db.refresh(deposito_destino)
        print(f"✅ Producto '{nuevo_producto.nombre}' y depósitos insertados.")

        # 5. Insertar un Movimiento (ahora que los objetos existen)
        nuevo_movimiento = MovimientoORM(
            producto_id=nuevo_producto.id,
            deposito_origen_id=deposito_origen.id,
            deposito_destino_id=deposito_destino.id,
            usuario_id=nuevo_usuario.id,
            cantidad=25,
            tipo=TipoMovimientoEnum.TRANSFERENCIA
        )
        db.add(nuevo_movimiento)
        db.commit()
        db.refresh(nuevo_movimiento)
        print(f"✅ Movimiento con ID {nuevo_movimiento.id} insertado exitosamente.")

        print("\n--- Inserción de todos los datos de prueba completada ---")
    
    except Exception as e:
        db.rollback()
        print(f"\n❌ Ocurrió un error en la transacción: {e}")
    finally:
        db.close()

# ----------------- Punto de Entrada del Script -----------------

if __name__ == "__main__":
    init_db()  # Primero, asegúrate de que las tablas existen
    insertar_datos_iniciales() # Luego, inserta los datos en el orden correcto