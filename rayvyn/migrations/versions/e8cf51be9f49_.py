"""empty message

Revision ID: e8cf51be9f49
Revises: 1286c3866b74
Create Date: 2020-09-02 20:21:07.569596

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e8cf51be9f49'
down_revision = '1286c3866b74'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cve__history')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cve__history',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('cve_id', sa.VARCHAR(length=50), nullable=True),
    sa.Column('last_modified', sa.VARCHAR(length=20), nullable=True),
    sa.Column('description', sa.TEXT(), nullable=True),
    sa.Column('vector', sa.VARCHAR(length=50), nullable=True),
    sa.Column('impact', sa.FLOAT(), nullable=True),
    sa.Column('cvss', sa.TEXT(), nullable=True),
    sa.Column('active', sa.INTEGER(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
