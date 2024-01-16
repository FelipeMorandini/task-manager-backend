from sqlalchemy import Column, DateTime, Integer, String, ForeignKey, func
from sqlalchemy.orm import relationship

from ..database.connection import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    username = Column(String(30), nullable=False)
    email = Column(String(50), nullable=False)
    password = Column(String, nullable=False)
    reset_password_code = Column(String(6), nullable=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, nullable=True, onupdate=func.now())
    
    tasks = relationship("Task", back_populates="user")
    
    