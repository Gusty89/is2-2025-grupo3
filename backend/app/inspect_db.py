# inspect_db.py
from sqlalchemy import inspect
from db.engine import engine  # tu engine que apunta a StockDB.db

# Crear el inspector
inspector = inspect(engine)

# Listar todas las tablas
tablas = inspector.get_table_names()
print("Tablas en la base de datos:")
for tabla in tablas:
    print(f"- {tabla}")

# Listar columnas de cada tabla
for tabla in tablas:
    print(f"\nColumnas en {tabla}:")
    for columna in inspector.get_columns(tabla):
        print(f"  {columna['name']} ({columna['type']})")