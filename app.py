import streamlit as st

st.logo("assets/images/logo.png", size="large")

pages = {
    "My App":[
        st.Page("pages/dashboard.py",title="Dashboard",icon=":material/dashboard:",default=True),
        st.Page( "pages/data.py", title="Data", icon=":material/database:"),
        st.Page("pages/settings.py", title="Settings",icon=":material/settings:"),  
    ],
}

pg = st.navigation(pages)

pg.run()