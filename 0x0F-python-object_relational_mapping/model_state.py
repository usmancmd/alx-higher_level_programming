#!/usr/bin/python3
"""
Defines a class states and an instance Base = declarative_base()
"""

from sqlalchemy import (Column, Integer, String)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Defines class states that inherit from Base"""
    __tablename__ = 'states'

    id = column(Integer, autoincrement=True, unique=True,
                nullable=False, primary_key=True)
    name = column(String(128), nullable=False)
