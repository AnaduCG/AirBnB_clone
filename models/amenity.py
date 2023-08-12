#!/usr/bin/python3
"""import BaseModel to be inherited"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """_summary_

    Args:
        BaseModel (_type_): _description_
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """
        inherite from BaseModel and adds a name
        """
        super().__init__(*args, **kwargs)
