import streamlit as st

st.title("Forms & Input Widgets Demo")

with st.form("user_form"):
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=0, max_value=120, step=1)
    dob = st.date_input("Date of Birth")
    newsletter = st.checkbox("Subscribe to newsletter")
    color = st.selectbox("Favorite Color", ["Red", "Blue", "Green", "Yellow"])
    submitted = st.form_submit_button("Submit")

if submitted:
    st.success(f"Submitted: {name}, {age}, {dob}, {color}, Subscribed: {newsletter}")
