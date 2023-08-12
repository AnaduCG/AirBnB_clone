#!/usr/bin/python3
"""imports the BaseModel"""
from models.base_model import BaseModel


class City(BaseModel):
    """inherites from Base Class"""

    def __init__(self, *args, **kwargs):
        """updates kwargs"""
        self.state_id = ""
        self.name = ""
        super().__init__(*args, **kwargs)