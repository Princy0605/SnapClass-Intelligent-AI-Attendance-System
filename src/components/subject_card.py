import streamlit as st


def subject_card(name, code, section, stats=None, footer_callback=None):
    with st.container(key=f"subject_{code}"):
 
        st.subheader(name)

        st.markdown(
            f"**Code:** `{code}` &nbsp;&nbsp; **Section:** {section}",
            unsafe_allow_html=True,
        )

        if stats:
            cols = st.columns(len(stats))

            for col, (icon, label, value) in zip(cols, stats):
                with col:
                    st.metric(
                        label=f"{icon} {label}",
                        value=value
                    )

        return st.button(
            f"Share Code: {name}",
            key=f"share_{code}",
            icon=":material/share:",
            use_container_width=True
        )