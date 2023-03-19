#!/usr/bin/python3
"""
Defines a class states and an instance Base = declarative_base()
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
	"""Defines class states and inherit from Base"""
	__tablename__ = 'states'

	id = column(Integer, primary_key=True)
	name = column(String(128), nullable=False)
