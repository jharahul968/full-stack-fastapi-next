"""create notes table

Revision ID: 501e77d46d45
Revises: 
Create Date: 2023-11-11 21:31:52.778190

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '501e77d46d45'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "notes",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("text", sa.String),
        sa.Column("completed", sa.Boolean)
    )


def downgrade():
    op.drop_table("notes")
