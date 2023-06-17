#!/usr/bin/python3
"""
Defines class State
that inherits from SQLAlchemy Base 
and links to the MySQL table states
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """Class state for MySQL database table"""
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

