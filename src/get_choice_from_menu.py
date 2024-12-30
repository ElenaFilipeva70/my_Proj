import os
from typing import Any, Dict, List

from src.get_read_transaction import get_read_csv, get_read_excel
from src.processing import filter_by_state
from src.utils import transactions_read


def choice_of_option() -> List[Dict[str, Any]]:
    """Выбор вида файла с транзакциями"""
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path_file_json = os.path.join(base_dir, "data", "operations_test.json")
    path_file_csv = os.path.join(base_dir, "data", "transactions.csv")
    path_file_excel = os.path.join(base_dir, "data", "transactions_excel.xlsx")
    while True:
        print(
            """Выберите необходимый пункт меню:
        1. Получить информацию о транзакциях из JSON-файла
        2. Получить информацию о транзакциях из CSV-файла
        3. Получить информацию о транзакциях из XLSX-файла
        """
        )
        users_choice = str(input())
        if users_choice == "1":
            print("Для обработки выбран JSON-файл.")
            result_list = transactions_read(path_file_json)
            return result_list
        elif users_choice == "2":
            print("Для обработки выбран CSV-файл.")
            result_list = get_read_csv(path_file_csv)
            return result_list
        elif users_choice == "3":
            print("Для обработки выбран XLSX-файл.")
            result_list = get_read_excel(path_file_excel)
            return result_list
        else:
            print(
                """Выбранный Вами пункт недоступен.
            Попробуйте выбрать еще раз.
            """
            )


# result_list = choice_of_option()
# print(result_list)


def choice_state(result_list: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Выбор статуса транзакции для фильтрации"""
    while True:
        print(
            """Введите статус, по которому необходимо выполнить фильтрацию.
        Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING
        """
        )
        users_choice_state = str(input().upper())
        if users_choice_state == "EXECUTED" or users_choice_state == "CANCELED" or users_choice_state == "PENDING":
            result_list = filter_by_state(result_list, users_choice_state)
            if not result_list:
                return result_list
            else:
                print(f'Операции отфильтрованы по статусу "{users_choice_state}"')
                return result_list
        else:
            print(f'Статус операции "{users_choice_state}" недоступен.')
