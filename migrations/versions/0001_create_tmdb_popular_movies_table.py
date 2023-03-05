"""Create tmdb_popular_movies table

Revision ID: 0001
Revises: 
Create Date: 2023-03-03 22:45:03.620664

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '0001'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'tmdb_popular_movies',
        sa.Column('movie_id', sa.Integer(), nullable=False),
        sa.Column('popularity_index', sa.Float(), nullable=False),
        sa.Column('vote_average', sa.Float(), nullable=False),
        sa.Column('vote_count', sa.Integer(), nullable=False),
        sa.Column('collection_date', sa.Date(), nullable=False),
        sa.PrimaryKeyConstraint('movie_id')
    )


def downgrade() -> None:
    op.drop_table('tmdb_popular_movies')
