"""add a column

Revision ID: 20bd64b7a2f3
Revises: 5336db8e851e
Create Date: 2024-01-30 17:32:24.373772

"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '20bd64b7a2f3'
down_revision: Union[str, None] = '5336db8e851e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('spaceships', sa.Column('speed', sa.Float))


def downgrade() -> None:
    op.drop_column('spaceships', 'speed')
