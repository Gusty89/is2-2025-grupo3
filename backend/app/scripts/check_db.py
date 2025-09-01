from app.db.session import engine
from sqlalchemy import inspect

inspector = inspect(engine)
print("Tablas existentes en la base de datos:")
print(inspector.get_table_names())
