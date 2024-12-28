import os
import re

from typing import Any, Dict, List

from src.processing import filter_by_state, sort_by_date
from src.utils import transactions_read
from src.get_read_transaction import get_read_csv, get_read_excel
from src.generators import filter_by_currency
from src.get_sorting import filter_transactions
from src.printed_result import printed_transaction


base_dir = os.path.dirname(os.path.abspath(__file__))
path_file_json = os.path.join(base_dir, "data", "operations_test.json")
path_file_csv = os.path.join(base_dir, "data", "transactions.csv")
path_file_excel = os.path.join(base_dir, "data", "transactions_excel.xlsx")
result_list: List[Dict[str, Any]] = []


def main() -> Any:
    """Функция, которая отвечает за основную логику проекта и связывает функциональности между собой"""
    print('Привет! Добро пожаловать в программу работы с банковскими транзакциями. ')

    while True:
        print('''Выберите необходимый пункт меню:
        1. Получить информацию о транзакциях из JSON-файла
        2. Получить информацию о транзакциях из CSV-файла
        3. Получить информацию о транзакциях из XLSX-файла
        ''')
        users_choice = str(input())
        if users_choice == "1":
            print('Для обработки выбран JSON-файл.')
            result_list = transactions_read(path_file_json)
            break
        elif users_choice == "2":
            print('Для обработки выбран CSV-файл.')
            result_list = get_read_csv(path_file_csv)
            break
        elif users_choice == "3":
            print('Для обработки выбран XLSX-файл.')
            result_list = get_read_excel(path_file_excel)
            break
        else:
            print('''Выбранный Вами пункт недоступен.
            Попробуйте выбрать еще раз.
            ''')

    while True:
        print('''Введите статус, по которому необходимо выполнить фильтрацию.
        Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING
        ''')
        users_choice_state = str(input().upper())
        if users_choice_state == "EXECUTED" or users_choice_state == 'CANCELED' or users_choice_state == 'PENDING':
            result_list = filter_by_state(result_list, users_choice_state)
            if not result_list:
                break
            else:
                print(f'Операции отфильтрованы по статусу "{users_choice_state}"')
            break
        else:
            print(f'Статус операции "{users_choice_state}" недоступен.')

    pattern_answer_yes = re.compile(r'^[дy]\D*', flags=re.IGNORECASE)
    pattern_answer_no = re.compile(r'^[нn]\D*', flags=re.IGNORECASE)
    while True:
        if not result_list:
            break
        else:
            print("Отсортировать операции по дате? Да/Нет")
            users_choice_date = str(input().lower())
            if re.search(pattern_answer_yes, users_choice_date):
                while True:
                    print("Отсортировать по возрастанию или по убыванию?")
                    users_choice_sort = str(input().lower())
                    if re.search(r'\bвозр\B', users_choice_sort):
                        result_list = sort_by_date(result_list, revers=False)
                        break
                    elif re.search(r'\bубыв\B', users_choice_sort):
                        result_list = sort_by_date(result_list)
                        break
                    else:
                        print("Вы ввели некорректный ответ")
                        continue
                break
            elif re.search(pattern_answer_no, users_choice_date):
                break
            else:
                print("Вы ввели некорректный ответ")

    while True:
        if not result_list:
            break
        else:
            print("Выводить только рублевые транзакции? Да/Нет")
            users_choice_currency = str(input().lower())
            if re.search(pattern_answer_yes, users_choice_currency):
                result_list = list(filter_by_currency(result_list, "RUB"))
                break
            elif re.search(pattern_answer_no, users_choice_currency):
                break
            else:
                print("Вы ввели некорректный ответ")
                continue

    while True:
        if not result_list:
            break
        else:
            print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
            users_choice_filter = str(input().lower())
            if re.search(pattern_answer_yes, users_choice_filter):
                result_list = filter_transactions(result_list)
                break
            elif re.search(pattern_answer_no, users_choice_filter):
                break
            else:
                print("Вы ввели некорректный ответ")
                continue

    print("Распечатываю итоговый список транзакций...")
    printed_transaction(result_list)


main()

# name_card = "Visa Platinum 8990 9221 1366 5229"
# name_card_mask = mask_account_card(name_card)
# print(name_card_mask)
# num_check = "Счет 73654 10843 01358 74305"
# num_check_mask = mask_account_card(num_check)
# print(num_check_mask)
# new_string_date = get_date("2024/03/11T02:26:18.671407")
# print("Дата", new_string_date)

# dictionary_operation = [
#     {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#     {"id": 939719570, "state": "EXECUTED", "date": "30 декабря 2018-06-30T02:08:58.425572"},
#     {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#     {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
# ]

# print(filter_by_state(dictionary_operation))
# state = "CANCELED"
# print(filter_by_state(dictionary_operation, state))
# print(sort_by_date(dictionary_operation))
# revers = False
# print(sort_by_date(dictionary_operation, revers))
