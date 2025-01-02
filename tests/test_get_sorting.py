from typing import Any, Dict, List
from unittest.mock import patch

from src.get_sorting import count_operations_by_category, filter_transactions

transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Открытие счета",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    },
]


def test_count_operations_by_category(my_transactions: List[Dict[str, Any]]) -> None:
    """Тестируем функцию, возвращающую словарь, в котором ключи — это названия категорий,
    а значения — это количество операций в каждой категории"""
    categories = ["Перевод организации", "Оплата", "Открытие"]
    assert count_operations_by_category(my_transactions, categories) == {
        "Перевод организации": 1,
        "Оплата организации": 1,
    }
    categories = ["Открытие"]
    assert count_operations_by_category(my_transactions, categories) == {}
    categories = ["ПЕРЕВОД"]
    assert count_operations_by_category(my_transactions, categories) == {
        "Перевод со счета на счет": 2,
        "Перевод с карты на карту": 1,
        "Перевод организации": 1,
    }


@patch("builtins.input")
def test_filter_transactions_no_match(mock_input: Any) -> None:
    """Проверяем случай, когда ни одна транзакция не соответствует искомой строке"""
    mock_input.return_value = "Оплата"
    assert filter_transactions(transactions) == []


@patch("builtins.input")
def test_filter_transactions(mock_input: Any) -> None:
    """Проверяем, что функция возвращает транзакции, в описании которых содержится искомая строка"""
    mock_input.return_value = "Открытие"
    assert filter_transactions(transactions) == [
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Открытие счета",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        }
    ]


@patch("builtins.input")
def test_filter_transactions_register(mock_input: Any) -> None:
    """Проверяем, что что поиск не чувствителен к регистру"""
    mock_input.return_value = "ОТКРЫТИЕ"
    assert filter_transactions(transactions) == [
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Открытие счета",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        }
    ]


@patch("builtins.input")
def test_filter_transactions_empty(mock_input: Any) -> None:
    """Проверяем работу функции при пустом списке"""
    mock_input.return_value = "Открытие"
    empty_transactions: List[Dict[str, Any]] = []
    assert filter_transactions(empty_transactions) == []
