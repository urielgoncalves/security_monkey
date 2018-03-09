"""Adding index to region. Dropping item.cloud.

Revision ID: 2ce75615b24d
Revises: d08d0b37788a
Create Date: 2016-11-15 20:31:27.393066

"""

# revision identifiers, used by Alembic.
revision = '2ce75615b24d'
down_revision = 'd08d0b37788a'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(u'exceptions_tech_id_fkey', 'exceptions', type_='foreignkey')
    op.drop_constraint(u'exceptions_item_id_fkey', 'exceptions', type_='foreignkey')
    op.drop_constraint(u'exceptions_account_id_fkey', 'exceptions', type_='foreignkey')
    op.create_foreign_key(None, 'exceptions', 'account', ['account_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key(None, 'exceptions', 'item', ['item_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key(None, 'exceptions', 'technology', ['tech_id'], ['id'], ondelete='CASCADE')
    op.create_index('ix_item_region', 'item', ['region'], unique=False)
    op.drop_column('item', 'cloud')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('item', sa.Column('cloud', sa.VARCHAR(length=32), autoincrement=False, nullable=True))
    op.drop_index('ix_item_region', table_name='item')
    op.drop_constraint(u'exceptions_tech_id_fkey', 'exceptions', type_='foreignkey')
    op.drop_constraint(u'exceptions_item_id_fkey', 'exceptions', type_='foreignkey')
    op.drop_constraint(u'exceptions_account_id_fkey', 'exceptions', type_='foreignkey')
    op.create_foreign_key(u'exceptions_account_id_fkey', 'exceptions', 'account', ['account_id'], ['id'])
    op.create_foreign_key(u'exceptions_item_id_fkey', 'exceptions', 'item', ['item_id'], ['id'])
    op.create_foreign_key(u'exceptions_tech_id_fkey', 'exceptions', 'technology', ['tech_id'], ['id'])
    ### end Alembic commands ###