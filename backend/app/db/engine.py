from sqlalchemy import create_engine
import os

# BASE_DIR apunta a app/db/
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "StockDB.db")  # Tu base dentro de db/

# Motor de SQLAlchemy
engine = create_engine(
    f"sqlite:///{DB_PATH}",
    connect_args={"check_same_thread": False}  # Necesario para SQLite
)