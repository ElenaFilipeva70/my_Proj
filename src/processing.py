from typing import Any, Dict, List

from src.widget import get_date


def filter_by_state(dictionary_operation: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """Функция принимает на вход список словарей с данными о банковских операциях и возвращает
    новый список, содержащий только те словари, у которых ключ содержит переданное в функцию значение."""
    result_dictionary = []
    for operation in dictionary_operation:
        if operation.get("state") == state:
            result_dictionary.append(operation)
    # if result_dictionary == []:
    #    print("Операций с выбранным статусом не найдено")
    return result_dictionary


def sort_by_date(dictionary_operation: List[Dict[str, Any]], revers: bool = True) -> List[Dict[str, Any]]:
    """Функция принимает на вход список словарей и параметр порядка сортировки, возвращает новый список,
    в котором исходные словари отсортированы по дате."""
    new_dictionary_operation = []
    for operation in dictionary_operation:
        string_date = str(operation.get("date"))
        string_date_format = get_date(string_date)
        if string_date_format != "Неверный формат данных":
            new_dictionary_operation.append(operation)
    result_dictionary = sorted(new_dictionary_operation, key=lambda x: x["date"], reverse=revers)
    # print(result_dictionary)
    return result_dictionary
