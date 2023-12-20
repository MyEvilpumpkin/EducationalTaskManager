"""
Streamlit multi page app
"""

import os                              # Required for pages connection
import streamlit as st                 # Required for streamlit components
from st_pages import Page, show_pages  # Required for pages


def main():
    """
    Main app function
    """

    st.title('Educational Task Manager')
    st.text('Please select page')

    show_pages(
        [
            Page(os.path.join(os.path.dirname(__file__), 'pages', 'motivation.py'), 'Motivation', '🙌'),
            Page(os.path.join(os.path.dirname(__file__), 'pages', 'tasks.py'), 'Tasks', '🗓')
        ]
    )
