from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)

    tasks = relationship("Task", back_populates="user")

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    description = Column(String(255))
    is_complete = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship("User", back_populates="tasks")
