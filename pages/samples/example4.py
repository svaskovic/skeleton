import streamlit as st

st.set_page_config(layout="wide")

st.title("Layout and Media Demo")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.header("Column 1")
    st.image("assets/images/cat.png", caption="Cat 😺", use_container_width=True)

with col2:
    st.header("Column 2")
    st.video("https://www.w3schools.com/html/mov_bbb.mp4")

with col3: 
    st.header("Column 3")
    st.caption("To be updated")

with col4:
    st.header("Column 4")
    st.caption("To be updated")

st.markdown("---")

st.subheader("Metric Display")
st.metric("Temperature", "22°C", "-1°C")
