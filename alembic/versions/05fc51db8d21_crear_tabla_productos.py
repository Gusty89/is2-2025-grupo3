"""crear tabla productos

Revision ID: 05fc51db8d21
Revises: 2b34ecfd7a80
Create Date: 2025-08-30 02:21:37.082804

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '05fc51db8d21'
down_revision: Union[str, None] = '2b34ecfd7a80'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
