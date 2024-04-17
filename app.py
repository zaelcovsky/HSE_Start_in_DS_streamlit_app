import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Custom CSS для размера шрифта
st.sidebar.markdown("""
    <style>
    .custom-font {
        font-size:14px !important;
    }
    </style>
    """,
    unsafe_allow_html=True)

# Заголовок
st.write(
    """
    ## Медали Олимпийских игр 1896-2016 гг 
    ###  
    """
)

# Картинка
image_path = str(Path("data/logo.png"))
st.image(image_path)

# Текст
st.markdown(
    """
    ###  
    В приложении использован датасет [120 years of Olympic history: athletes and results](https://www.kaggle.com/datasets/heesoo37/120-years-of-olympic-history-athletes-and-results/data).   
    Датасет содержит информацию об атлетах, видах спорта и выигранных медалях с Олимпийских игр 1896-2016 гг. 
    Приложение позволяет проанализировать количество выигранных атлетами медалей в разрезе страны, пола атлетов и вида медали (бронза, серебро, золото).
    """
)

# Загрузка данных
athletes = st.cache_data(pd.read_csv)("data/athlete_events.csv")

# Датасет
with st.expander("Датасет Олимпийских игр 1896-2016 гг (первые 200 строк)"):
    # st.dataframe(athletes.head().style.format(hide_index=True))
    st.dataframe(athletes.head(200), hide_index=True)

# Multiselect widget
countries = st.sidebar.multiselect(
    'Выберите страну',
    athletes['Team'].unique()
)

# toggle widgets
st.sidebar.markdown('<p class="custom-font">Выберите пол</p>', unsafe_allow_html=True)
sex = []
sex_m = st.sidebar.toggle(
    'Мужчины'
)
if sex_m:
    sex.append("M")

sex_f = st.sidebar.toggle(
    'Женщины'
)
if sex_f:
    sex.append("F")

# checkbox widgets
st.sidebar.markdown('<p class="custom-font">Выберите тип медали</p>', unsafe_allow_html=True)
medals = []
medals_gold = st.sidebar.checkbox(
    'Золотые медали',
)
if medals_gold:
    medals.append("Gold")

medals_silver = st.sidebar.checkbox(
    'Серебряные медали',
)
if medals_silver:
    medals.append("Silver")

medals_bronze = st.sidebar.checkbox(
    'Бронзовые медали',
)
if medals_bronze:
    medals.append("Bronze")

# Подзаголовок
st.markdown(
    """
    ##### Количество медалей по годам
    """
)


_button = st.sidebar.button("Показать", type="primary")

# кнопка и подсчет медалей
if _button:
    filtered = athletes[
        athletes['Team'].isin(countries) & (athletes['Medal'].isin(medals)) & (athletes['Sex'].isin(sex))]
    count_by_year = filtered.groupby('Year', as_index=False)['Name'].count().sort_values('Year')

    # Отображаем датафрейм в виде таблицы
    count_by_year_transposition = count_by_year.rename(columns={"Name": "Количество медалей", "Year": "Год"}).T
    st.dataframe(count_by_year_transposition.style.format({
        "Год": "{}",  # Show no formatting
        "Количество медалей": "{}"
    }))

    # Построение столбчатой диаграммы
    x = count_by_year["Year"]
    y = count_by_year["Name"]

    plt.figure(figsize=(25, 5))
    plt.bar(x, y, color='gold')

    # Название всего графика
    # plt.title('Количество медалей по годам')

    # Подпись каждой из осей
    plt.xlabel('Годы')
    plt.ylabel('Количество медалей')

    xmarks = range(1896, 2016, 1)
    plt.xticks(xmarks, fontsize=9)
    # ymarks = range(0, 230, 10)
    # plt.yticks(ymarks)
    plt.xticks(rotation=90)

    # добавим значения на каждый столбец
    for i in range(len(y)):
        plt.annotate(str(y[i]), xy=(x[i], y[i]), ha='center', va='bottom')

    # Отображаем график
    st.pyplot(plt)

else:
    st.write('Выберите параметры для показа графика')
