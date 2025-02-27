# Import necessary libraries
import streamlit as st
import functions


# Retrieve the list of to-do items from the functions module
todos = functions.get_todos()


# Function to add a new to-do item to the list and update the file
def add_todo():
    """Retrieves new to-do from session state, adds it to the list, and updates the file."""
    todo = st.session_state["new_todo"] + "\n"  # Get new to-do from session state
    todos.append(todo)  # Add new to-do to the list
    functions.write_todos(todos)  # Save updated list to the file


# Set the title of the Streamlit web app
st.title("To-do App")

# Display a message above the task list
st.write("Today I will:")


# Iterate through the list of to-do items and create a checkbox for each
for index, todo in enumerate(todos):
    # Assign a checkbox to each to-do item, using the item itself as the unique key
    checkbox = st.checkbox(todo, key=todo)

    # If the checkbox is checked (i.e., task is completed)
    if checkbox:
        todos.pop(index)  # Remove the completed to-do item from the list
        functions.write_todos(todos)  # Update the file to save the change
        del st.session_state[todo]  # Remove the item from session state
        st.rerun()  # Refresh the app to reflect changes instantly


# Create a text input field for adding new to-do items
st.text_input(
    label="",
    placeholder="Enter a new to-do...",
    on_change=add_todo,
    key="new_todo"
)
