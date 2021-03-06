"""new fields in user model

Revision ID: 291531485550
Revises: caa985be39d5
Create Date: 2020-07-09 01:08:21.156307

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '291531485550'
down_revision = 'caa985be39d5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
