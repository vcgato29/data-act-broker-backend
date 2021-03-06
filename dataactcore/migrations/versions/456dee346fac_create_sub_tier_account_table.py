"""create sub tier account table

Revision ID: 456dee346fac
Revises: 32435c7f73b9
Create Date: 2017-01-06 12:30:37.209575

"""

# revision identifiers, used by Alembic.
revision = '456dee346fac'
down_revision = '32435c7f73b9'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade(engine_name):
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name):
    globals()["downgrade_%s" % engine_name]()





def upgrade_data_broker():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sub_tier_agency',
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('sub_tier_agency_id', sa.Integer(), nullable=False),
    sa.Column('sub_tier_agency_code', sa.Text(), nullable=False),
    sa.Column('sub_tier_agency_name', sa.Text(), nullable=True),
    sa.Column('cgac_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['cgac_id'], ['cgac.cgac_id'], name='fk_sub_tier_agency_cgac'),
    sa.PrimaryKeyConstraint('sub_tier_agency_id')
    )
    op.create_index(op.f('ix_sub_tier_agency_sub_tier_agency_code'), 'sub_tier_agency', ['sub_tier_agency_code'], unique=True)
    ### end Alembic commands ###


def downgrade_data_broker():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_sub_tier_agency_sub_tier_agency_code'), table_name='sub_tier_agency')
    op.drop_table('sub_tier_agency')
    ### end Alembic commands ###

