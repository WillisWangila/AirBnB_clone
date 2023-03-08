#!/usr/bin/python3
"""
Module for Basemodel parent class
This class defines all common attributes/methods for other classes
"""

from datetime import datetime
from uuid import uuid4


class BaseModel:
    """Represents Basemodel parent class
    """

    def __init__(self):
        """
        Creates an instance of BaseModel
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """
        updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values of
        __dict__ of the instance
        1. adds class name to the dictionary
        2. ensures time values are displayed as strings in isoformat """
        my_dict = self.__dict__.copy()
        my_dict['__class__'] = self.__class__.__name__
        my_dict['created_at'] = my_dict['created_at'].isoformat()
        my_dict['updated_at'] = my_dict['updated_at'].isoformat()
        return my_dict

    def __str__(self):
        """
        Prints informal string representation of the object
        """
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")
