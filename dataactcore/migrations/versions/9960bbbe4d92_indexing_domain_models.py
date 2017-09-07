"""Indexing domain models

Revision ID: 9960bbbe4d92
Revises: d35ecdfc1da7
Create Date: 2017-09-06 13:09:21.210982

"""

# revision identifiers, used by Alembic.
revision = '9960bbbe4d92'
down_revision = 'd35ecdfc1da7'
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
    op.create_index(op.f('ix_cfda_program_archived_date'), 'cfda_program', ['archived_date'], unique=False)
    op.create_index(op.f('ix_cfda_program_program_number'), 'cfda_program', ['program_number'], unique=False)
    op.create_index(op.f('ix_cfda_program_published_date'), 'cfda_program', ['published_date'], unique=False)
    op.create_index(op.f('ix_city_code_city_code'), 'city_code', ['city_code'], unique=False)
    op.create_index(op.f('ix_city_code_state_code'), 'city_code', ['state_code'], unique=False)
    op.create_index(op.f('ix_county_code_county_number'), 'county_code', ['county_number'], unique=False)
    op.create_index(op.f('ix_county_code_state_code'), 'county_code', ['state_code'], unique=False)
    op.create_index(op.f('ix_program_activity_account_number'), 'program_activity', ['account_number'], unique=False)
    op.create_index(op.f('ix_program_activity_agency_id'), 'program_activity', ['agency_id'], unique=False)
    op.create_index(op.f('ix_program_activity_budget_year'), 'program_activity', ['budget_year'], unique=False)
    op.create_index(op.f('ix_program_activity_program_activity_code'), 'program_activity', ['program_activity_code'], unique=False)
    op.create_index(op.f('ix_program_activity_program_activity_name'), 'program_activity', ['program_activity_name'], unique=False)
    op.create_index(op.f('ix_sf_133_agency_identifier'), 'sf_133', ['agency_identifier'], unique=False)
    op.create_index(op.f('ix_sf_133_allocation_transfer_agency'), 'sf_133', ['allocation_transfer_agency'], unique=False)
    op.create_index(op.f('ix_sf_133_fiscal_year'), 'sf_133', ['fiscal_year'], unique=False)
    op.create_index(op.f('ix_sf_133_period'), 'sf_133', ['period'], unique=False)
    op.create_index('ix_sf_133_tas_group', 'sf_133', ['tas', 'fiscal_year', 'period', 'line'], unique=True)
    op.drop_index('ix_sf_133_tas', table_name='sf_133')
    op.create_index(op.f('ix_sf_133_tas'), 'sf_133', ['tas'], unique=False)
    op.create_index(op.f('ix_states_state_code'), 'states', ['state_code'], unique=False)
    op.create_index(op.f('ix_zips_congressional_district_no'), 'zips', ['congressional_district_no'], unique=False)
    op.create_index(op.f('ix_zips_county_number'), 'zips', ['county_number'], unique=False)
    op.create_index(op.f('ix_zips_state_abbreviation'), 'zips', ['state_abbreviation'], unique=False)
    ### end Alembic commands ###


def downgrade_data_broker():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_zips_state_abbreviation'), table_name='zips')
    op.drop_index(op.f('ix_zips_county_number'), table_name='zips')
    op.drop_index(op.f('ix_zips_congressional_district_no'), table_name='zips')
    op.drop_index(op.f('ix_states_state_code'), table_name='states')
    op.drop_index(op.f('ix_sf_133_tas'), table_name='sf_133')
    op.create_index('ix_sf_133_tas', 'sf_133', ['tas', 'fiscal_year', 'period', 'line'], unique=True)
    op.drop_index('ix_sf_133_tas_group', table_name='sf_133')
    op.drop_index(op.f('ix_sf_133_period'), table_name='sf_133')
    op.drop_index(op.f('ix_sf_133_fiscal_year'), table_name='sf_133')
    op.drop_index(op.f('ix_sf_133_allocation_transfer_agency'), table_name='sf_133')
    op.drop_index(op.f('ix_sf_133_agency_identifier'), table_name='sf_133')
    op.drop_index(op.f('ix_program_activity_program_activity_name'), table_name='program_activity')
    op.drop_index(op.f('ix_program_activity_program_activity_code'), table_name='program_activity')
    op.drop_index(op.f('ix_program_activity_budget_year'), table_name='program_activity')
    op.drop_index(op.f('ix_program_activity_agency_id'), table_name='program_activity')
    op.drop_index(op.f('ix_program_activity_account_number'), table_name='program_activity')
    op.drop_index(op.f('ix_county_code_state_code'), table_name='county_code')
    op.drop_index(op.f('ix_county_code_county_number'), table_name='county_code')
    op.drop_index(op.f('ix_city_code_state_code'), table_name='city_code')
    op.drop_index(op.f('ix_city_code_city_code'), table_name='city_code')
    op.drop_index(op.f('ix_cfda_program_published_date'), table_name='cfda_program')
    op.drop_index(op.f('ix_cfda_program_program_number'), table_name='cfda_program')
    op.drop_index(op.f('ix_cfda_program_archived_date'), table_name='cfda_program')
    ### end Alembic commands ###

