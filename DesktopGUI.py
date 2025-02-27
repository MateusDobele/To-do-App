import functions
import FreeSimpleGUI as sg
import time

# ensure file is a standalone executable by creating dependency file "todos.txt":
import os

if not os.path.exists("todos.txt"):  # os.path.exists checks if the file / path exists on the device
    # If the file 'todos.txt' doesn't exist on a device, this command will create it:
    with open("todos.txt", "w") as file:
        pass

# set theme:
sg.theme('DarkTeal6')   # google 'pysimplegui themes' to find all themes (e.g., 'DarkTeal6')

# create GUI widgets:
clock = sg.Text('', key='clock')
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter to-do", key="todo")
add_button = sg.Button("Add", size=10)
list_box = sg.Listbox(values=functions.get_todos() or [], key='todos',
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Replace")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

# List of lists to construct the GUI window layout:
layout = [[clock],
          [label],
          [input_box, add_button],
          [list_box, sg.Column([[edit_button], [complete_button]])],  # Column stacks buttons vertically
          [exit_button]]

# 'layout' command is used to connect the GUI widgets (e.g., 'label', 'input_box', etc.)
# to the GUI window (sg.Window)
window = sg.Window('My To-Do App',
                   layout=layout,
                    font=('Helvetica', 20))

# Button implementations in window:
# Event loop
while True:
    event, values = window.read(timeout=10)

    # Handle Window Closed event first
    if event in (sg.WIN_CLOSED, "Exit"):
        break

    # Update the clock
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))

    match event:
        # Add button:
        case "Add":
            new_todo = values["todo"].strip()
            if not new_todo:
                sg.popup("Please enter a valid to-do.", font=("Helvetica", 20))
            else:
                todos = functions.get_todos()
                todos.append(new_todo + "\n")
                functions.write_todos(todos)
                window["todos"].update(values=todos)
                window["todo"].update(value="")  # Clear input field

        # Edit button
        case "Replace":
            if values["todos"]:  # Ensure selection
                todo_to_edit = values["todos"][0]
                new_todo = values["todo"].strip()

                if not new_todo:
                    sg.popup("Please enter a valid to-do before editing.", font=("Helvetica", 20))
                else:
                    todos = functions.get_todos()
                    index = todos.index(todo_to_edit)
                    todos[index] = new_todo + "\n"
                    functions.write_todos(todos)
                    window["todos"].update(values=todos)
                    window["todo"].update(value="")  # Clear input field
            else:
                sg.popup("Please select an item first.", font=("Helvetica", 20))

        # Complete button
        case "Complete":
            if values["todos"]:  # Ensure an item is selected before attempting removal
                todo_to_complete = values["todos"][0].strip()
                todos = [t.strip() for t in functions.get_todos()]  # Normalize all stored todos

                if todo_to_complete in todos:
                    todos.remove(todo_to_complete)
                    functions.write_todos([t + "\n" for t in todos])  # Re-add newlines before writing
                    window["todos"].update(values=todos)
                    window["todo"].update(value="")  # Clear input field
                else:
                    sg.popup("Selected to-do not found.", font=("Helvetica", 20))
            else:
                sg.popup("Please select an item first.", font=("Helvetica", 20))

        case "todos":
            if values["todos"]:  # Ensure an item is selected before updating
                window["todo"].update(value=values["todos"][0])

window.close()


