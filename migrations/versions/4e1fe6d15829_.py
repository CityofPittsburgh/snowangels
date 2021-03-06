"""empty message

Revision ID: 4e1fe6d15829
Revises: 286163916881
Create Date: 2015-09-23 20:30:20.671665

"""

# revision identifiers, used by Alembic.
revision = '4e1fe6d15829'
down_revision = '286163916881'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('address', sa.String(length=64), nullable=True))
    op.create_index('ix_users_address', 'users', ['address'], unique=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_users_address', 'users')
    op.drop_column('users', 'address')
    ### end Alembic commands ###
