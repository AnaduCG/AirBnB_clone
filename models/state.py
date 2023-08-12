#!/usr/bin/python3
"""imports BaseModel"""
from models.base_model import BaseModel


class State(BaseModel):
    """inherites from BaseModel"""

    name = ""

    def __init__(self, *args, **kwargs):
        """update kwargs with state"""
        super().__init__(*args, **kwargs)
