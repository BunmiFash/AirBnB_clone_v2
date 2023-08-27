#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String, ForeignKey
from sqlalchmemy.orm import relationship
from models.user import User
from models.place import Place


class Review(BaseModel, Base):
    """ Review classto store review information """
    __tablename__ = "reviews"

    place_id = Column(String(60), nullable=False, ForeignKey(Place.id))
    user_id = Column(String(60), nullable=False, ForeignKey(User.id))
    text = Column(String(1024), nullable=False)
