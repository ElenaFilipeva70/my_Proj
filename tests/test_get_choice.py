from unittest.mock import patch

from _pytest.capture import CaptureFixture

from src.get_choice import choice_currency, choice_date_sorting_direction, choice_filter

test_transactions = [{"id": 1, "description": "Тестовая транзакция"}]


@patch("src.get_choice.sort_by_date")
def test_choice_date_sorting_direction_yes(mock_sort_by_date, capsys: CaptureFixture[str]) -> None:
    """Тестируем положительный выбор сортировки транзакций по дате и выбор направления сортировки"""
    with patch("builtins.input", side_effect=["Да", "по убыванию", "по возрастанию"]):
        mock_sort_by_date.return_value = test_transactions
        result = choice_date_sorting_direction(test_transactions)
        captured = capsys.readouterr()
        assert "Отсортировать по возрастанию или по убыванию?" in captured.out
        assert result == test_transactions


@patch("src.get_choice.sort_by_date")
def test_choice_date_sorting_direction_other(mock_sort_by_date, capsys: CaptureFixture[str]) -> None:
    """Тестируем положительный выбор сортировки транзакций по дате и выбор направления сортировки,
    проверяя ввод на английском и в верхнем регистре"""
    with patch("builtins.input", side_effect=["YES", "fake", "ПО ВОЗРАСТАНИЮ"]):
        mock_sort_by_date.return_value = test_transactions
        result = choice_date_sorting_direction(test_transactions)
        captured = capsys.readouterr()
        assert "Отсортировать по возрастанию или по убыванию?" in captured.out
        assert "Вы ввели некорректный ответ" in captured.out
        assert "Отсортировать по возрастанию или по убыванию?" in captured.out
        assert result == test_transactions


def test_choice_date_sorting_direction_no(capsys: CaptureFixture[str]) -> None:
    """Тестируем отказ от сортировки транзакций по дате, проверяя некорректный ответ пользователя и
    ввод на английском языке и в верхнем регистре"""
    with patch("builtins.input", side_effect=["fake", "нет", "NO"]):
        result = choice_date_sorting_direction(test_transactions)
        captured = capsys.readouterr()
        assert "Отсортировать операции по дате? Да/Нет" in captured.out
        assert "Вы ввели некорректный ответ" in captured.out
        assert "Отсортировать операции по дате? Да/Нет" in captured.out
        assert result == test_transactions


def test_choice_currency_no(capsys: CaptureFixture[str]) -> None:
    """Тестируем отказ от выбора валюты транзакций для вывода, проверяя некорректный ответ пользователя и
    ввод на английском языке и в верхнем регистре"""
    with patch("builtins.input", side_effect=["fake", "нет", "NO"]):
        result = choice_currency(test_transactions)
        captured = capsys.readouterr()
        assert "Выводить только рублевые транзакции? Да/Нет" in captured.out
        assert "Вы ввели некорректный ответ" in captured.out
        assert "Выводить только рублевые транзакции? Да/Нет" in captured.out
        assert result == test_transactions


@patch("src.get_choice.filter_by_currency")
def test_choice_currency_yes(mock_filter_by_currency) -> None:
    """Тестируем выбор валюты транзакций для вывода, проверяя ввод на английском языке и в верхнем регистре"""
    with patch("builtins.input", side_effect=["Да", "YES"]):
        mock_filter_by_currency.return_value = test_transactions
        result = choice_currency(test_transactions)
        assert result == test_transactions


@patch("src.get_choice.filter_transactions")
def test_choice_filter_yes(mock_filter_transactions) -> None:
    """Тестируем выбор описания операции транзакции для сортировки,
    проверяя ввод на английском языке и в верхнем регистре"""
    with patch("builtins.input", side_effect=["Да", "YES"]):
        mock_filter_transactions.return_value = test_transactions
        result = choice_filter(test_transactions)
        assert result == test_transactions


def test_choice_filter_no(capsys: CaptureFixture[str]) -> None:
    """Тестируем отказ от выбора описания операции транзакции для сортировки,
    проверяя некорректный ответ пользователя и ввод на английском языке и в верхнем регистре"""
    with patch("builtins.input", side_effect=["fake", "нет", "NO"]):
        result = choice_filter(test_transactions)
        captured = capsys.readouterr()
        assert "Отфильтровать список транзакций по определенному слову в описании? Да/Нет" in captured.out
        assert "Вы ввели некорректный ответ" in captured.out
        assert "Отфильтровать список транзакций по определенному слову в описании? Да/Нет" in captured.out
        assert result == test_transactions
