"""
Streamlit app launcher
"""

import streamlit as st                  # Required for Streamlit running from command line
import sys                              # Required for Streamlit running from python script
from streamlit.web import cli as stcli  # Required for Streamlit running from python script

from streamlit_app import app  # Required for app launching


if __name__ == '__main__':
    if st.runtime.exists():
        app.main()
    else:
        sys.argv = ['streamlit', 'run', sys.argv[0]]
        sys.exit(stcli.main())
