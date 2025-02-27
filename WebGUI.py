import streamlit as st
import functions

# Retrieve the list of to-do items from the functions module
todos = functions.get_todos()

# Function to add a new to-do item to the list and update the file
def add_todo():
    todo = st.session_state["new_todo"] + "\n"  # Retrieve new to-do from session state
    todos.append(todo)  # Add new to-do to the list
    functions.write_todos(todos)  # Save updated list to the file

# Set the title and write a message for the Streamlit web app
st.title("To-do App")
st.write("Today I will:")

# Create a checkbox for each to-do item in the list
for todo in todos:
    st.checkbox(todo)

# Create a text input field for adding new to-do items
# The 'on_change' parameter triggers the 'add_todo' function when input is submitted
# The 'key' stores the input value in the session state
st.text_input(label="", placeholder="Enter a new to-do...",
              on_change=add_todo, key='new_todo')