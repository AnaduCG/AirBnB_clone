import json
from models.base_model import BaseModel

class FileStorage:
    __file_path = "file.json"
    __objects = {}
    def all(self):
        return self.__objects

    def new(self, obj):
        string = f"{obj.__class__.__name__}.{str(obj)}"
        self.__objects[string] = obj

    def save(self):
        temp_storage = []
        with open(file=self.__file_path, mode="a", encoding="UTF8") as file:
            json.dump(file, self.__objects)

    def reload(self):
        ...   