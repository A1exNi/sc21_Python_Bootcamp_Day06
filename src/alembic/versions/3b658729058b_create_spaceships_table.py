"""create spaceships table

Revision ID: 3b658729058b
Revises: 
Create Date: 2024-01-29 11:59:48.724585

"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3b658729058b'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'spaceships',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('alignment', sa.Integer),
        sa.Column('name', sa.String),
        sa.Column('ship_class', sa.Integer),
        sa.Column('length', sa.Float),
        sa.Column('crew_size', sa.Integer),
        sa.Column('armed', sa.Boolean),
    )
    op.create_table(
        'officers',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('first_name', sa.String),
        sa.Column('last_name', sa.String),
        sa.Column('rank', sa.String),
        sa.Column('spaceship_id', sa.Integer, sa.ForeignKey('spaceships.id')),
    )


def downgrade() -> None:
    op.drop_table('officers')
    op.drop_table('spaceships')
