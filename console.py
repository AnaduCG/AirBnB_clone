import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import json


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    class_key = ['BaseModel', 'User', 'Place', 'State',
                 'City', 'Amenity', 'Review']
    class_val = [BaseModel, User, Place, State,
                City, Amenity, Review]
    
    def do_quit(self, other):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, other):
        """Quit command to exit the program"""
        return True

    def emptyline(self) -> bool:
        """emptyline"""
        ...
    
    def validate(self, other):
        """validate other input"""
        list_paras = other.split(" ")
        if list_paras[0] not in HBNBCommand.class_key:
            print("** class doesn't exist **")
            return False
        else:
            return True
    
    def do_create(self, other):
        """create (className)"""
        if other:
            if self.validate(other):
                list_paras = other.split(" ")
                index = HBNBCommand.class_key.index(list_paras[0])
                print(HBNBCommand.class_val[index]().id)
                models.storage.save()
        else:
            print("** class name missing **")
    
    def do_show(self, other):
        """show (className)"""
        if other:
            if self.validate(other):
                list_other = other.split(" ")
                if len(list_other) == 1:
                    print("** instance id missing **")
                else:
                    models.storage.reload()
                    index = HBNBCommand.class_key.index(list_other[0])
                    load_dict = models.storage.all()
                    string = f"{HBNBCommand.class_key[index]}.{list_other[1]}"
                    dict_text = f"{string}"
                    if dict_text in load_dict:
                        get_id_dict = load_dict[dict_text]
                        print(get_id_dict)
                    else:
                        print("** no instance found **")
        else:
            print("** class name missing **")
    
    def do_destroy(self, other):
        """destroy (className)"""
        if other:
            if self.validate(other):
                list_other = other.split(" ")
                if (len(list_other) == 1):
                    print("** instance id missing **")
                else:
                    models.storage.reload()
                    load_dict = models.storage.all()
                    index = HBNBCommand.class_key.index(list_other[0])
                    string = f"{HBNBCommand.class_key[index]}.{list_other[1]}"
                    dict_text = f"{string}"
                    if dict_text in list(load_dict.keys()):
                        del load_dict[dict_text]
                    else:
                        print("** no instance found **")
                    models.storage.save()
        else:
            print("** class name missing **")
    
    def do_all(self, other):
        """all or all (ClassName)"""
        models.storage.reload()
        JSONLIST = []
        load_dict = models.storage.all()
        if other:
            list_other = other.split(" ")
            class_name = HBNBCommand.class_key
            if list_other[0] in class_name:
                for key in load_dict:
                    if list_other[0] in key:
                        JSONLIST.append(str(load_dict[key]))
                print(json.dumps(JSONLIST))
            else:
                print("** class doesn't exist **")
        else:
            for key in load_dict:
                JSONLIST.append(str(load_dict[key]))
            print(json.dumps(JSONLIST))
                
    def do_update(self, other):
        """update (className)"""
        models.storage.reload()
        if other:
            if self.validate(other):
                list_other = other.split()
                if (len(list_other) == 1):
                    print("** instance id missing **")
                else:
                    load_dict = models.storage.all()#data in json file
                    index = HBNBCommand.class_key.index(list_other[0])
                    dict_text = f"{HBNBCommand.class_key[index]}.{list_other[1]}"
                if dict_text not in load_dict:
                    print("** no instance found **")
                elif len(list_other) == 2:
                    print("** attribute name missing **")
                elif len(list_other) == 3:
                    print("** value missing **")
                else:
                    dict_data = load_dict[dict_text]
                    change_text = list_other[3]
                    no_quote = change_text.strip('"').replace('\\"', '"')
                    if hasattr(dict_data, list_other[2]):
                        json_type = type(getattr(dict_data, list_other[2]))
                        setattr(dict_data, list_other[2], json_type(no_quote))
                    else:
                        setattr(dict_data, list_other[2], no_quote)
                    models.storage.save()
        else:
            print("** class name missing **")
    
    @staticmethod
    def call_show(other):
        list_brack = other.split('"')
        func = list_brack[0].split('.')[-1]  + list_brack[-1]
        id = other.split('"')[1]
        return func, id, len(list_brack)
    
    def default(self, other):
        models.storage.reload()
        JSONLIST = []
        load_dict = models.storage.all()
        if other:
            """CALL ALL"""
            list_other = other.split(".")
            class_name = HBNBCommand.class_key
            if list_other[0] in class_name:
                if list_other[1] == "all()":
                    for key in load_dict:
                        if list_other[0] in key:
                            JSONLIST.append(str(load_dict[key]))
                    print(json.dumps(JSONLIST))
                """CALL COUNT"""
                if list_other[1] == "count()":
                    count = 0
                    for key in load_dict:
                        if list_other[0] in key:
                            count = count + 1
                    print(count)
                    return
                """CALL SHOW"""
                func, id, length = HBNBCommand.call_show(other)
                if func == "show()" and length > 1:
                    models.storage.reload()
                    index = HBNBCommand.class_key.index(list_other[0])
                    load_dict = models.storage.all()
                    string = f"{HBNBCommand.class_key[index]}.{id}"
                    dict_text = f"{string}"
                    string_id = string.split('.')[1]
                    if dict_text in load_dict and id == string_id:
                        print(load_dict[dict_text])
                    else:
                        print("** no instance found **")
            else:
                print("** class doesn't exist **")

if __name__ == "__main__":
    HBNBCommand().cmdloop()