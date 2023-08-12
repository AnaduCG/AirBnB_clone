#!/usr/bin/python3
"""imports BaseModel"""
from models.base_model import BaseModel


class Review(BaseModel):
    """inherites from BaseModel"""

    def __init__(self, *args, **kwargs):
        """update review in kwargs"""
        self.place_id = ""
        self.user_id = ""
        self.text = ""
        super().__init__(*args, **kwargs)