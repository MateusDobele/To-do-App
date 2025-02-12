import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter to-do", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=[45,10])
edit_button= sg.Button("Edit")

# List of lists to construct the GUI window layout:
layout = [[label], [input_box, add_button], [list_box, edit_button]]

# 'layout' command is used to connect the 'label', 'input_box', 'add_button', etc to the GUI window
window = sg.Window('My To-Do App',
                   layout=layout,
                    font=('Helvetica', 20))

# Add button implementation:
while True:
    event, values = window.read()
    print(1, event)
    print(2, values)
    print(3, values['todos'])
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break  # 'break' is used to break the (while) loop and proceed to the next block of code
            # if instead of the 'break' statement, the 'exit()' statement would have been used, this command would
            # exit the program entirely and no more code blocks would be run.
window.close()


