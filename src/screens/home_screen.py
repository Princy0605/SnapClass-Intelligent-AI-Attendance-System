import streamlit as st
from src.components.header import header_home
from src.components.footer import footer_home
from src.ui.base_layout import style_base_layout,style_background_home

def home_screen():


    
    style_background_home()
    style_base_layout()

    header_home()
    

    st.markdown("""
        <style>
        div[data-testid="column"]{
            background-color: white;
            padding: 25px;
            border-radius: 15px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        }

        div[data-testid="column"] h2{
            text-align:center;
            color:black !important;
        }
        </style>
        """, unsafe_allow_html=True)

    left, col1, col2, right = st.columns([1,4,4,1], gap="large")

    with col1:
        st.header("I am Student")
        st.image(
            "https://img.freepik.com/premium-vector/cute-school-girl-cartoon-style-vector-illustration_1116403-1778.jpg?w=996",
            width=120
        )

        if st.button("Student Portal", key="student",icon=":material/arrow_outward:",icon_position="right"):
            st.session_state["login_type"] = "student"
            st.rerun()

    with col2:
        st.header("I am Teacher")
        st.image(
            "https://tse1.mm.bing.net/th/id/OIP.4tPgISUmaMInLqVKIzezCgHaHa?r=0&cb=thfc1falcon2&rs=1&pid=ImgDetMain&o=7&rm=3",
            width=120
        )

        if st.button("Teacher Portal", key="teacher",icon=":material/arrow_outward:",icon_position="right"):
            st.session_state["login_type"] = "teacher"
            st.rerun()

    footer_home()
        