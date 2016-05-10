"""init database

Revision ID: 6015ec0f59c9
Revises: 
Create Date: 2016-03-17 11:36:56.904831

"""

# revision identifiers, used by Alembic.
revision = '6015ec0f59c9'
down_revision = 'a118bf9e4970'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade(engine_name):
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name):
    globals()["downgrade_%s" % engine_name]()





def upgrade_error_data():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('error_type',
    sa.Column('error_type_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('error_type_id')
    )
    op.create_table('file_status',
    sa.Column('file_status_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('file_status_id')
    )
    op.create_table('error_data',
    sa.Column('error_data_id', sa.Integer(), nullable=False),
    sa.Column('job_id', sa.Integer(), nullable=True),
    sa.Column('filename', sa.Text(), nullable=True),
    sa.Column('field_name', sa.Text(), nullable=True),
    sa.Column('error_type_id', sa.Integer(), nullable=True),
    sa.Column('occurrences', sa.Integer(), nullable=True),
    sa.Column('first_row', sa.Integer(), nullable=True),
    sa.Column('rule_failed', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['error_type_id'], ['error_type.error_type_id'], ),
    sa.PrimaryKeyConstraint('error_data_id')
    )
    op.create_table('file',
    sa.Column('file_id', sa.Integer(), nullable=False),
    sa.Column('job_id', sa.Integer(), nullable=True),
    sa.Column('filename', sa.Text(), nullable=True),
    sa.Column('file_status_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['file_status_id'], ['file_status.file_status_id'], ),
    sa.PrimaryKeyConstraint('file_id')
    )
    ### end Alembic commands ###


def downgrade_error_data():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('file')
    op.drop_table('error_data')
    op.drop_table('file_status')
    op.drop_table('error_type')
    ### end Alembic commands ###


def upgrade_job_tracker():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('file_type',
    sa.Column('file_type_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('file_type_id')
    )
    op.create_table('status',
    sa.Column('status_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('status_id')
    )
    op.create_table('submission',
    sa.Column('submission_id', sa.Integer(), nullable=False),
    sa.Column('datetime_utc', sa.Text(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('submission_id')
    )
    op.create_table('type',
    sa.Column('type_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('type_id')
    )
    op.create_table('job_status',
    sa.Column('job_id', sa.Integer(), nullable=False),
    sa.Column('filename', sa.Text(), nullable=True),
    sa.Column('status_id', sa.Integer(), nullable=True),
    sa.Column('type_id', sa.Integer(), nullable=True),
    sa.Column('submission_id', sa.Integer(), nullable=True),
    sa.Column('file_type_id', sa.Integer(), nullable=True),
    sa.Column('staging_table', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['file_type_id'], ['file_type.file_type_id'], ),
    sa.ForeignKeyConstraint(['status_id'], ['status.status_id'], ),
    sa.ForeignKeyConstraint(['submission_id'], ['submission.submission_id'], ),
    sa.ForeignKeyConstraint(['type_id'], ['type.type_id'], ),
    sa.PrimaryKeyConstraint('job_id')
    )
    op.create_table('job_dependency',
    sa.Column('dependency_id', sa.Integer(), nullable=False),
    sa.Column('job_id', sa.Integer(), nullable=True),
    sa.Column('prerequisite_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['job_id'], ['job_status.job_id'], ),
    sa.ForeignKeyConstraint(['prerequisite_id'], ['job_status.job_id'], ),
    sa.PrimaryKeyConstraint('dependency_id')
    )
    ### end Alembic commands ###


def downgrade_job_tracker():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('job_dependency')
    op.drop_table('job_status')
    op.drop_table('type')
    op.drop_table('submission')
    op.drop_table('status')
    op.drop_table('file_type')
    ### end Alembic commands ###


def upgrade_user_manager():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('permission_type',
    sa.Column('permission_type_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('permission_type_id')
    )
    op.create_table('user_status',
    sa.Column('user_status_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('user_status_id')
    )
    op.create_table('users',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('username', sa.Text(), nullable=True),
    sa.Column('email', sa.Text(), nullable=True),
    sa.Column('name', sa.Text(), nullable=True),
    sa.Column('agency', sa.Text(), nullable=True),
    sa.Column('title', sa.Text(), nullable=True),
    sa.Column('permissions', sa.Integer(), nullable=True),
    sa.Column('user_status_id', sa.Integer(), nullable=True),
    sa.Column('password_hash', sa.Text(), nullable=True),
    sa.Column('salt', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['user_status_id'], ['user_status.user_status_id'], ),
    sa.PrimaryKeyConstraint('user_id')
    )
    op.create_table('email_template_type',
    sa.Column('email_template_type_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('email_template_type_id')
    )
    op.create_table('email_template',
    sa.Column('email_template_id', sa.Integer(), nullable=False),
    sa.Column('template_type_id', sa.Integer(), nullable=True),
    sa.Column('subject', sa.Text(), nullable=True),
    sa.Column('content', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['template_type_id'], ['email_template_type.email_template_type_id']),
    sa.PrimaryKeyConstraint('email_template_id')
    )
    op.create_table('email_token',
    sa.Column('email_token_id', sa.Integer(), nullable=False),
    sa.Column('token', sa.Text(), nullable=True),
    sa.Column('salt', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('email_token_id')
    )
    ### end Alembic commands ###


def downgrade_user_manager():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('user_status')
    op.drop_table('permission_type')
    op.drop_table('email_template_type')
    op.drop_table('email_template')
    op.drop_table('email_token')
    ### end Alembic commands ###

def upgrade_validation():
    pass

def downgrade_validation():
    pass

