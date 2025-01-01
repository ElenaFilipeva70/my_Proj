from typing import Any, Dict, List
from unittest.mock import patch

from _pytest.capture import CaptureFixture

from src.get_printed_result import printed_transaction


def test_printed_transaction_empty(capsys: CaptureFixture[str]) -> None:
    result_transaction: List[Dict[str, Any]] = []
    printed_transaction(result_transaction)
    captured = capsys.readouterr()
    assert captured.out == "Не найдено ни одной транзакции, подходящей под ваши условия фильтрации\n"


def test_printed_transaction_json(capsys: CaptureFixture[str]) -> None:
    """Проверка печати результата выбора транзакций из JSON-файла"""
    result_transaction = [
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
        {
            "id": 587085106,
            "state": "EXECUTED",
            "date": "2018-03-23T10:45:06.972075",
            "operationAmount": {"amount": "48223.05", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Открытие вклада",
            "to": "Счет 41421565395219882431",
        },
    ]
    with patch("builtins.input"):
        printed_transaction(result_transaction)
        captured = capsys.readouterr()
        assert captured.out == (
            "Всего банковских операций в выборке: 2\n"
            "12.09.2018 Перевод организации\n"
            "Visa Platinum 1246 37** **** 3588 -> Счет **1657\n"
            "Сумма: 67314.70 руб.\n"
            "23.03.2018 Открытие вклада\n"
            "Счет **2431\n"
            "Сумма: 48223.05 руб.\n"
        )


def test_printed_transaction_csv_xls(capsys: CaptureFixture[str]) -> None:
    """Проверка печати результата выбора транзакций из CSV-файла"""
    result_transaction = [
        {
            "id": 5380041,
            "state": "CANCELED",
            "date": "2021-02-01T11:54:58.Z",
            "amount": "23789",
            "currency_name": "Peso",
            "currency_code": "UYU",
            "from": "",
            "to": "Счет 23294994494356835683",
            "description": "Открытие вклада",
        },
        {
            "id": 4234093,
            "state": "EXECUTED",
            "date": "2021-07-08T07:31:21.Z",
            "amount": "23182",
            "currency_name": "Ruble",
            "currency_code": "RUB",
            "from": "Visa 0773092093872450",
            "to": "Discover 8602781449570491",
            "description": "Перевод с карты на карту",
        },
    ]
    with patch("builtins.input"):
        printed_transaction(result_transaction)
        captured = capsys.readouterr()
        assert captured.out == (
            "Всего банковских операций в выборке: 2\n"
            "01.02.2021 Открытие вклада\n"
            "Счет **5683\n"
            "Сумма: 23789 UYU\n"
            "08.07.2021 Перевод с карты на карту\n"
            "Visa 0773 09** **** 2450 -> Discover 8602 78** **** 0491\n"
            "Сумма: 23182 руб.\n"
        )
