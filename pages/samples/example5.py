import streamlit as st

st.title("Expanders and Code Viewer")

with st.expander("See explanation"):
    st.write("""
        Expanders let you hide content behind a toggle.
        They're great for FAQs, notes, or step-by-step guides.
    """)

st.subheader("Show Code")
code = '''
def greet(name):
    return f"Hello, {name}!"
'''
st.code(code, language="python")

st.subheader("JSON Display")
sample_data = {
    "name": "Slobo",
    "role": "Director",
    "tools": ["dbt", "Snowflake", "Power BI"]
}
st.json(sample_data)
