"""create traitors table

Revision ID: 5336db8e851e
Revises: 3b658729058b
Create Date: 2024-01-30 17:11:14.742056

"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5336db8e851e'
down_revision: Union[str, None] = '3b658729058b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'traitors',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('first_name', sa.String),
        sa.Column('last_name', sa.String),
        sa.Column('rank', sa.String)
    )


def downgrade() -> None:
    op.drop_table('traitors')
