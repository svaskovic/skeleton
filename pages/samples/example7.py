import streamlit as st

st.title("Layout & Columns")

col1, col2 = st.columns(2)

with col1:
    st.header("Left Column")
    st.button("Click Me")

with col2:
    st.header("Right Column")
    st.selectbox("Pick one", ["Apple", "Banana", "Cherry"])

with st.expander("See explanation"):
    st.write("This expander hides additional details.")
