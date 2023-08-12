#!/usr/bin/python3
"""imports the BaseModel"""
from models.base_model import BaseModel


class City(BaseModel):
    """inherites from Base Class"""

    state_id = ""
    name = ""
    def __init__(self, *args, **kwargs):
        """updates kwargs"""
        super().__init__(*args, **kwargs)