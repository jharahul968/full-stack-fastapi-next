"""create notes table

Revision ID: 0974ce6f2ef1
Revises: 
Create Date: 2023-11-06 12:01:40.595328

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0974ce6f2ef1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # pass
    op.create_table(
        "notes",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("text", sa.String),
        sa.Column ("completed", sa.Boolean)
    )
    


def downgrade():
    # pass
    op.drop_table("notes")
