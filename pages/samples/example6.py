import streamlit as st

st.title("Session State & Caching")

if "counter" not in st.session_state:
    st.session_state.counter = 0

@st.cache_data
def get_heavy_computation(x):
    return x * 1000

if st.button("Increment Counter"):
    st.session_state.counter += 1

st.write("Counter:", st.session_state.counter)
st.write("Cached Result:", get_heavy_computation(st.session_state.counter))
