import streamlit as st

st.set_page_config(page_title="Custom Styling", layout="wide")
st.markdown("<h1 style='color: blue;'>Custom HTML Styling</h1>", unsafe_allow_html=True)

st.markdown(
    """
    <style>
    .big-font {
        font-size:30px !important;
        color: green;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<p class="big-font">This is a custom styled paragraph.</p>', unsafe_allow_html=True)
