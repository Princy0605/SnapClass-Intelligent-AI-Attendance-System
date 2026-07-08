import streamlit as st

def footer_home():
    logo_url ="src\Self_Logo.png"

    st.markdown(f"""
        <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; items-align:center">
            <p style="font-weight:bold; color:white"> Created with ❤️ by PRINCY JAIN</p>
        </div>

    
    """,unsafe_allow_html=True)

def footer_dashboard():
    logo_url ="src\Self_Logo.png"

    st.markdown(f"""
        <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; items-align:center">
            <p style="font-weight:bold; color:black"> Created with ❤️ by PRINCY JAIN</p>
        </div>

    
    """,unsafe_allow_html=True)