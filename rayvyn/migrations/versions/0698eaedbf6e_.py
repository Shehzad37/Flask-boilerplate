"""empty message

Revision ID: 0698eaedbf6e
Revises: 
Create Date: 2020-07-23 14:36:30.394811

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0698eaedbf6e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cve', sa.Column('advisory_link', sa.String(length=200), nullable=True))
    op.add_column('cve', sa.Column('list_vendors', sa.String(length=50), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('cve', 'list_vendors')
    op.drop_column('cve', 'advisory_link')
    # ### end Alembic commands ###