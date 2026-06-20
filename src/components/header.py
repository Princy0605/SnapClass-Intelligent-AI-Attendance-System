import streamlit as st

def header_home():
    logo_url = "https://tse3.mm.bing.net/th/id/OIP.6JJ4a00hlIQx4_Sz5bsQ_QAAAA?r=0&cb=thfc1falcon2&rs=1&pid=ImgDetMain&o=7&rm=3"

    st.markdown(
        f"""
        <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; margin-bottom:30px; margin-top:30px;">
            <img src="{logo_url}" style="height:100px;">
            <h1 style="text-align:center; color:#E0E3FF;">SNAP<br>CLASS</h1>
        </div>
        """,
        unsafe_allow_html=True
    )

# header_home()