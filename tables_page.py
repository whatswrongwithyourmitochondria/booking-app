import streamlit as st
from datetime import datetime, timedelta

from table import Table
from booking import Booking
import tables_manager

def tables():
    '''Tables page is responsible for instant booking (for those who came without booking),
    releasing tables and for adding new tables'''

    st.subheader("Instant booking for guests without pre-booked tables")

    start = datetime.now()
    end = start + timedelta(hours=1)
    free_tables = tables_manager.free_tables(start, end)

    '''We create a function that adds a table to bookings instantly'''
    def add_table(table, start, end):
        table.add(Booking("Instant booking", "XXXXXXXXXX", start, end))

    for table in free_tables:
        st.button(f"Take {table.name} - {table.seats}",
                  on_click=add_table,
                  args=(table, start, end))

    '''This function is used to release a table and leaves a list of free tables'''
    def release_table(table, start):
        table.release(start)

    busy_tables = tables_manager.busy_tables(start, start)

    st.subheader("Release tables")

    for table in busy_tables:
        st.button(f"Release {table.name} - {table.seats}",
                  on_click=release_table,
                  args=(table, start))

    '''
    in this part we create a new table and add it to our session_state
    '''
    st.subheader("Add a new table")
    input_name = st.text_input("Name of Table")
    input_seats = st.number_input("Number of seats", 0, 12)

    new_table = Table(input_name, input_seats)
    add = st.button("Add", key="new")
    if add:
        st.session_state.tables.append(new_table)
        st.success("The table is added")








