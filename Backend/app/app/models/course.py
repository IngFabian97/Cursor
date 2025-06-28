from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.db.base import Base


class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    thumbnail = Column(String(500), nullable=True)
    slug = Column(String(255), unique=True, nullable=False, index=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    deleted_at = Column(DateTime, nullable=True)
    
    # Foreign Keys
    teacher_id = Column(Integer, ForeignKey("teachers.id"), nullable=False)

    # Relaciones
    teacher = relationship("Teacher", back_populates="courses")
    classes = relationship("Class", back_populates="course")

    def __repr__(self):
        return f"<Course(id={self.id}, name='{self.name}', slug='{self.slug}')>" 