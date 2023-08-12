#!/usr/bin/python3
"""interactive shell"""
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
    """console interface"""

    prompt = "(hbnb) "
    class_key = [
            'BaseModel', 'User', 'Place', 'State',
            'City', 'Amenity', 'Review'
            ]
    class_val = [
            BaseModel, User, Place, State,
            City, Amenity, Review
            ]

    def do_quit(self, other):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, other):
        """Quit command to exit the program"""
        print()
        return True

    def emptyline(self) -> bool:
        """emptyline"""
        pass

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

    @staticmethod
    def load_only(list_other):
        """reload the json file"""
        models.storage.reload()
        index = HBNBCommand.class_key.index(list_other[0])
        load_dict = models.storage.all()
        return index, load_dict

    def do_show(self, other):
        """show (className)"""
        if other:
            if self.validate(other):
                list_other = other.split(" ")
                if len(list_other) == 1:
                    print("** instance id missing **")
                else:
                    index, load_dict = HBNBCommand.load_only(list_other)
                    string = f"{HBNBCommand.class_key[index]}.{list_other[1]}"
                    dict_text = f"{string}"
                    if dict_text in load_dict:
                        get_id_dict = load_dict[dict_text]
                        print(get_id_dict)
                    else:
                        print("** no instance found **")
        else:
            print("** class name missing **")

    def help_destroy(self, list_other):
        """help function to distroy the object from the json file"""
        index, load_dict = HBNBCommand.load_only(list_other)
        string = f"{HBNBCommand.class_key[index]}.{list_other[1]}"
        dict_text = f"{string}"
        if dict_text in list(load_dict.keys()):
            del load_dict[dict_text]
        else:
            print("** no instance found **")
        models.storage.save()

    def do_destroy(self, other):
        """destroy (className)"""
        if other:
            if self.validate(other):
                list_other = other.split(" ")
                if (len(list_other) == 1):
                    print("** instance id missing **")
                else:
                    print(list_other)
                    self.help_destroy(list_other)
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
                list_other = other.split(" ")
                if (len(list_other) == 1):
                    print("** instance id missing **")
                else:
                    load_dict = models.storage.all()
                    index = HBNBCommand.class_key.index(list_other[0])
                    s = f"{HBNBCommand.class_key[index]}.{list_other[1]}"
                    dict_text = f"{s}"
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
        """call the get the name of func, id and length

        Args:
            other (input in cmd): data from command line

        Returns:
            tuple: return tuple of function name and id
        """
        list_brack = other.split('"')
        func = list_brack[0].split('.')[-1] + list_brack[-1]
        id = other.split('"')[1]
        return func, id, len(list_brack)

    def Destroy(self, other, classname):
        """use help documentation just making code short

        Args:
            other (str): data from command line
            classname (str): classname
        """
        func, id, length = HBNBCommand.call_show(other)
        if length > 1:
            if func == "destroy()":
                self.help_destroy([classname, id])
        else:
            pass

    def default(self, other):
        """default when invalid is inputed in the command line"""
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
                    index, load_dict = HBNBCommand.load_only(list_other)
                    string = f"{HBNBCommand.class_key[index]}.{id}"
                    dict_text = f"{string}"
                    string_id = string.split('.')[1]
                    if dict_text in load_dict and id == string_id:
                        print(load_dict[dict_text])
                    else:
                        print("** no instance found **")
                if func == "destroy()":
                    self.Destroy(other, list_other[0])
            else:
                print("** class doesn't exist **")


if __name__ == "__main__":
    """entry point infinit loop"""
    HBNBCommand().cmdloop()