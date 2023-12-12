import time
import streamlit as st
import pandas as pd
from PIL import Image


def preload_content():
    """ preload content used in web app """

    all = Image.open('img/all_to_all.png')
    corr = Image.open('img/corr.png')
    hist = Image.open('img/hist.png')
    pie = Image.open('img/pie.png')
    table = Image.open('img/table.png')

    return all, corr, hist, pie, table



def render_page(all, corr, hist, pie, table):
    """ creates app page with tabs """

    st.title('EDA')
    st.subheader('Исследуем данные')
    st.write('Материал - данные клиентов банка')
    st.write('Зависимость числовых признаков друг от друга')
    st.image(all)
    st.write('Корреляции числовых признаков')
    st.image(corr)
    st.write('Распределение числовых признаков')
    st.image(hist)
    st.write('Статистики числовых признаков')
    st.image(table)
    st.write('Распределение категориальных признаков')
    st.image(pie)
    


def load_page():
    """ loads main page """

    all, corr, hist, pie, table = preload_content()

    st.set_page_config(layout="wide",
                       page_title="Банка EDA",
                       page_icon=':chart_with_upwards_trend:')

    render_page(all, corr, hist, pie, table)


if __name__ == "__main__":
    load_page()