from typing import Any
from unittest.mock import patch

from src.external_api import conversions_get, get_convert_info


@patch("requests.get")
def test_get_convert_info(mock_get) -> None:
    """Проверяем завершение обработки запроса к внешнему API"""
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"amount": 8221.37, "rate": 104.007477, "result": 855083.951183}
    assert get_convert_info(8221.37, "USD") == {"amount": 8221.37, "rate": 104.007477, "result": 855083.951183}
    mock_get.assert_called_once()


@patch("requests.get")
def test_get_convert_info_invalid(mock_get) -> None:
    """Проверка некорректного завершения обработки запроса к внешнему API"""
    mock_get.return_value.status_code = 404
    mock_get.return_value.json.return_value = {}
    assert get_convert_info(8221.37, "USD") == {}
    mock_get.assert_called_once()


def test_conversions_get_RUB(transaction_RUB: dict[str, Any]) -> None:
    """Проверка работы функции, когда транзакция в рублях"""
    assert conversions_get(transaction_RUB) == 67314.70


@patch("requests.get")
def test_conversions_get_USD(mock_get) -> None:
    """Проверка корректной работы функции, когда транзакция в валюте USD"""
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"amount": 8221.37, "rate": 104.007477, "result": 855083.951183}
    transaction_USD = {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {"amount": "8221.37", "currency": {"name": " USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560",
    }
    assert conversions_get(transaction_USD) == 855083.9512
    mock_get.assert_called_once()


@patch("requests.get")
def test_conversions_get_invalid(mock_get) -> None:
    """Проверка работы функции, когда возникло исключение"""
    mock_get.return_value.status_code = 400
    mock_get.return_value.json.return_value = {}
    transaction_USD = {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {"amount": "8221.37", "currency": {"name": " USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560",
    }
    assert conversions_get(transaction_USD) == None
    mock_get.assert_called_once()
