import streamlit as st
from streamlit import session_state

import functions

todos=functions.get_todos()

def add_todo():
    todo=st.session_state["new_todo"] +"\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title("My Todo App")
st.write("Use it for your daily life purposes")

for index,todo in enumerate(todos):
    check=st.checkbox(todo, key=todo)
    if check:
        todos.pop(index)
        functions.write_todos(todos)
        del session_state[todo]
        st.rerun()

st.text_input(label="Add your plan", placeholder="Add your item here.....",
              on_change=add_todo,key="new_todo")
