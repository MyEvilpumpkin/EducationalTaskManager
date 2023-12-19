import sys

import streamlit as st
from streamlit.web import cli as stcli

from src.modules.tasks_handler import get_actual_tasks


def main():
    st.title('Tasks Viewer')
    st.write(get_actual_tasks())


if __name__ == '__main__':
    if st.runtime.exists():
        main()
    else:
        sys.argv = ['streamlit', 'run', sys.argv[0]]
        sys.exit(stcli.main())
