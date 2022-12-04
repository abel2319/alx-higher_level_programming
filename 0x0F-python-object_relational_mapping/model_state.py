#!/usr/bin/python3
"""
the class definition of a State and an instance Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class States(Base):
    """Class States
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, NOT NULL, AUTO_INCREMENT)
    name = Column(String(256))
