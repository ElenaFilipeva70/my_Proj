from typing import Any, Dict, List


def filter_by_state(dictionary_operation: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """Функция принимает на вход список словарей с данными о банковских операциях и возвращает
    новый список, содержащий только те словари, у которых ключ содержит переданное в функцию значение."""
    result_dictionary = []
    for operation in dictionary_operation:
        if operation.get("state") == state:
            result_dictionary.append(operation)
    return result_dictionary


def sort_by_date(dictionary_operation: List[Dict[str, Any]], revers: bool = True) -> List[Dict[str, Any]]:
    """Функция принимает на вход список словарей и параметр порядка сортировки, возвращает новый список,
    в котором исходные словари отсортированы по дате."""
    result_dictionary = sorted(dictionary_operation, key=lambda x: x["date"], reverse=revers)
    return result_dictionary
