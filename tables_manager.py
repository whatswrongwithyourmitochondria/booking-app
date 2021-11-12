#here we import all the necessary libraries
import streamlit as st
from table import Table

def create_tables():
    '''
    Let's create an initial list of tables with seats to choose from.
    First, we initialize an empty list, then we add tables one by one
    '''
    if "tables" in st.session_state:
        return
    st.session_state.tables = []
    st.session_state.tables.append(Table("Table 1", 4))
    st.session_state.tables.append(Table("Table 2", 2))
    st.session_state.tables.append(Table("Table 3", 8))
    st.session_state.tables.append(Table("Table 4", 10))

'''
We need two functions that return a list of free tables and a list of 
tables that are already busy
'''
def free_tables(start, end):
    return [table for table in st.session_state.tables
            if not table.busy(start, end)]

def busy_tables(start, end):
    return [table for table in st.session_state.tables
            if table.busy(start, end)]