#!/usr/bin/python3
"""
Module for Basemodel parent class
This class defines all common attributes/methods for other classes
"""

from datetime import datetime
from uuid import uuid4
import models


class BaseModel:
    """Represents Basemodel parent class
    """

    def __init__(self, *args, **kwargs):
        """
        Creates an instance of BaseModel
        Args:
            *args: list of arguments
            **kwargs: dict of key/value arguments
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def save(self):
        """
        updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

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
