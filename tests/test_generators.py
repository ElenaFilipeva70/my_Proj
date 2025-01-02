from typing import Any, Dict, List

import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency(my_transactions: List[Dict[str, Any]]) -> None:
    generator = filter_by_currency(my_transactions, "USD")
    assert next(generator) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Оплата организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }
    assert next(generator) == {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }
    assert next(generator) == {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    }
    with pytest.raises(StopIteration):
        assert next(filter_by_currency(my_transactions, "Рубли"))


def test_filter_by_currency_invalid(my_transactions_invalid: List[Dict[str, Any]]) -> None:
    assert next(filter_by_currency(my_transactions_invalid, "USD")) == "Нет данных для анализа"


def test_transaction_descriptions(my_transactions: List[Dict[str, Any]]) -> None:
    generator = transaction_descriptions(my_transactions)
    assert next(generator) == "Оплата организации"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Перевод с карты на карту"
    assert next(generator) == "Перевод организации"


def test_transaction_descriptions_invalid(my_transactions_invalid: List[Dict[str, Any]]) -> None:
    assert next(transaction_descriptions(my_transactions_invalid)) == "Нет данных для анализа"


@pytest.mark.parametrize(
    "start, stop, expected",
    [
        (9999999999999997, 9999999999999999, ["9999 9999 9999 9997", "9999 9999 9999 9998", "9999 9999 9999 9999"]),
        (
            1,
            5,
            [
                "0000 0000 0000 0001",
                "0000 0000 0000 0002",
                "0000 0000 0000 0003",
                "0000 0000 0000 0004",
                "0000 0000 0000 0005",
            ],
        ),
        (9999999999999999, 9999999999999997, [""]),
        (9999999999999999, 99999999999999991, [""]),
        (99999999999999991, 999999999999999923, [""]),
    ],
)
def test_card_number_generator(start: int, stop: int, expected: str) -> None:
    card_number = card_number_generator(start, stop)
    for exp in expected:
        assert next(card_number) == exp


@pytest.mark.parametrize(
    "start, stop, expected", [(9999999999999999, 9999999999999997, [""]), (9999999999999999, 99999999999999991, [""])]
)
def test_card_number_generator_invalid(start: int, stop: int, expected: str) -> None:
    card_number = card_number_generator(start, stop)
    for exp in expected:
        assert next(card_number) == exp
