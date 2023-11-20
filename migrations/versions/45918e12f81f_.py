"""empty message

Revision ID: 45918e12f81f
Revises: 7febd84044c9
Create Date: 2023-11-20 14:10:36.502322

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '45918e12f81f'
down_revision = '7febd84044c9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('comment', schema=None) as batch_op:
        batch_op.add_column(sa.Column('likes', sa.Integer(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('comment', schema=None) as batch_op:
        batch_op.drop_column('likes')

    # ### end Alembic commands ###
