#!/usr/bin/python3
"""This module creates a Review class"""
from models.base_model import BaseModel


class Review(BaseMode):
    """Class for managing review objects"""

    place_id = ""
    user_id = ""
    text = ""
