from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, Float
from sqlalchemy.orm import relationship
from sqlalchemy.sql.functions import user
from passlib.context import CryptContext

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, unique=True, index=True)
    last_name = Column(String, unique=True, index=True)
    user_name = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    status = Column(String)
    super_user = Column(String)

    


class Task(Base):
    __tablename__ = "task"

    id = Column(Integer, primary_key=True, index=True)
    Task_Name = Column(String, index=True)
    Task_description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    
    
class Project(Base):
    __tablename__ = "project"

    project_id = Column(Integer, primary_key=True, index=True)
    project_name = Column(String(20), index=True)
    date_of_completion = Column(Date, nullable=False)
    budget = Column(Float, nullable=False)
    description = Column(String, index=True)

