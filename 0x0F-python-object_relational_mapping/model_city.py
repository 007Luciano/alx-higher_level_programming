#!/usr/bin/python3
"""
This module creates a table for City
"""
from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from model_state import Base, State


class City(Base):
    """
    City class that is mapped to our
    cities table
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
