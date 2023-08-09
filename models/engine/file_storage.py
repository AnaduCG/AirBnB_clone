#!/usr/bin/python3
import json


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
        try:
            with open(self.__file_path, mode="r", encoding="UTF8") as file:
                json_data = json.load(file)
            for key, value in json_data.items():
                self.new(BaseModel(**value))
        except Exception:
            return
          