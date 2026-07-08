import streamlit as st
from src.database.db import create_subject

@st.dialog("Create new Subject")
def create_subject_dialog(teacher_id):
    st.write("Enter the details of new subject")
    sub_id=st.text_input("Subject Code",placeholder="CS101",key="subject_Id")
    sub_name=st.text_input("Subject Name",placeholder="Introduction to Computer Science",key="subject_name")
    sub_section=st.text_input("Section",placeholder="A",key="subject_section")

    if st.button("Create subject Now",type="primary",width="stretch"):
        if sub_id and sub_name and sub_section:
            try:
                create_subject(sub_id,sub_name,sub_section,teacher_id)
                st.toast("Subject Created successfully")
                st.rerun()
            except Exception as e:
                st.error(f"Error:{str(e)}")
        else:
            st.warning("Please fill all the fields")