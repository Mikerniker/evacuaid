import hmac
import streamlit as st
from st_pages import Page, show_pages, hide_pages


show_pages(
    [
        Page("Home.py", "Home", "🏠"),
        Page("pages/Evacuation_Sites.py", "Evacuation Sites",
             "🗺️"),
        Page("pages/Chat.py", "Chat", "💬"),
        Page("pages/Situation_Report.py", "Login", "🔒"),
    ]
)
hide_pages(
    [

        Page("pages/Report_Records.py", "Records and Inventory",
             "📄"),
    ]
)

def check_password():
    """Returns `True` if the user had a correct password."""

    def login_form():
        """Form with widgets to collect user information"""
        with st.form("Credentials"):
            st.text_input("Username", key="username")
            st.text_input("Password", type="password", key="password")
            st.form_submit_button("Log in", on_click=password_entered)

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if st.session_state["username"] in st.secrets[
            "passwords"
        ] and hmac.compare_digest(
            st.session_state["password"],
            st.secrets.passwords[st.session_state["username"]],
        ):
            st.session_state["password_correct"] = True
            del st.session_state["password"]
            del st.session_state["username"]

            #ADD CONDITION FOR SIDEBAR
            show_pages(
                [
                    Page("Home.py", "Home", "🏠"),
                    Page("pages/Evacuation_Sites.py", "Evacuation Sites",
                         "🗺️"),
                    Page("pages/Chat.py", "Chat", "💬"),
                    Page("pages/Situation_Report.py", "Situation Report",
                         "📝"),
                    Page("pages/Report_Records.py", "Records and Inventory",
                         "📄"),
                ]
            )

        else:
            st.session_state["password_correct"] = False



    if st.session_state.get("password_correct", False):
        return True

    login_form()
    if "password_correct" in st.session_state:
        st.error("😕 User not known or password incorrect")
    return False


if not check_password():
    st.stop()
