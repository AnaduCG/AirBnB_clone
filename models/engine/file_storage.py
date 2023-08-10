#!/usr/bin/python3
import json
import os


class FileStorage:
    __file_path = "file.json"
    __object = {}

    def all(self):
        return self.__object

    def new(self, obj):
        self.__object[obj.__class__.__name__ + '.' + str(obj.id)] = obj

    def save(self):
        dummy_dict = {}
        empty_string = ""
        for key, value in self.__object.items():
            dummy_dict[key] = value.to_dict()
        empty_string = json.dumps(dummy_dict)
        with open(self.__file_path, mode="w", encoding="UTF8") as file:
            file.write(empty_string)

    def reload(self):
        """  deserializes the JSON file to __objects (only if the JSON file """
        from models.base_model import BaseModel
        """ importing the base model for dictionary evaluation """

        if os.path.isfile(self.__file_path):
            with open(self.__file_path, 'r') as f:
                object_data = json.load(f)
                for key, value in object_data.items():
                    self.__objects[key] = eval(value['__class__'])(**value)
