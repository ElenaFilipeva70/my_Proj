from unittest.mock import patch

import pandas as pd

from src.get_read_transaction import get_read_csv, get_read_excel


@patch("pandas.read_csv")
def test_get_read_csv(mock_read_csv) -> None:
    """Тестируем чтение CSV-файла"""
    transaction_dict = {"key1": ["value1", "value2"], "key2": ["value1", "value2"]}
    mock_read_csv.return_value = pd.DataFrame(transaction_dict)
    assert get_read_csv("test.csv") == [{"key1": "value1", "key2": "value1"}, {"key1": "value2", "key2": "value2"}]
    mock_read_csv.assert_called_once()


@patch("pandas.read_excel")
def test_get_read_excel(mock_read_excel) -> None:
    """Тестируем чтение EXCEL-файла"""
    transaction_dict = {"key1": ["value1", "value2"], "key2": ["value1", "value2"]}
    mock_read_excel.return_value = pd.DataFrame(transaction_dict)
    assert get_read_excel("test.xlsx") == [{"key1": "value1", "key2": "value1"}, {"key1": "value2", "key2": "value2"}]
    mock_read_excel.assert_called_once()


def test_get_read_csv_empty() -> None:
    """Проверяем работу функции, если файл пустой"""
    result = get_read_csv("data/orders.csv")
    assert result == []


def test_get_read_excel_empty() -> None:
    """Проверяем работу функции, если файл пустой"""
    result = get_read_excel("data/orders_empty.xlsx")
    assert result == []


def test_get_read_csv_not_found() -> None:
    """Проверяем работу функции, если файл не найден"""
    result = get_read_csv("data/orders1.csv")
    assert result == []


def test_get_read_excel_not_found() -> None:
    """Проверяем работу функции, если файл не найден"""
    result = get_read_excel("data/orders_empty1.xlsx")
    assert result == []
