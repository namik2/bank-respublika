"""empty message

Revision ID: 087fb1d05838
Revises: 
Create Date: 2022-03-17 19:50:03.339222

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '087fb1d05838'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('card_extensions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('card_number', sa.Integer(), nullable=False),
    sa.Column('pasport_select', sa.String(length=100), nullable=False),
    sa.Column('pasport_number', sa.Integer(), nullable=False),
    sa.Column('order', sa.String(length=100), nullable=False),
    sa.Column('number', sa.Integer(), nullable=False),
    sa.Column('number_select', sa.String(length=100), nullable=False),
    sa.Column('filial_select', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('news',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=200), nullable=True),
    sa.Column('share_time', sa.String(length=200), nullable=True),
    sa.Column('photoImage', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('news_detailed',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=200), nullable=True),
    sa.Column('photoImage', sa.String(length=200), nullable=True),
    sa.Column('description', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('products',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=200), nullable=True),
    sa.Column('description', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('products')
    op.drop_table('news_detailed')
    op.drop_table('news')
    op.drop_table('card_extensions')
    # ### end Alembic commands ###
