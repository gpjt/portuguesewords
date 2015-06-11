"""empty message

Revision ID: 4bfa26093bb
Revises: 4144fc0ac99
Create Date: 2015-06-11 17:13:53.671147

"""

# revision identifiers, used by Alembic.
revision = '4bfa26093bb'
down_revision = '4144fc0ac99'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('words', sa.Column('notes', sa.String(length=4096), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('words', 'notes')
    ### end Alembic commands ###
