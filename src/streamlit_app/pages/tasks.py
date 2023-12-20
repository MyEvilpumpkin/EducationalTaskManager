"""
Tasks page
"""

import streamlit as st  # Required for streamlit components

from providers.tasks import get_relevant_tasks  # Required for content


st.title('Tasks')
st.write(get_relevant_tasks())
