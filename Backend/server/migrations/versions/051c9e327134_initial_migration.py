"""Initial migration.

Revision ID: 051c9e327134
Revises: 05be42a1a785
Create Date: 2024-07-12 18:48:53.859791
"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '051c9e327134'
down_revision = '05be42a1a785'
branch_labels = None
depends_on = None


def upgrade():
    # Create 'users' table
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('username', sa.String(length=50), nullable=False),
        sa.Column('email', sa.String(length=120), nullable=False),
        sa.Column('password_hash', sa.String(length=128), nullable=False),  # Adjusted to match your model
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('username'),
        sa.UniqueConstraint('email')
    )

    # Create 'accounts' table
    op.create_table(
        'accounts',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('amount', sa.Float(), nullable=False),  # Adjusted to match your model
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
        sa.PrimaryKeyConstraint('id')
    )

    # Create 'transactions' table
    op.create_table(
        'transactions',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),  # Adjusted to match your model
        sa.Column('amount', sa.Float(), nullable=False),
        sa.Column('type', sa.String(), nullable=False),  # Adjusted to match your model
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
        sa.PrimaryKeyConstraint('id')
    )

    # Create 'savings' table
    op.create_table(
        'savings',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('amount', sa.Float(), nullable=False),
        sa.Column('target_date', sa.Date(), nullable=False),  # Adjusted to match your model
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
        sa.PrimaryKeyConstraint('id')
    )

    # Create 'loans' table
    op.create_table(
        'loans',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('borrowed_amount', sa.Float(), nullable=False),  # Adjusted to match your model
        sa.Column('borrow_date', sa.Date(), nullable=False),  # Adjusted to match your model
        sa.Column('target_date', sa.Date(), nullable=False),  # Adjusted to match your model
        sa.Column('trustee', sa.String(), nullable=False),  # Adjusted to match your model
        sa.Column('trustee_phone_number', sa.String(), nullable=False),  # Adjusted to match your model
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
        sa.PrimaryKeyConstraint('id')
    )

    # Create 'subscriptions' table
    op.create_table(
        'subscriptions',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('start_date', sa.Date(), nullable=False),
        sa.Column('end_date', sa.Date(), nullable=True),  # Adjusted to match your model
        sa.Column('status', sa.String(), nullable=False),  # Adjusted to match your model
        sa.Column('service_provider', sa.String(), nullable=False),  # Adjusted to match your model
        sa.Column('plan', sa.String(), nullable=False),  # Adjusted to match your model
        sa.Column('amount', sa.Float(), nullable=False),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
        sa.PrimaryKeyConstraint('id')
    )

    # Create 'groups' table
    op.create_table(
        'groups',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=100), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('name')
    )

    # Create 'users_groups' table for many-to-many relationship
    op.create_table(
        'users_groups',
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('group_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
        sa.ForeignKeyConstraint(['group_id'], ['groups.id'], ),
        sa.PrimaryKeyConstraint('user_id', 'group_id')
    )


def downgrade():
    # Drop tables in reverse order of creation
    op.drop_table('users_groups')
    op.drop_table('groups')
    op.drop_table('subscriptions')
    op.drop_table('loans')
    op.drop_table('savings')
    op.drop_table('transactions')
    op.drop_table('accounts')
    op.drop_table('users')
