"""tables update

Revision ID: 15c9722b94fb
Revises: 776019c487db
Create Date: 2026-09-13 15:24:57.899653

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '15c9722b94fb'
down_revision: Union[str, Sequence[str], None] = '776019c487db'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
