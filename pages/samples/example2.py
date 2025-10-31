import streamlit as st
import pandas as pd
import numpy as np

st.title("Charts Demo")

# Sample Data
data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["Sales", "Profit", "Growth"]
)

st.subheader("Line Chart")
st.line_chart(data)

st.subheader("Bar Chart")
st.bar_chart(data)

st.subheader("Area Chart")
st.area_chart(data)
