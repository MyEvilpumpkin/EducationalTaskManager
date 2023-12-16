import sys

import streamlit as st
from streamlit.web import cli as stcli

from motivation_generator import generate


def main():
    st.title("Generator Test")
    text = st.text_area(label="Запрос", placeholder="Введите запрос...")
    if text != "":
        st.write("Ответ")
        st.write(generate(text))
        st.button("Перегенерировать")
    else:
        st.write("Для получения ответа необходимо ввести запрос")


if __name__ == "__main__":
    if st.runtime.exists():
        main()
    else:
        sys.argv = ["streamlit", "run", sys.argv[0]]
        sys.exit(stcli.main())
