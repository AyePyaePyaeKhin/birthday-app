import datetime
import streamlit as st
birthday_date = st.date_input("When's your birthday",min_value=datetime.date(1900, 1, 1))
st.write("Your birthday is:", birthday_date)
