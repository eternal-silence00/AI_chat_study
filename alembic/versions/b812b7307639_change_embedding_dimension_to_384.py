"""change embedding dimension to 384

Revision ID: b812b7307639
Revises: b984aebed2da
Create Date: 2026-06-01 14:49:17.141396

"""
from typing import Sequence, Union

from alembic import op
from pgvector.sqlalchemy import Vector
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b812b7307639'
down_revision: Union[str, Sequence[str], None] = 'b984aebed2da'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column('document', 'embedding',
               existing_type=Vector(1536),
               type_=Vector(384),
               existing_nullable=False)


def downgrade() -> None:
    op.alter_column('document', 'embedding',
               existing_type=Vector(384),
               type_=Vector(1536),
               existing_nullable=False)
