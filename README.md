![Python Versions](https://img.shields.io/badge/python-3.10--3.11-blue)
![Streamlit version](https://img.shields.io/badge/streamlit-1.33.0-white)
![License](https://img.shields.io/github/license/blackary/st_pages)  
  
[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://hse-start-in-ds-app.streamlit.app/)

# Приложение на основе фреймворка Streamlit

В приложении использован датасет [120 years of Olympic history: athletes and results](https://www.kaggle.com/datasets/heesoo37/120-years-of-olympic-history-athletes-and-results/data).   
Датасет содержит информацию об атлетах, видах спорта и выигранных медалях с Олимпийских игр 1896-2016 гг. Файл ```athlete_events.csv``` содержит 271116 строк и 15 столбцов. 
Каждая строка соответствует отдельному спортсмену, участвующему в отдельных олимпийских соревнованиях.
Приложение позволяет проанализировать количество выигранных атлетами медалей в разрезе страны, пола атлетов и вида медали (бронза, серебро, золото).  
 ```streamlit``` приложение задеплоено на [Streamlit Community Cloud](https://hse-start-in-ds-app.streamlit.app/).  
Для запуска проекта локально:  
1) Клонируем проект
```shell
git clone https://github.com/zaelcovsky/HSE_Start_in_DS_streamlit_app.git
```
2) Устанавливаем необходимые зависимости
```shell
pip install -r requirements.txt
```
3) Запускаем ```streamlit``` приложениe
```shell
streamlit run app.py
```  
##  
Студент Черепанов С.Ю.