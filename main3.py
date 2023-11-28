import streamlit as st
from streamlit_option_menu import option_menu
import about, mapping


st.set_page_config(
    page_title="Visualization of Satellite images",
)


class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({"title": title, "function": func})

    def run():
        # app = st.sidebar(
        with st.sidebar:
            app = option_menu(
                menu_title="SkyMap Canvas",
                options=["시각화", "정보"],
                icons=[
                    "house-fill",
                    "person-circle",
                    "chat-fill",
                    "info-circle-fill",
                ],
                menu_icon="chat-text-fill",
                default_index=1,
                styles={
                    "container": {
                        "padding": "5!important",
                        "background-color": "black",
                    },
                    "icon": {"color": "white", "font-size": "23px"},
                    "nav-link": {
                        "color": "white",
                        "font-size": "20px",
                        "text-align": "left",
                        "margin": "0px",
                        "--hover-color": "blue",
                    },
                    "nav-link-selected": {"background-color": "#02ab21"},
                },
            )

        if app == "시각화":
            mapping.app()
        if app == "정보":
            about.app()

    run()