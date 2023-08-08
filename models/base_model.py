"""
uuid - randomly get a unique id
datetime - get the current day and time
"""
import uuid
from datetime import datetime


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

    def __str__(self):
        """returns string representation of the object"""
        return f"[{__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updating time"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """return a dictionary representation"""
        self.created_at = datetime.isoformat(self.created_at)
        self.updated_at = datetime.isoformat(self.updated_at)
        inst_dict = self.__dict__
        inst_dict["__class__"] = __class__.__name__
        return inst_dict
