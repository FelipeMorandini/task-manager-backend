from sqlalchemy import Column, Integer, String, Boolean, DateTime ,ForeignKey, func
from sqlalchemy.orm import relationship

from ..database.connection import Base

class Task(Base):
    __tablename__ = "tasks"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    description = Column(String(500), nullable=True)
    deadline = Column(DateTime, nullable=True)
    complete = Column(Boolean, default=False, nullable=False, default=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, nullable=True, onupdate=func.now())
    
    user_id = Column(Integer, ForeignKey("users.id"))
    creator = relationship("User", back_populates="tasks")