"""empty message

Revision ID: 47534ae8b34a
Revises: 4fd9cd69c7f3
Create Date: 2023-04-30 12:23:34.733741

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '47534ae8b34a'
down_revision = '4fd9cd69c7f3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('product', sa.Column('likes', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('product', 'likes')
    # ### end Alembic commands ###
