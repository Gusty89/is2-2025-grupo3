import sys
import pathlib
from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context

# -------------------------------------------------------
# Hacer que Python encuentre la carpeta app/
sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))
# -------------------------------------------------------

# Importar Base y modelos ORM para que Alembic los detecte
from app.db.base import Base
from app.db.models import producto  # importa ProductoORM
# NOTA: No hace falta importar app.domain.producto (data class) porque no afecta las tablas

# Alembic Config object
config = context.config
fileConfig(config.config_file_name)

# Metadata objetivo para autogenerate
target_metadata = Base.metadata

# -------------------------------------------------------
# Funciones de upgrade / downgrade de Alembic
# -------------------------------------------------------

def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()


# -------------------------------------------------------
# Ejecutar modo offline u online según sea necesario
# -------------------------------------------------------
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
