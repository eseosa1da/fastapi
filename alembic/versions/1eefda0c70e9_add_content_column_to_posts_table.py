"""add content column to posts table

Revision ID: 1eefda0c70e9
Revises: 0933aff6d3b2
Create Date: 2024-10-03 22:30:09.855606

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1eefda0c70e9'
down_revision: Union[str, None] = '0933aff6d3b2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
