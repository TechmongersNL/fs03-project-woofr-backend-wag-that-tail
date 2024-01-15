"""Create dogs

Revision ID: 22b7d6297afd
Revises: ae8de95a07a1
Create Date: 2024-01-15 15:08:53.562647

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '22b7d6297afd'
down_revision: Union[str, None] = 'ae8de95a07a1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('dogs',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('owner_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['owner_id'], ['dog_owners.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_dogs_id'), 'dogs', ['id'], unique=False)
    op.alter_column('dog_owners', 'username',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('dog_owners', 'about_me',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.add_column('woofs', sa.Column('description', sa.String(), nullable=True))
    op.add_column('woofs', sa.Column('image', sa.String(), nullable=True))
    op.add_column('woofs', sa.Column('dog_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'woofs', 'dogs', ['dog_id'], ['id'])
    op.drop_column('woofs', 'message')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('woofs', sa.Column('message', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'woofs', type_='foreignkey')
    op.drop_column('woofs', 'dog_id')
    op.drop_column('woofs', 'image')
    op.drop_column('woofs', 'description')
    op.alter_column('dog_owners', 'about_me',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('dog_owners', 'username',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.drop_index(op.f('ix_dogs_id'), table_name='dogs')
    op.drop_table('dogs')
    # ### end Alembic commands ###
