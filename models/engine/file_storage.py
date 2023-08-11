#!/usr/bin/python3
"""import the needed files"""
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    __file_path = "file.json"
    __objects = {}
    def all(self):
        """return object of dictionary"""
        return self.__objects
    
    def new(self, obj):
        """create a new object

        Args:
            obj (obj): instance of object
        """
        class_key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[class_key] = obj
    
    def save(self):
        """serilize object to json file"""
        dummy_dict = {}
        for key, value in self.__objects.items():
            dummy_dict[key] = value.to_dict()
        with open(self.__file_path, mode="w", encoding="UTF8") as file:
            json.dump(dummy_dict, file)
    
    def reload(self):
        """deserilize object from json file"""
        try:
            with open(self.__file_path, mode="r", encoding="UTF8") as file:
                json_data = json.load(file)
            for key, value in json_data.items():
                class_name = value["__class__"]
                if class_name == "BaseModel":
                    self.__objects[key] = BaseModel(**value)
                if class_name == "User":
                    self.__objects[key] = User(**value)
                if class_name == "Place":
                    self.__objects[key] = Place(**value)
                if class_name == "State":
                    self.__objects[key] = State(**value)
                if class_name == "City":
                    self.__objects[key] = City(**value)
                if class_name == "Amenity":
                    self.__objects[key] = Amenity(**value)
                if class_name == "Review":
                    self.__objects[key] = Review(**value)
        except Exception:
            pass
