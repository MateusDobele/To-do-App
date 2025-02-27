import streamlit as st
import functions

# Retrieve the list of to-do items from the functions module
todos = functions.get_todos()

# Set the title and write a message for the Streamlit web app
st.title("To-do App")
st.write("Today I will:")

# Create a checkbox for each to-do item in the list
for todo in todos:
    st.checkbox(todo)

# Create text input field containing placeholder for adding new to-do items
st.text_input(label="", placeholder="Enter a new to-do...")