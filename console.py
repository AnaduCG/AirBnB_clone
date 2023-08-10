import cmd
import models.base_model as model
import models
import json


class HBNBCommand(cmd.Cmd):
    """hbnb command line"""

    prompt = "(hbnb) "
    class_str_names = ["BaseModel"]
    def do_quit(self, other):
        """Quit command to exit the program"""
        return True
    
    def do_EOF(self, other):
        """Exist the Program"""
        return True
    
    def emptyline(self):
        ...
        
    def do_create(self, other):
        """create (className)"""
        list_other = other.split(" ")
        if other:
            dummy_inst = model.BaseModel()
            class_name = dummy_inst.__class__.__name__
            if class_name == list_other[0]:
                dummy_inst.save()
                print(dummy_inst.id)
            else:
                print("** class doesn't exit **")
        else:
            print("** class name missing **")
        
    def do_show(self, other):
        """show (className)"""
        list_other = other.split(" ")
        if other:
            class_name = model.BaseModel().__class__.__name__
            if class_name != list_other[0]:
                print("** class doesn't exist **")
            elif len(list_other) == 1:
                print("** instance id missing **")
            else:
                models.storage.reload()
                load_dict = models.storage.all()
                dict_text = f"{class_name}.{list_other[1]}"
                if dict_text in load_dict:
                    get_id_dict = load_dict[dict_text]
                    print(get_id_dict)
                else:
                    print("** no instance found **")
        else:
            print("** class name missing **")
    
    def do_destroy(self, other):
        """destory (ClassName)"""
        list_other = other.split(" ")
        if other:
            class_name = model.BaseModel().__class__.__name__
            if class_name != list_other[0]:
                print("** class doesn't exist **")
            elif len(list_other) == 1:
                print("** instance id missing **")
            else:
                models.storage.reload()
                load_dict = models.storage.all()
                dict_text = f"{class_name}.{list_other[1]}"
                if dict_text in load_dict:
                    get_id_dict = load_dict[dict_text]
                    del get_id_dict
                    models.storage.save()
                else:
                    print("** no instance found **")
        else:
            print("** class name missing **")
    
    def do_all(self, other):
        """all (ClassName)"""
        models.storage.reload()
        JSONLIST = []
        load_dict = models.storage.all()
        if not other:
            for key in load_dict:
                JSONLIST.append(str(load_dict[key]))
            print(json.dumps(JSONLIST))
            return
        list_other = other.split(" ")
        class_name = "BaseModel"
        if list_other[0] == class_name:
            for key in load_dict:
                if list_other[0] in key:
                    JSONLIST.append(str(load_dict[key]))
            print(json.dumps(JSONLIST))
        else:
            print("** class doesn't exist **")
    
    def do_update(self, other):
        """update (ClassName)"""
        if other:
            list_other = other.split(" ")
            print(list_other)
            if list_other[0] != "BaseModel":
                print("** class doesn't exist **")
                return
            elif len(list_other) == 1:
                print("** instance id missing **")
                return
            class_name = "BaseModel"
            models.storage.reload()
            load_dict = models.storage.all()
            dict_text = f"{class_name}.{list_other[1]}"
            if dict_text not in load_dict:
                print("** no instance found **")
            elif len(list_other) == 2:
                print("** attribute name missing **")
            elif len(list_other) == 3:
                print("** attribute name missing **")
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