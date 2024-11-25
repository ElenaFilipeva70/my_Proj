# Проект "Мой банк"
## Описание. 
   Мой банк - это новая фича для личного кабинета клиента - это виджет, который показывает
   несколько последних успешных банковских операций клиента.
   

## Требования к окружению
  На вашем компьютере должна быть установлена следующая версияи Python:
    ```
     Python 3.12.7+
    ```
## Установка проекта 
  - Склонировать репозиторий. Для этого набарать следующую команду:
    ```
    git clone https://github.com/ElenaFilipeva70/my_Proj
    ```
  - Перейти в директорию проекта:
    ```
    cd my_Proj
    ```
  - Создать и активировать виртуальное окружение:
    ```
    python -m venv .env

    .env\Scripts\activate 
    ```
## Установка зависимостей:
    
    poetry install

## Как запустить проект:
```
  python main.py   
```
## Использование

Этот проект готовит данные для отображения в новом виджете: 
 - выводит тип и номер карты или счета, используя типы маскировок;
 - выводит список операций по выбранному статусу;
 - сортирует операции по дате (по возрастанию или убыванию).

В проекте предусмотрены проверки на некорректность входных данных:
- проверка работы функции маскировки номера банковской карты на различных входных
  форматах номеров карт, включая граничные случаи и нестандартные длины номеров,
  проверка, что функция корректно обрабатывает входные строки, где отсутствует
  номер карты;
- проверка работы функции маскировки номера банковского счета с различными форматами 
  и длинами номеров счетов, проверка, что функция корректно обрабатывает входные данные, 
  где номер счета меньше ожидаемой длины;
- проверка, что корректно распознается и применяется нужный тип маскировки в зависимости 
  от типа входных данных (карта или счет);
- проверка работы функции обработки даты операции на различных входных форматах даты, 
  включая некорректные и нестандартные форматы дат, проверка, что функция корректно 
  обрабатывает входные строки, где отсутствует дата;
- проверка работы функции фильтрации списка операций по заданному статусу операции при
  отсутствии в списке операций операции с указанным статусом;
- проверка корректности работы функции сортировки списка операций по датам в порядке
  убывания или возрастания при одинаковых датах, проверка на работу функции с некорректными
  или нестандартными форматами дат.

 Для эффективной работы с большими объемами данных транзакций используя возможности Python
 созданы инструменты для обработки данных через генераторы. Эти генераторы должны позволять 
 финансовым аналитикам быстро и удобно находить нужную информацию о транзакциях и проводить 
 анализ данных. Все новые функции, реализующие генераторы для обработки данных, находятся
 в одном модуле generators. В настоящий момент их три:
- функция *filter_by_currency*, которая принимает на вход список словарей, представляющих 
  транзакции. Возвращает итератор, который поочередно выдает транзакции, где валюта операции 
  соответствует заданной (например, USD);
- генератор *transaction_descriptions*, который принимает список словарей с транзакциями и 
  возвращает описание каждой операции по очереди;
- генератор *card_number_generator*, который выдает номера банковских карт в формате 
  XXXX XXXX XXXX XXXX, где X — цифра номера карты. Генератор может сгенерировать номера 
  карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999.


## Лицензия:

Данный проект лицензирован в соответствии с условиями лицензии MIT 
