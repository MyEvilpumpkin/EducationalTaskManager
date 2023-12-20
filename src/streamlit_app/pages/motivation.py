"""
Motivation Page
"""

import streamlit as st  # Required for streamlit components

from providers.motivation import get_motivation  # Required for content


st.title('Motivation')
text = st.text_area(label='Запрос', placeholder='Введите запрос...')
if text != '':
    st.write('Ответ')
    st.write(get_motivation(text))
    st.button('Перегенерировать')
else:
    st.write('Для получения ответа необходимо ввести запрос')

