from app.db.session import SessionLocal
from app.db.crud_producto import (
    crear_producto,
    listar_productos,
    obtener_producto,
    actualizar_producto,
    eliminar_producto,
)
from app.db.crud_deposito import (
    crear_deposito,
    listar_depositos,
    obtener_deposito,
    actualizar_deposito,
    eliminar_deposito,
)
from app.db.base import Base
from app.db.engine import engine


# Crear tablas al inicio
Base.metadata.create_all(bind=engine)


def to_dict(obj):
    """Convierte un objeto ORM a dict sin _sa_instance_state"""
    if not obj:
        return None
    return {c.name: getattr(obj, c.name) for c in obj.__table__.columns}


def menu_productos():
    db = SessionLocal()
    try:
        while True:
            print("\n--- CRUD Productos ---")
            print("1. Crear producto")
            print("2. Listar productos")
            print("3. Buscar producto por ID")
            print("4. Actualizar producto")
            print("5. Eliminar producto")
            print("6. Volver")

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
                print(f"✅ Producto creado: {to_dict(producto)}")

            elif opcion == "2":
                productos = listar_productos(db)
                for p in productos:
                    print(to_dict(p))

            elif opcion == "3":
                producto_id = int(input("ID del producto: "))
                producto = obtener_producto(db, producto_id)
                print(to_dict(producto) if producto else "❌ No encontrado")

            elif opcion == "4":
                producto_id = int(input("ID del producto a actualizar: "))
                nombre = input("Nombre (Enter para omitir): ") or None
                descripcion = input("Descripción (Enter para omitir): ") or None
                sku = input("SKU (Enter para omitir): ") or None
                stock = input("Stock (Enter para omitir): ")
                stock = int(stock) if stock else None
                stock_minimo = input("Stock mínimo (Enter para omitir): ")
                stock_minimo = int(stock_minimo) if stock_minimo else None
                producto = actualizar_producto(
                    db, producto_id, nombre, descripcion, sku, stock, stock_minimo
                )
                print(to_dict(producto) if producto else "❌ No encontrado")

            elif opcion == "5":
                producto_id = int(input("ID del producto a eliminar: "))
                producto = eliminar_producto(db, producto_id)
                print(f"🗑️ Producto eliminado: {to_dict(producto)}" if producto else "❌ No encontrado")

            elif opcion == "6":
                break
            else:
                print("⚠️ Opción inválida")
    finally:
        db.close()


def menu_depositos():
    db = SessionLocal()
    try:
        while True:
            print("\n--- CRUD Depósitos ---")
            print("1. Crear depósito")
            print("2. Listar depósitos")
            print("3. Buscar depósito por ID")
            print("4. Actualizar depósito")
            print("5. Eliminar depósito")
            print("6. Volver")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                nombre = input("Nombre: ")
                ubicacion = input("Ubicación (opcional): ") or None
                deposito = crear_deposito(db, nombre, ubicacion)
                print(f"✅ Depósito creado: {to_dict(deposito)}")

            elif opcion == "2":
                depositos = listar_depositos(db)
                if not depositos:
                     print("📭 NO HAY NINGÚN DEPÓSITO LISTADO EN LA BASE DE DATOS.")
                else:
                    for d in depositos:
                         print(to_dict(d))

            elif opcion == "3":
                deposito_id = int(input("ID del depósito: "))
                deposito = obtener_deposito(db, deposito_id)
                print(to_dict(deposito) if deposito else "❌ No encontrado")

            elif opcion == "4":
                deposito_id = int(input("ID del depósito a actualizar: "))
                nombre = input("Nombre (Enter para omitir): ") or None
                ubicacion = input("Ubicación (Enter para omitir): ") or None
                deposito = actualizar_deposito(db, deposito_id, nombre, ubicacion)
                print(to_dict(deposito) if deposito else "❌ No encontrado")

            elif opcion == "5":
                deposito_id = int(input("ID del depósito a eliminar: "))
                deposito = eliminar_deposito(db, deposito_id)
                print(f"🗑️ Depósito eliminado: {to_dict(deposito)}" if deposito else "❌ No encontrado")

            elif opcion == "6":
                break
            else:
                print("⚠️ Opción inválida")
    finally:
        db.close()

def menu():
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. CRUD Productos")
        print("2. CRUD Depósitos")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_productos()
        elif opcion == "2":
            menu_depositos()
        elif opcion == "3":
            print("👋 Saliendo...")
            break
        else:
            print("⚠️ Opción inválida")


if __name__ == "__main__":
    menu()