"""empty message

Revision ID: 9cfd590a2493
Revises: e68c563828e1
Create Date: 2020-07-05 00:56:59.720000

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '9cfd590a2493'
down_revision = 'e68c563828e1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tasks', sa.Column('update_ad', sa.DateTime(), nullable=True))
    op.drop_column('tasks', 'udate_ad')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tasks', sa.Column('udate_ad', mysql.DATETIME(), nullable=True))
    op.drop_column('tasks', 'update_ad')
    # ### end Alembic commands ###
