# Define FILEPATH
FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of to-do items. """
    with open(filepath, 'r') as file_local:  # Open the file 'todos.txt' in read mode to check current content.
        todos_local = file_local.readlines()  # Read all lines from the file into a list.
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write a to-do items list in the text file. """
    with open(filepath, 'w') as file:  # Open 'todos.txt' file in write mode to override and add new input.
        file.writelines(todos_arg)  # Write all to-do items back to the file


if __name__ == "__main__":
    print("Hello")
    print(get_todos)
