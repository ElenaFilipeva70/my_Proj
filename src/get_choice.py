import re
from typing import Any, Dict, List

from src.generators import filter_by_currency
from src.get_sorting import filter_transactions
from src.processing import sort_by_date

pattern_answer_yes = re.compile(r"^[дy]\D*", flags=re.IGNORECASE)
pattern_answer_no = re.compile(r"^[нn]\D*", flags=re.IGNORECASE)


def choice_date_sorting_direction(result_list: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Выбор сортировки транзакций по дате"""
    while True:
        if not result_list:
            return result_list
        else:
            print("Отсортировать операции по дате? Да/Нет")
            users_choice_date = str(input().lower())
            if re.search(pattern_answer_yes, users_choice_date):
                while True:
                    print("Отсортировать по возрастанию или по убыванию?")
                    users_choice_sort = str(input().lower())
                    if re.search(r"\bвозр\B", users_choice_sort):
                        result_list = sort_by_date(result_list, revers=False)
                        return result_list
                    elif re.search(r"\bубыв\B", users_choice_sort):
                        result_list = sort_by_date(result_list)
                        return result_list
                    else:
                        print("Вы ввели некорректный ответ")
                        continue
            elif re.search(pattern_answer_no, users_choice_date):
                return result_list
            else:
                print("Вы ввели некорректный ответ")


def choice_currency(result_list: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Выбор валюты транзакций для вывода"""
    while True:
        if not result_list:
            return result_list
        else:
            print("Выводить только рублевые транзакции? Да/Нет")
            users_choice_currency = str(input().lower())
            if re.search(pattern_answer_yes, users_choice_currency):
                result_list = list(filter_by_currency(result_list, "RUB"))
                return result_list
            elif re.search(pattern_answer_no, users_choice_currency):
                return result_list
            else:
                print("Вы ввели некорректный ответ")
                continue


def choice_filter(result_list: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Выбор описания операции транзакции для сортировки"""
    while True:
        if not result_list:
            return result_list
        else:
            print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
            users_choice_filter = str(input().lower())
            if re.search(pattern_answer_yes, users_choice_filter):
                result_list = filter_transactions(result_list)
                return result_list
            elif re.search(pattern_answer_no, users_choice_filter):
                return result_list
            else:
                print("Вы ввели некорректный ответ")
                continue
