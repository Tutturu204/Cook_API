"""empty message

Revision ID: 6392a57c1f0e
Revises: d23bba63a8cf
Create Date: 2021-09-08 18:39:46.608699

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6392a57c1f0e'
down_revision = 'd23bba63a8cf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'bio')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('bio', sa.VARCHAR(length=10), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
