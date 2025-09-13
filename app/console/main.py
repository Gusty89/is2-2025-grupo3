
from app.db.session import SessionLocal
from app.console.crud_producto import crear_producto, listar_productos, obtener_producto, actualizar_producto, eliminar_producto
from app.console.crud_deposito import crear_deposito, listar_depositos, obtener_deposito, actualizar_deposito, eliminar_deposito
from app.console.crud_usuario import crear_usuario, listar_usuarios, obtener_usuario, actualizar_usuario, eliminar_usuario
from app.console.crud_rol import crear_rol, listar_roles, obtener_rol, actualizar_rol, eliminar_rol
from app.console.crud_movimiento import crear_movimiento, listar_movimientos, obtener_movimiento, actualizar_movimiento, eliminar_movimiento
from app.db.models.base import Base
from app.db.engine import engine
from app.db.models import ProductoORM, MovimientoORM, DepositoORM, UsuarioORM, RolORM

db = SessionLocal()

# Crear tablas
Base.metadata.create_all(bind=engine)



# ------------------- Submenú CRUD Producto -------------------
def submenu_productos():
    while True:
        print("\n--- CRUD Productos ---")
        print("1. Crear producto")
        print("2. Listar productos")
        print("3. Buscar producto por ID")
        print("4. Actualizar producto")
        print("5. Eliminar producto")
        print("6. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            descripcion = input("Descripción: ") or None
            sku = input("SKU (Enter para generar automáticamente): ")
            if not sku:
                sku = nombre.lower().replace(" ", "-")
            stock = int(input("Stock: "))
            stock_minimo = input("Stock mínimo (default 0): ")
            stock_minimo = int(stock_minimo) if stock_minimo else 0
            producto = crear_producto(db, nombre, descripcion, sku, stock, stock_minimo)
            print(f"Producto creado: {producto.__dict__}")

        elif opcion == "2":
            productos = listar_productos(db)
            for p in productos:
                print(p.__dict__)

        elif opcion == "3":
            producto_id = int(input("ID del producto: "))
            producto = obtener_producto(db, producto_id)
            print(producto.__dict__ if producto else "No encontrado")

        elif opcion == "4":
            producto_id = int(input("ID del producto a actualizar: "))
            nombre = input("Nombre (Enter para omitir): ") or None
            descripcion = input("Descripción (Enter para omitir): ") or None
            sku = input("SKU (Enter para omitir): ") or None
            stock = input("Stock (Enter para omitir): ")
            stock = int(stock) if stock else None
            stock_minimo = input("Stock mínimo (Enter para omitir): ")
            stock_minimo = int(stock_minimo) if stock_minimo else None
            producto = actualizar_producto(db, producto_id, nombre, descripcion, sku, stock, stock_minimo)
            print(producto.__dict__ if producto else "No encontrado")

        elif opcion == "5":
            producto_id = int(input("ID del producto a eliminar: "))
            producto = eliminar_producto(db, producto_id)
            print(f"Producto eliminado: {producto}" if producto else "No encontrado")

        elif opcion == "6":
            break

        else:
            print("Opción inválida")


# ------------------- Submenú CRUD Depósito -------------------
def submenu_depositos():
    while True:
        print("\n--- CRUD Depósitos ---")
        print("1. Crear depósito")
        print("2. Listar depósitos")
        print("3. Buscar depósito por ID")
        print("4. Actualizar depósito")
        print("5. Eliminar depósito")
        print("6. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            ubicacion = input("Ubicación: ")
            deposito = crear_deposito(db, nombre, ubicacion)
            print(f"Depósito creado: {deposito.__dict__}")

        elif opcion == "2":
            depositos = listar_depositos(db)
            for d in depositos:
                print(d.__dict__)

        elif opcion == "3":
            deposito_id = int(input("ID del depósito: "))
            deposito = obtener_deposito(db, deposito_id)
            print(deposito.__dict__ if deposito else "No encontrado")

        elif opcion == "4":
            deposito_id = int(input("ID del depósito a actualizar: "))
            nombre = input("Nombre (Enter para omitir): ") or None
            ubicacion = input("Ubicación (Enter para omitir): ") or None
            deposito = actualizar_deposito(db, deposito_id, nombre, ubicacion)
            print(deposito.__dict__ if deposito else "No encontrado")

        elif opcion == "5":
            deposito_id = int(input("ID del depósito a eliminar: "))
            try:
                deposito = eliminar_deposito(db, deposito_id)
                print(f"Depósito eliminado: {deposito}" if deposito else "No encontrado")
            except Exception as e:
                print(f"Error: {e}")

        elif opcion == "6":
            break

        else:
            print("Opción inválida")

# ------------------- Submenú CRUD Usuario -------------------
def submenu_usuarios():
    while True:
        print("\n--- CRUD Usuarios ---")
        print("1. Crear usuario")
        print("2. Listar usuarios")
        print("3. Buscar usuario por ID")
        print("4. Actualizar usuario")
        print("5. Eliminar usuario")
        print("6. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            username = input("Username: ")
            email = input("Email: ")
            hashed_password = input("Hashed password: ")
            is_active = input("Activo (True/False, default True): ") or "True"
            is_active = True if is_active.lower() == "true" else False
            usuario = crear_usuario(db, username, email, hashed_password, is_active)
            print(f"Usuario creado: {usuario.__dict__}")

        elif opcion == "2":
            usuarios = listar_usuarios(db)
            for u in usuarios:
                print(u.__dict__)

        elif opcion == "3":
            usuario_id = int(input("ID del usuario: "))
            usuario = obtener_usuario(db, usuario_id)
            print(usuario.__dict__ if usuario else "No encontrado")

        elif opcion == "4":
            usuario_id = int(input("ID del usuario a actualizar: "))
            username = input("Username (Enter para omitir): ") or None
            email = input("Email (Enter para omitir): ") or None
            hashed_password = input("Hashed password (Enter para omitir): ") or None
            is_active = input("Activo (True/False, Enter para omitir): ") or None
            if is_active is not None:
                is_active = True if is_active.lower() == "true" else False
            usuario = actualizar_usuario(db, usuario_id, username, email, hashed_password, is_active)
            print(usuario.__dict__ if usuario else "No encontrado")

        elif opcion == "5":
            usuario_id = int(input("ID del usuario a eliminar: "))
            usuario = eliminar_usuario(db, usuario_id)
            print(f"Usuario eliminado: {usuario}" if usuario else "No encontrado")

        elif opcion == "6":
            break

        else:
            print("Opción inválida")


# ------------------- Submenú CRUD Rol -------------------
def submenu_roles():
    while True:
        print("\n--- CRUD Roles ---")
        print("1. Crear rol")
        print("2. Listar roles")
        print("3. Buscar rol por ID")
        print("4. Actualizar rol")
        print("5. Eliminar rol")
        print("6. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre del rol: ")
            rol = crear_rol(db, nombre)
            print(f"Rol creado: {rol.__dict__}")

        elif opcion == "2":
            roles = listar_roles(db)
            for r in roles:
                print(r.__dict__)

        elif opcion == "3":
            rol_id = int(input("ID del rol: "))
            rol = obtener_rol(db, rol_id)
            print(rol.__dict__ if rol else "No encontrado")

        elif opcion == "4":
            rol_id = int(input("ID del rol a actualizar: "))
            nombre = input("Nombre (Enter para omitir): ") or None
            rol = actualizar_rol(db, rol_id, nombre)
            print(rol.__dict__ if rol else "No encontrado")

        elif opcion == "5":
            rol_id = int(input("ID del rol a eliminar: "))
            rol = eliminar_rol(db, rol_id)
            print(f"Rol eliminado: {rol}" if rol else "No encontrado")

        elif opcion == "6":
            break

        else:
            print("Opción inválida")


# ------------------- Submenú CRUD Movimiento -------------------
def submenu_movimientos():
    while True:
        print("\n--- CRUD Movimientos ---")
        print("1. Crear movimiento")
        print("2. Listar movimientos")
        print("3. Buscar movimiento por ID")
        print("4. Actualizar movimiento")
        print("5. Eliminar movimiento")
        print("6. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            tipo = input("Tipo (ENTRADA/SALIDA/TRANSFERENCIA): ")
            cantidad = int(input("Cantidad: "))
            usuario_id = int(input("ID del usuario: "))
            deposito_id = int(input("ID del depósito: "))
            movimiento = crear_movimiento(db, tipo, cantidad, usuario_id, deposito_id)
            print(f"Movimiento creado: {movimiento.__dict__}")

        elif opcion == "2":
            movimientos = listar_movimientos(db)
            for m in movimientos:
                print(m.__dict__)

        elif opcion == "3":
            movimiento_id = int(input("ID del movimiento: "))
            movimiento = obtener_movimiento(db, movimiento_id)
            print(movimiento.__dict__ if movimiento else "No encontrado")

        elif opcion == "4":
            movimiento_id = int(input("ID del movimiento a actualizar: "))
            tipo = input("Tipo (Enter para omitir): ") or None
            cantidad = input("Cantidad (Enter para omitir): ")
            cantidad = int(cantidad) if cantidad else None
            usuario_id = input("ID usuario (Enter para omitir): ")
            usuario_id = int(usuario_id) if usuario_id else None
            deposito_id = input("ID depósito (Enter para omitir): ")
            deposito_id = int(deposito_id) if deposito_id else None
            movimiento = actualizar_movimiento(db, movimiento_id, tipo, cantidad, usuario_id, deposito_id)
            print(movimiento.__dict__ if movimiento else "No encontrado")

        elif opcion == "5":
            movimiento_id = int(input("ID del movimiento a eliminar: "))
            movimiento = eliminar_movimiento(db, movimiento_id)
            print(f"Movimiento eliminado: {movimiento}" if movimiento else "No encontrado")

        elif opcion == "6":
            break

        else:
            print("Opción inválida")


# ------------------- Menú Principal -------------------
def menu():
    while True:
        print("\n=== Menú Principal ===")
        print("1. CRUD de Productos")
        print("2. CRUD de Depósitos")
        print("3. CRUD de Usuarios")
        print("4. CRUD de Roles")
        print("5. CRUD de Movimientos")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            submenu_productos()
        elif opcion == "2":
            submenu_depositos()
        elif opcion == "3":
            submenu_usuarios()
        elif opcion == "4":
            submenu_roles()
        elif opcion == "5":
            submenu_movimientos()
        elif opcion == "6":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida")


if __name__ == "__main__":
    menu()
