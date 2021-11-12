#here we import a library and all the necessary modules
import streamlit as st

import bookings_page
import status_page
import tables_page
import tables_manager


def main():
    '''
    main() function is responsible for the navigation across the app
    '''
    st.title("Table Booking App")

    tables_manager.create_tables()

    menu = ["Booking", "Tables", "Status"]
    page = st.sidebar.selectbox("Menu", menu)
    if page == "Booking":
        bookings_page.bookings()
    elif page == "Tables":
        tables_page.tables()
    elif page == "Status":
        status_page.status()

if __name__ == '__main__':
    main()
