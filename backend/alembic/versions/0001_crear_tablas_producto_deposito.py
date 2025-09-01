"""crear tablas producto y deposito

Revision ID: 0001
Revises: 
Create Date: 2025-09-01 21:30:00.000000
"""
from alembic import op
import sqlalchemy as sa

# Identificadores de Alembic
revision = '0001'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'producto',
        sa.Column('id', sa.Integer, primary_key=True, index=True, autoincrement=True),
        sa.Column('nombre', sa.String(length=100), nullable=False),
        sa.Column('sku', sa.String(length=50), nullable=False, unique=True),
        sa.Column('descripcion', sa.String(length=255)),
        sa.Column('stock', sa.Integer, nullable=True, default=0),
        sa.Column('stock_minimo', sa.Integer, nullable=True, default=0),
    )

    op.create_table(
        'deposito',
        sa.Column('id', sa.Integer, primary_key=True, index=True, autoincrement=True),
        sa.Column('nombre', sa.String(length=100), nullable=False, unique=True),
        sa.Column('direccion', sa.String(length=255)),
        sa.Column('capacidad_maxima', sa.Integer, nullable=True, default=0),
    )


def downgrade():
    op.drop_table('producto')
    op.drop_table('deposito')