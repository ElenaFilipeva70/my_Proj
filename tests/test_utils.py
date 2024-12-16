from unittest.mock import patch

from src.utils import transactions_read


@patch("json.load")
@patch("builtins.open", create=True)
def test_transactions_read(mock_open, mock_json) -> None:
    """Проверяем работу функции на открытие файла"""
    mock_json.return_value = [{"key": "value"}]
    assert transactions_read("test.txt") == [{"key": "value"}]
    mock_open.assert_called_once_with("test.txt", "r", encoding="utf-8")


def test_transactions_read_not_lict() -> None:
    """Проверяем работу функции, если в файле не список"""
    result = transactions_read("data/operations_any.json")
    assert result == []


def test_transactions_read_empty() -> None:
    """Проверяем работу функции, если файл пустой"""
    result = transactions_read("data/operations_empty.json")
    assert result == []


def test_transactions_read_not_found() -> None:
    """Проверяем работу функции, если файл не найден"""
    result = transactions_read("data/operations_empty1.json")
    assert result == []
