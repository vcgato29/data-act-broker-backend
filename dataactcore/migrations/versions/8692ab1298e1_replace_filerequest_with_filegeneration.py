"""replace FileRequest with FileGeneration

Revision ID: 8692ab1298e1
Revises: 4bbc47f2b48d
Create Date: 2018-10-24 14:54:39.278159

"""

# revision identifiers, used by Alembic.
revision = '8692ab1298e1'
down_revision = '4bbc47f2b48d'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade(engine_name):
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name):
    globals()["downgrade_%s" % engine_name]()





def upgrade_data_broker():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('file_generation',
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('file_generation_id', sa.Integer(), nullable=False),
    sa.Column('request_date', sa.Date(), nullable=False),
    sa.Column('start_date', sa.Date(), nullable=False),
    sa.Column('end_date', sa.Date(), nullable=False),
    sa.Column('agency_code', sa.Text(), nullable=False),
    sa.Column('agency_type', sa.Enum('awarding', 'funding', name='generation_agency_types'), server_default='awarding', nullable=False),
    sa.Column('file_type', sa.Enum('D1', 'D2', name='generation_file_types'), server_default='D1', nullable=False),
    sa.Column('file_path', sa.Text(), nullable=True),
    sa.Column('is_cached_file', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('file_generation_id')
    )
    op.create_index(op.f('ix_file_generation_agency_code'), 'file_generation', ['agency_code'], unique=False)
    op.create_index(op.f('ix_file_generation_agency_type'), 'file_generation', ['agency_type'], unique=False)
    op.create_index(op.f('ix_file_generation_end_date'), 'file_generation', ['end_date'], unique=False)
    op.create_index(op.f('ix_file_generation_file_type'), 'file_generation', ['file_type'], unique=False)
    op.create_index(op.f('ix_file_generation_request_date'), 'file_generation', ['request_date'], unique=False)
    op.create_index(op.f('ix_file_generation_start_date'), 'file_generation', ['start_date'], unique=False)
    op.add_column('job', sa.Column('file_generation_id', sa.Integer(), nullable=True))
    op.create_foreign_key('fk_file_request_file_generation_id', 'job', 'file_generation', ['file_generation_id'], ['file_generation_id'], ondelete='SET NULL')
    op.drop_column('job', 'from_cached')
    # ### end Alembic commands ###


def downgrade_data_broker():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('job', sa.Column('from_cached', sa.BOOLEAN(), server_default=sa.text('false'), autoincrement=False, nullable=False))
    op.drop_constraint('fk_file_request_file_generation_id', 'job', type_='foreignkey')
    op.drop_column('job', 'file_generation_id')
    op.drop_index(op.f('ix_file_generation_start_date'), table_name='file_generation')
    op.drop_index(op.f('ix_file_generation_request_date'), table_name='file_generation')
    op.drop_index(op.f('ix_file_generation_file_type'), table_name='file_generation')
    op.drop_index(op.f('ix_file_generation_end_date'), table_name='file_generation')
    op.drop_index(op.f('ix_file_generation_agency_type'), table_name='file_generation')
    op.drop_index(op.f('ix_file_generation_agency_code'), table_name='file_generation')
    op.drop_table('file_generation')
    op.execute("""
        DROP TYPE generation_agency_types
    """)
    op.execute("""
        DROP TYPE generation_file_types
    """)
    # ### end Alembic commands ###

