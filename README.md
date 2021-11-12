# Booking-app
A web application is designed to track bookings and manage tables in a restaurant.
(made with the help of Streamlit library: https://docs.streamlit.io/)

run locally: **streamlit run main.py**

# App functionality

The app consists of three pages:
- *bookings_page* is responsible for booking tables in advance entering guest's name, phonenumber, time and period as well as a certain table. Tables are bound with time, so if a table was previously booked for a certain period of time, you can't book this table during that period. Also this page displays only availiable tables with a number of seats. 
- *tables_page* is a page for tables management. It has two main parts:
  - A part for instant booking for those who came without reservation and instant table releasing;
  - A part to add a new table to the pool of existing tables. 

- *status_page* shows all the availiable tables and calculates their number with a number of seats on the whole. 

# App components

- a sidebar with a selectbox widget to navigate across the app;
- **main.py** which is responsible to switch the pages;
- three separate modules with pages **booking_page.py, tables_page.py and status_page.py**
- a module **tables_manager.py** including necessary functions to manage tables statuses;
- separate files with classes **table.py and booking.py**;
- storage of information is implemented via *session_state*: https://docs.streamlit.io/library/api-reference/session-state

**A room for improvement**
always exists :)
