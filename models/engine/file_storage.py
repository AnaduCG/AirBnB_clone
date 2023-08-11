#!/usr/bin/python3
import json
from models.base_model import BaseModel
from models.user import User


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
        """serialize object to json file"""
        dummy_dict = {}
        for key, value in self.__objects.items():
            dummy_dict[key] = value.to_dict()
        with open(self.__file_path, mode="w", encoding="UTF8") as file:

            json.dump(dummy_dict, file)

    def reload(self):
        """deserialize object from json file"""
        try:
            with open(self.__file_path, mode="r", encoding="UTF8") as file:
                json_data = json.load(file)
            for key, value in json_data.items():
                class_name = value["__class__"]
                del value["__class__"]
                obj = eval(class_name)(**value)
                self.__objects[key] = obj
        except Exception:
            pass
