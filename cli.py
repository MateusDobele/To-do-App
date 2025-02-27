# 2 approaches for importing functions:
# Approach 1:
# from functions import get_todos, write_todos
# Approach 2 (requires adding "functions." in the script):
import functions

# Add 'Date' function:
import time
now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

# Create action for user to enter either 'add', 'show', 'edit', 'completed' or 'exit':
while True:  # Start an infinite loop to continuously prompt the user for the following actions:
    user_action = input("Type add, show, edit, complete or exit: ")  # Prompt user for action
    user_action = user_action.strip()  # Remove any leading/trailing whitespace from user input

    if user_action.startswith("add"):  # Case when user inputs 'add' or 'new'
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + '\n')  # Append new to-do item to the list

        functions.write_todos(todos, "todos.txt")

    elif user_action.startswith("show"):

        todos = functions.get_todos()

        # for loop to print / show each to-do item individually.
        for index, item in enumerate(todos):  # enumerate in for loop requires 2 arguments (index & item).
            item = item.strip('\n')  # strip '\n' from each item to remove white space between printed items in list.
            row = f"{index + 1}-{item}"  # f-string to allow editing the white spaces between the string outputs.
            print(row)  # the row, containing the 'index' and 'item' are printed.

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1  # List Indexing starts from 0, so this ensures user intput 1 = 0 and so forth.

            todos = functions.get_todos()

            new_todo = input("Enter new to-do:")
            todos[number] = new_todo + '\n'  # List indexing & Replacing Item: accesses 'number' in to-do list to be edited.

            functions.write_todos(todos, "todos.txt")

        except ValueError:  # the specific type of exception that is expected during the 'try'
            print("Your command is not valid.")
            continue  # used to 'continue the loop' (i.e., restart the current loop)

    elif user_action.startswith("complete"):
        try:
            number = int(input("Number of the to-do to mark as completed: "))

            todos = functions.get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos, "todos.txt")

            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)
        except IndexError:  # the specific type of exception that is expected during the 'try'
            print("There is no item with that number.")
            continue

    elif user_action.startswith("complete"):
        break  # 'break': breaks loop and moves on to next line of code outside of the loop.

    else:
        print("Command is not valid.")

print("Goodbye!")