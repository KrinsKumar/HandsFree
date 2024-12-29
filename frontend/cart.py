import streamlit as st
from mycomponent import mycomponent

value = mycomponent()
st.write("Received", value)