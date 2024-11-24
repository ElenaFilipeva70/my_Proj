from collections.abc import Iterator
from typing import Any, Dict, List

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
        "description": "Перевод со счета на счет",
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


def filter_by_currency(transactions_list: List[Dict[str, Any]], currency: str) -> Any:
    """Функция возвращает транзакции по заданному значению валюты"""
    if transactions_list == []:
        yield "Нет данных для анализа"
    else:
        for transaction in transactions_list:
            if transaction["operationAmount"]["currency"]["code"] == currency:
                yield transaction


if __name__ == "__main__":
    usd_transactions = filter_by_currency(transactions, "USD")
    try:
        for _ in range(3):
            print(next(usd_transactions))
    except StopIteration:
        print("Нет операций в заданной валюте")


def transaction_descriptions(transactions_list: List[Dict[str, Any]]) -> Any:
    if transactions_list == []:
        yield "Нет данных для анализа"
    else:
        for transaction in transactions_list:
            name_operation = transaction["description"]
            yield name_operation


if __name__ == "__main__":
    descriptions = transaction_descriptions(transactions)
    try:
        for _ in range(5):
            print(next(descriptions))
    except StopIteration:
        print("Конец операций")


def card_number_generator(start: int, stop: int) -> Any:
    if len(str(start)) > 16 or len(str(stop)) > 16 or start > stop:
        yield ""
    else:
        for i in range(start, stop + 1):
            card_number_code = "0" * (16 - len(str(i))) + str(i)
            number_card = list(card_number_code[x * 4 : (x + 1) * 4] for x in range(4))
            yield " ".join(number_card)


for card_number in card_number_generator(1, 5):
    print(card_number)
