"""updating dog_owners table again

Revision ID: 49e62994b49f
Revises: 0164580b3a31
Create Date: 2024-01-11 15:31:02.090506

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '49e62994b49f'
down_revision: Union[str, None] = '0164580b3a31'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('dog_owners', 'name')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('dog_owners', sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
