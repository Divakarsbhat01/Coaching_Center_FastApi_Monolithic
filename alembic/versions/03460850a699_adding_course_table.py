"""Adding Course Table

Revision ID: 03460850a699
Revises: 1888a1a5f33b
Create Date: 2024-02-10 09:36:59.518650

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '03460850a699'
down_revision: Union[str, None] = '1888a1a5f33b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Course',
    sa.Column('course_name', sa.String(length=50), nullable=False),
    sa.Column('course_id', sa.Integer(), nullable=False),
    sa.Column('course_desc', sa.String(length=100), nullable=False),
    sa.Column('course_credit', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('course_id'),
    sa.UniqueConstraint('course_name')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Course')
    # ### end Alembic commands ###
