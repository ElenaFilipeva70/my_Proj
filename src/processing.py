from typing import Any, Dict, List


def filter_by_state(bank_operation: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """Функция принимает на вход список словарей с данными о банковских операциях и возвращает
    новый список, содержащий только те словари, у которых ключ  содержит переданное в функцию значение."""
    result_diction = []
    for operation in bank_operation:
        if operation.get("state") == state:
            result_diction.append(operation)
    return result_diction


def sort_by_date(bank_operation_sort: List[Dict[str, Any]], sort_order: bool = True) -> List[Dict[str, Any]]:
    """Функция принимает на вход список словарей и параметр порядка сортировки, возвращает новый список,
    в котором исходные словари отсортированы по дате."""
    result_diction = sorted(bank_operation_sort, key=lambda operation: operation["date"], reverse=sort_order)
    return result_diction
