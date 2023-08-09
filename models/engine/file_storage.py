#!/usr/bin/python3
import json
import os


class FileStorage:
    """ Class that handles storing data in json format """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Method that returns the dictionary (__objects) """
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        key = f"{obj.__class__.__name__}.{str(obj.id)}"
        self.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """
        json_data = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as f:
            json.dump(json_data, f)

    def reload(self):
        """  deserializes the JSON file to __objects (only if the JSON file """
        from models.base_model import BaseModel

        if os.path.isfile(self.__file_path):
            with open(self.__file_path, 'r') as f:
                object_data = json.load(f)
                for key, value in object_data.items():
                    self.__objects[key] = eval(value['__class__'])(**value)
