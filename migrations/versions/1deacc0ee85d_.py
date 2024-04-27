"""empty message

Revision ID: 1deacc0ee85d
Revises: dcda19ad33d2
Create Date: 2024-04-08 20:15:45.727429

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1deacc0ee85d'
down_revision = 'dcda19ad33d2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('emails',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('captchar', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('emails')
    # ### end Alembic commands ###
