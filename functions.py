def get_todos(filepath="todos.txt"):
    """ Read List and get back the result
    to-do List Items
    """
    with open(filepath, 'r') as file_local:
        """ Write file to do List 
        to Do List Write 
        """
        todos_local = file_local.readlines()
    return todos_local


def write_todo(todos_arg, filepath="todos.txt"):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)
