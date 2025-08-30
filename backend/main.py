from app.db.session import SessionLocal
from app.db.crud_producto import crear_producto, listar_productos, obtener_producto, actualizar_producto, eliminar_producto

db = SessionLocal()

def menu():
    while True:
        print("\n--- CRUD Productos ---")
        print("1. Crear producto")
        print("2. Listar productos")
        print("3. Buscar producto por ID")
        print("4. Actualizar producto")
        print("5. Eliminar producto")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            descripcion = input("Descripción: ") or None
            sku = input("SKU (Enter para generar automáticamente): ")
            if not sku:
                sku = nombre.lower().replace(" ", "-")  # Genera SKU si no se ingresa
            stock = int(input("Stock: "))
            stock_minimo = int(input("Stock mínimo: (default 0) "))
            stock_minimo = int(stock_minimo) if stock_minimo else 0
            producto = crear_producto(db, nombre, descripcion, sku, stock, stock_minimo)
            print(f"Producto creado: {producto}")

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
            stock_minimo = input("Stock Minimo (Enter para omitir): ")
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

if __name__ == "__main__":
    menu()
