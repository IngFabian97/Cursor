from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.db.base import Base


class Class(Base):
    __tablename__ = "classes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    slug = Column(String(255), nullable=False, index=True)
    video_url = Column(String(500), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    deleted_at = Column(DateTime, nullable=True)
    
    # Foreign Keys
    course_id = Column(Integer, ForeignKey("courses.id"), nullable=False)

    # Relaciones
    course = relationship("Course", back_populates="classes")

    def __repr__(self):
        return f"<Class(id={self.id}, name='{self.name}', slug='{self.slug}')>" 