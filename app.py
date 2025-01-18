import streamlit as st

st.title("Welcome to this page")


a = st.number_input(label="Enter the number")

b = a*a
c = a**3

st.button(label="submmit")

st.write(b)
st.write(c)
