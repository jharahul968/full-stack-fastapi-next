"""create note table

Revision ID: 08ba64b07bcf
Revises: 0974ce6f2ef1
Create Date: 2023-11-06 16:02:10.524240

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '08ba64b07bcf'
down_revision = '0974ce6f2ef1'
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