# Project "Ростелеком"

Объект тестирования: https://b2c.passport.rt.ru


## Для написания автотестов были использованы:
1. Язык программирования Python3
1. Библиотеки PyTest , PyTest - Selenium
1. Паттерн PageObject
1. Фреймворк Smart Page Object

## Файлы проекта:
1. Каталог /pages:
   - auth_page.py – содержит класс с элементами страницы авторизации 
   - reg_page.py – содержит класс с элементами страницы регистрации
   - base.py – содержит базовый класс с методами для работы со страницей

2. Каталог /tests:
    - test_auth_page.py – содержит тесты для страницы авторизации 
    - test_reg_page.py – содержит тесты для страницы регистрации
4. config_data.py – содержит информационные данные

## Запуск тестов.
### 1. Установить requirements:
```
pip3 install -r requirements.txt
```
### 2. Скачать [драйвер](https://chromedriver.chromium.org/downloads) для вашей версии браузера 
### 3. Запустить тесты:
````
pytest -v --driver Chrome --driver-path ~/chromedriver_win32 tests
      или
python -m pytest -v --driver Chrome --driver-path ~/chromedriver_win32 tests, где chromedriver_win32 – это скачанный и разархивированный драйвер
````
## Дополнительные данные по проекту:
1. Набор [тест-кейсов](https://docs.google.com/spreadsheets/d/1zRXpnPNiM4QDknA2dJyZIoBia4zbgUWhdU8tjgbKvW0/edit?usp=sharing)
2. Баг-репорты