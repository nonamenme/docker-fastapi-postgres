"""create users table

Revision ID: a73cea6a3257
Revises: 07d1a7a766a6
Create Date: 2023-05-12 18:47:29.011602+09:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a73cea6a3257'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('login_id', sa.String(50), nullable=False),
        sa.Column('password', sa.Text(), nullable=False),
    )


def downgrade():
    op.drop_table('users')
