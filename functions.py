def get_todos(filepath="todos.txt"):
    """ reads a text file and return
    a list of to-do objects
    """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath="todos.txt"):
    """ write the to-do item list to the text file"""
    with open(filepath, "w") as file:
        file.writelines(todos_arg)

""" print(__name__) """
if __name__ == "__main__":
    print("Hello")
    print(get_todos())
