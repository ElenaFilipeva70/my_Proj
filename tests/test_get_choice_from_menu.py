from unittest.mock import patch

from _pytest.capture import CaptureFixture

from src.get_choice_from_menu import choice_of_option, choice_state

test_transactions = [{"id": 1, "description": "Тестовая транзакция"}]


@patch("src.get_choice_from_menu.transactions_read")
def test_choice_of_option_json(mock_transactions_read, capsys: CaptureFixture[str]) -> None:
    """Тестируем выбор пункта №1 - JSON-файла"""
    with patch("builtins.input", side_effect=["1"]):
        mock_transactions_read.return_value = test_transactions
        result = choice_of_option()
        captured = capsys.readouterr()
        assert "Для обработки выбран JSON-файл." in captured.out
        assert result == test_transactions


@patch("src.get_choice_from_menu.get_read_csv")
def test_choice_of_option_csv(mock_get_read_csv, capsys: CaptureFixture[str]) -> None:
    """Тестируем выбор пункта №2 - CSV-файла"""
    with patch("builtins.input", side_effect=["2"]):
        mock_get_read_csv.return_value = test_transactions
        result = choice_of_option()
        captured = capsys.readouterr()
        assert "Для обработки выбран CSV-файл." in captured.out
        assert result == test_transactions


@patch("src.get_choice_from_menu.get_read_excel")
def test_choice_of_option_excel(mock_get_read_excel, capsys: CaptureFixture[str]) -> None:
    """Тестируем выбор пункта №3 - XLSX-файла"""
    with patch("builtins.input", side_effect=["3"]):
        mock_get_read_excel.return_value = test_transactions
        result = choice_of_option()
        captured = capsys.readouterr()
        assert "Для обработки выбран XLSX-файл." in captured.out
        assert result == test_transactions


@patch("src.get_choice_from_menu.get_read_csv")
def test_choice_of_option_invalid(mock_get_read_csv, capsys: CaptureFixture[str]) -> None:
    """Тестируем выбор сначала недоступного пункта, а потом выбор пункта из списка"""
    with patch("builtins.input", side_effect=["4", "2"]):
        mock_get_read_csv.return_value = test_transactions
        result = choice_of_option()
        captured = capsys.readouterr()
        assert "Выбранный Вами пункт недоступен." in captured.out
        assert "Попробуйте выбрать еще раз." in captured.out
        assert "Для обработки выбран CSV-файл." in captured.out
        assert result == test_transactions


@patch("src.get_choice_from_menu.filter_by_state")
def test_choice_state_executed(mock_filter_by_state, capsys: CaptureFixture[str]) -> None:
    """Тестируем выбор статуса транзакции для фильтрации"""
    with patch("builtins.input", side_effect=["EXECUTED"]):
        mock_filter_by_state.return_value = test_transactions
        result = choice_state(test_transactions)
        captured = capsys.readouterr()
        assert 'Операции отфильтрованы по статусу "EXECUTED"' in captured.out
        assert result == test_transactions


@patch("src.get_choice_from_menu.filter_by_state")
def test_choice_state_canceled(mock_filter_by_state, capsys: CaptureFixture[str]) -> None:
    """Тестируем выбор статуса транзакции для фильтрации, включая независимый от регистра ввод"""
    with patch("builtins.input", side_effect=["canceled"]):
        mock_filter_by_state.return_value = test_transactions
        result = choice_state(test_transactions)
        captured = capsys.readouterr()
        assert 'Операции отфильтрованы по статусу "CANCELED"' in captured.out
        assert result == test_transactions


@patch("src.get_choice_from_menu.filter_by_state")
def test_choice_state_other(mock_filter_by_state, capsys: CaptureFixture[str]) -> None:
    """Тестируем выбор статуса транзакции для фильтрации, включая ввод отсутствующего статуса"""
    with patch("builtins.input", side_effect=["fake", "PENDING"]):
        mock_filter_by_state.return_value = test_transactions
        result = choice_state(test_transactions)
        captured = capsys.readouterr()
        assert 'Статус операции "FAKE" недоступен.' in captured.out
        assert 'Операции отфильтрованы по статусу "PENDING"' in captured.out
        assert result == test_transactions
