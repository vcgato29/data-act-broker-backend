"""add FREC to user model

Revision ID: 4d8408c33fee
Revises: da2e50d423ff
Create Date: 2017-07-06 13:19:01.155328

"""

# revision identifiers, used by Alembic.
revision = '4d8408c33fee'
down_revision = 'da2e50d423ff'
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
    op.add_column('user_affiliation', sa.Column('frec_id', sa.Integer(), nullable=True))
    op.add_column('user_affiliation', sa.Column('user_affiliation_id', sa.Integer(), nullable=False, primary_key=True))
    op.create_index(op.f('ix_user_affiliation_cgac_id'), 'user_affiliation', ['cgac_id'], unique=False)
    op.create_index(op.f('ix_user_affiliation_frec_id'), 'user_affiliation', ['frec_id'], unique=False)
    op.create_index(op.f('ix_user_affiliation_user_id'), 'user_affiliation', ['user_id'], unique=False)
    op.create_foreign_key('user_affiliation_frec_fk', 'user_affiliation', 'frec', ['frec_id'], ['frec_id'], ondelete='CASCADE')
    op.drop_constraint('user_affiliation_pkey', 'user_affiliation', type_='primary')
    op.create_primary_key('user_affiliation_pkey', 'user_affiliation', ['user_affiliation_id'])
    op.alter_column('user_affiliation', 'cgac_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    ### end Alembic commands ###


def downgrade_data_broker():
    op.execute("DELETE FROM user_affiliation "
               "WHERE cgac_id IS NULL")
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user_affiliation', 'cgac_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.drop_constraint('user_affiliation_pkey', 'user_affiliation', type_='primary')
    op.create_primary_key('user_affiliation_pkey', 'user_affiliation', ['user_id', 'cgac_id'])
    op.drop_constraint('user_affiliation_frec_fk', 'user_affiliation', type_='foreignkey')
    op.drop_index(op.f('ix_user_affiliation_user_id'), table_name='user_affiliation')
    op.drop_index(op.f('ix_user_affiliation_frec_id'), table_name='user_affiliation')
    op.drop_index(op.f('ix_user_affiliation_cgac_id'), table_name='user_affiliation')
    op.drop_column('user_affiliation', 'user_affiliation_id')
    op.drop_column('user_affiliation', 'frec_id')
    ### end Alembic commands ###

