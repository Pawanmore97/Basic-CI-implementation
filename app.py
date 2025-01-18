import streamlit as st

st.title("Welcome to this page")


a = st.number_input(label="Enter the number")

b = a*a

st.button(label="submmit")

st.write(b)