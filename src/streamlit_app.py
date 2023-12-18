import sys

import streamlit as st
from streamlit.web import cli as stcli
from st_pages import Page, show_pages


def main():
    st.title("Educational Task Manager")
    st.text("Please select page")

    show_pages(
        [
            Page("streamlit_pages/motivation.py", "Motivation", "🙌"),
            Page("streamlit_pages/tasks.py", "Tasks", "🗓"),
        ]
    )


if __name__ == '__main__':
    if st.runtime.exists():
        main()
    else:
        sys.argv = ['streamlit', 'run', sys.argv[0]]
        sys.exit(stcli.main())
