import streamlit as st
from datetime import datetime, date, timedelta

from booking import Booking
import tables_manager


def bookings():
    '''Booking page is responsible for tables booking in advance. We create a few fields to input
     the information about guests
    '''
    st.subheader("Book a table")

    name = st.text_input("Enter your name")
    phone = st.text_input("Enter your phone number (10 digits)")
    time_from = st.time_input("From")
    period = st.number_input("Period to book (hours)", 1, 12)

    start = datetime.combine(date.today(), time_from)
    end = start + timedelta(hours=period)
    free_tables = tables_manager.free_tables(start, end)

    '''
    we need a separate function responsible for submitting the form that takes the input information as 
    arguments
    '''
    def submit(table, name, phone, start, end):
        try:
            table.add(Booking(name, phone, start, end))
        except Exception as e:
            st.error(str(e))
            return
        st.success(f"{name}, your booking is successful :sunglasses:")

    st.subheader("Free tables to book")
    for table in free_tables:
        st.button(f"{table.name} - {table.seats}",
                  on_click=submit,
                  args=(table, name, phone, start, end))





















