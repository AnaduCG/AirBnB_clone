import cmd
from models.base_model import BaseModel
import models
import json


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    class_names = {'BaseModel': BaseModel}

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
        key_list = list(HBNBCommand.class_names.keys())
        if list_paras[0] not in key_list[0]:
            print("** class doesn't exist **")
            return False
        else:
            return True
    
    def do_create(self, other):
        """create (className)"""
        if other:
            if self.validate(other):
                new_insts = list(HBNBCommand.class_names.values())[0]()
                print(new_insts.id)
                models.storage.save()
        else:
            print("** class name missing **")
    
    def do_show(self, other):
        """show (className)"""
        if other:
            if self.validate(other):
                list_other = other.split()
                if len(list_other) == 1:
                    print("** instance id missing **")
                else:
                    models.storage.reload()
                    key_list = list(HBNBCommand.class_names.keys())
                    load_dict = models.storage.all()
                    dict_text = f"{key_list[0]}.{list_other[1]}"
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
                    key_list = list(HBNBCommand.class_names.keys())
                    dict_text = f"{key_list[0]}.{list_other[1]}"
                    if dict_text in list(load_dict.keys()):
                        del load_dict[dict_text]
                    else:

                        print("** no instance found **")
                    models.storage.save()
        else:
            print("** class name missing **")
    
    def do_all(self, other):
        """all (ClassName)"""
        models.storage.reload()
        JSONLIST = []
        load_dict = models.storage.all()
        if other:
            list_other = other.split(" ")
            class_name = "BaseModel"
            if list_other[0] == class_name:
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
        if other:
            if self.validate(other):
                list_other = other.split()
                if (len(list_other) == 1):
                    print("** instance id missing **")
                else:
                    models.storage.reload()
                    load_dict = models.storage.all()#data in json file
                    key_list = list(HBNBCommand.class_names.keys())
                    dict_text = f"{key_list[0]}.{list_other[1]}"
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


if __name__ == "__main__":
    HBNBCommand().cmdloop()