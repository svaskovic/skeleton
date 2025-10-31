import streamlit as st

# Page title and introduction
st.title("Title")
st.caption("This page demonstrates Streamlit's layout and text formatting elements.")

# Header and subheader
st.header("Section 1: Headers and Markdown")
st.subheader("Using headers and subheaders to organize your content")

# Markdown and text
st.markdown("""
You can use **Markdown** to style text:
- **Bold**
- *Italic*
- [Links](https://streamlit.io)
- `Inline code`
""")

st.text("This is plain text.")
st.code("print('Hello, Streamlit!')", language="python")
st.latex(r"E = mc^2")

# Divider
st.divider()

# Layout with columns
st.header("Section 2: Columns and Containers")

col1, col2 = st.columns(2)
with col1:
    st.markdown("**Left Column**")
    st.write("You can put text, charts, and other elements here.")
with col2:
    st.markdown("**Right Column**")
    st.write("This is useful for side-by-side layout.")

# Container
with st.container():
    st.info("This block is inside a container.")
    st.write("Containers can be used to group elements together logically.")

# Expander
with st.expander("Click to expand this section"):
    st.write("Expandable content is great for hiding optional details.")
    st.code("st.expander('More info')", language="python")

# Footer
st.divider()
st.caption("End of Report 1 - Text & Layout Demo")
