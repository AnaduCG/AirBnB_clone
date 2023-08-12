#!/usr/bin/python3
"""
uuid - randomly get a unique id
datetime - get the current day and time
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """parent class that hold the functionality"""

    def __init__(self, *args, **kwargs):
        """initializing attributes"""
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key in ['created_at', 'updated_at']:
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                self.__setattr__(key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """returns string representation of the object"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updating time"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """return a dictionary representation"""
        if isinstance(self.created_at, datetime):
            self.created_at = self.created_at.isoformat()
        if isinstance(self.updated_at, datetime):
            self.updated_at = self.updated_at.isoformat()
        inst_dict = self.__dict__
        inst_dict["__class__"] = self.__class__.__name__
        return inst_dict
