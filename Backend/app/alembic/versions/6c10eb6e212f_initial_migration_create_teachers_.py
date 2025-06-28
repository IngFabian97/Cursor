"""Initial migration - Create teachers, courses, and classes tables

Revision ID: 6c10eb6e212f
Revises: 
Create Date: 2025-06-28 05:48:40.921337

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6c10eb6e212f'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # Create teachers table
    op.create_table('teachers',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=255), nullable=False),
        sa.Column('email', sa.String(length=255), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
        sa.Column('deleted_at', sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_teachers_id'), 'teachers', ['id'], unique=False)
    op.create_index(op.f('ix_teachers_email'), 'teachers', ['email'], unique=True)
    
    # Create courses table
    op.create_table('courses',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=255), nullable=False),
        sa.Column('description', sa.Text(), nullable=False),
        sa.Column('thumbnail', sa.String(length=500), nullable=True),
        sa.Column('slug', sa.String(length=255), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
        sa.Column('deleted_at', sa.DateTime(), nullable=True),
        sa.Column('teacher_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['teacher_id'], ['teachers.id'], ),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('slug')
    )
    op.create_index(op.f('ix_courses_id'), 'courses', ['id'], unique=False)
    op.create_index(op.f('ix_courses_slug'), 'courses', ['slug'], unique=True)
    
    # Create classes table
    op.create_table('classes',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=255), nullable=False),
        sa.Column('description', sa.Text(), nullable=False),
        sa.Column('slug', sa.String(length=255), nullable=False),
        sa.Column('video_url', sa.String(length=500), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
        sa.Column('deleted_at', sa.DateTime(), nullable=True),
        sa.Column('course_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['course_id'], ['courses.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_classes_id'), 'classes', ['id'], unique=False)
    op.create_index(op.f('ix_classes_slug'), 'classes', ['slug'], unique=False)


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_index(op.f('ix_classes_slug'), table_name='classes')
    op.drop_index(op.f('ix_classes_id'), table_name='classes')
    op.drop_table('classes')
    op.drop_index(op.f('ix_courses_slug'), table_name='courses')
    op.drop_index(op.f('ix_courses_id'), table_name='courses')
    op.drop_table('courses')
    op.drop_index(op.f('ix_teachers_email'), table_name='teachers')
    op.drop_index(op.f('ix_teachers_id'), table_name='teachers')
    op.drop_table('teachers')
