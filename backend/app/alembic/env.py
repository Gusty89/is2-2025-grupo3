from logging.config import fileConfig
import sys
import os

from sqlalchemy import pool
from alembic import context

# Agregar ruta para importar app/db
sys.path.append(os.path.join(os.path.dirname(__file__), '../app'))

# Importar Base y engine de tu proyecto
from db.base import Base
from db.engine import engine

# Configuración Alembic
config = context.config

# Configuración del logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Metadata de tus modelos para autogenerar migraciones
target_metadata = Base.metadata


def run_migrations_offline() -> None:
    """Ejecuta migraciones en modo offline (solo genera SQL)."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Ejecuta migraciones en modo online (aplica cambios directo en la DB)."""
    connectable = engine  # Usamos el engine de app/db/engine.py que apunta a StockDB.db

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()


# Ejecutar según el modo
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()