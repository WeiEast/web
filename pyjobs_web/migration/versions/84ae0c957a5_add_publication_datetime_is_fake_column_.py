"""Add publication_datetime_is_fake column to job table

Revision ID: 84ae0c957a5
Revises: 3056be06bd1c
Create Date: 2016-01-29 15:01:12.548254

"""

# revision identifiers, used by Alembic.
revision = '84ae0c957a5'
down_revision = '3056be06bd1c'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('jobs', sa.Column('publication_datetime_is_fake', sa.Boolean(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('jobs', 'publication_datetime_is_fake')
    ### end Alembic commands ###
