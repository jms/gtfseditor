"""Change column type on route.route_short_name

Revision ID: 444bb0eb07bc
Revises: 1a6e215d57c2
Create Date: 2018-06-28 09:33:04.268147

"""

# revision identifiers, used by Alembic.
revision = '444bb0eb07bc'
down_revision = '1a6e215d57c2'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('routes', 'route_short_name',
               existing_type=sa.VARCHAR(length=50),
               type_=sa.Text(),
               existing_nullable=True)
    op.alter_column('routes_version', 'route_short_name',
               existing_type=sa.VARCHAR(length=50),
               type_=sa.Text(),
               existing_nullable=True)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('routes', 'route_short_name',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=50),
               existing_nullable=True)
    op.alter_column('routes_version', 'route_short_name',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=50),
               existing_nullable=True)
    ### end Alembic commands ###
