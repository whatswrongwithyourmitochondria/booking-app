import streamlit as st
from datetime import datetime
import tables_manager

'''Status page displays all free tables with seats and calculates a number of free tables and seats'''
def status():

    st.header("Status")

    st.subheader("Shows all the free tables right now")
    start = datetime.now()
    #end = start + timedelta(hours=1))
    free_tables = tables_manager.free_tables(start, start)
    for table in free_tables:
        st.write(f"{table.name} - {table.seats} is free")

    st.subheader("Number of free tables and seats:")
    st.write(f"{len([table.name for table in free_tables])} tables and"
             f" {sum([table.seats for table in free_tables])} seats")

