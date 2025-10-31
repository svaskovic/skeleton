import streamlit as st
import pandas as pd

st.title("File Upload & Download")

uploaded_file = st.file_uploader("Upload a CSV", type="csv")
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)

    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("Download CSV", csv, "processed.csv", "text/csv")
