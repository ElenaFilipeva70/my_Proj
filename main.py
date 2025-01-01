from typing import Any, Dict, List

from src.get_choice import choice_currency, choice_date_sorting_direction, choice_filter
from src.get_choice_from_menu import choice_of_option, choice_state
from src.get_printed_result import printed_transaction


def main() -> Any:
    """Функция, которая отвечает за основную логику проекта и связывает функциональности между собой"""
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями. ")
    result_list: List[Dict[str, Any]] = []
    result_list = choice_of_option()
    result_list = choice_state(result_list)
    result_list = choice_date_sorting_direction(result_list)
    result_list = choice_currency(result_list)
    result_list = choice_filter(result_list)
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
