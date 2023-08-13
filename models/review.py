#!/usr/bin/python3
"""imports BaseModel"""
from models.base_model import BaseModel


class Review(BaseModel):
    """inherites from BaseModel"""

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """update review in kwargs"""
        super().__init__(*args, **kwargs)
