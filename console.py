import cmd
import models.base_model as model
import models


class HBNBCommand(cmd.Cmd):
    """hbnb command line"""

    prompt = "(hbnb) "
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
        if len(list_other) > 0 and list_other[0] != '':
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
        if len(list_other) > 0 and list_other[0] != '':
            class_name = model.BaseModel().__class__.__name__
            if class_name != list_other[0]:
                print("** class doesn't exist **")
            elif len(list_other) == 1:
                print("** instance id missing **")
            else:
                load_dict = models.storage.all()
                dict_text = f"{class_name}.{list_other[1]}"
                if dict_text in load_dict:
                    get_id_dict = load_dict[f"{class_name}.{list_other[1]}"]
                    print(get_id_dict)
                else:
                    print("** no instance found **")
    
    def do_destroy(self, other):
        list_other = other.split(" ")
        if len(list_other) > 0 and list_other[0] != '':
            class_name = model.BaseModel().__class__.__name__
            if other[0] != class_name:
                print("** class doesn't exist **")
            else:
                ...
    
    def do_all(self, other):
        ...
    
    def do_update(self, other):
        ...

if __name__ == "__main__":
    HBNBCommand().cmdloop()