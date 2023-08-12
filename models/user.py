#!/usr/bin/python3
"""imports BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """inherites from Base Model"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
    def __init__(self, *args, **kwargs):
        """update kwargs with user elements"""
        super().__init__(*args, **kwargs)
