"""empty message

Revision ID: 4144fc0ac99
Revises: None
Create Date: 2015-05-27 18:15:11.967868

"""

# revision identifiers, used by Alembic.
revision = '4144fc0ac99'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('words',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('word', sa.String(length=32), nullable=True),
    sa.Column('english', sa.String(length=256), nullable=True),
    sa.Column('count', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('words')
    ### end Alembic commands ###
