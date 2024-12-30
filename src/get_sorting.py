import re
from collections import Counter
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


def filter_transactions(transactions: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Функцию принимает список словарей с данными о банковских операциях и строку поиска
    и возвращает список словарей, у которых в описании есть данная строка"""
    try:
        print("Введите слово, по которому будем фильтровать")
        search_string = str(input().lower())
        pattern = re.compile(re.escape(search_string), flags=re.IGNORECASE)
        filtered_transactions = [
            transaction
            for transaction in transactions
            if "description" in transaction and pattern.search(transaction["description"])
        ]
        # if len(filtered_transactions) == 0:
        #     print("Нет операций с заданным описанием")
        return filtered_transactions
    except Exception as e:  # pragma: nocover
        print(type(e).__name__)
        return []


# result = filter_transactions(transactions)
# print(result)


def count_operations_by_category(transactions: List[Dict[str, Any]], categories: List[str]) -> Dict[str, int]:
    """Функция принимает список словарей с данными о банковских операциях и список категорий операций
    и возвращает словарь, в котором ключи — это названия категорий, а значения — это количество операций
     в каждой категории"""
    try:
        category_count: Dict[str, int] = Counter()
        for transaction in transactions:
            description = transaction.get("description", "")
            for category in categories:
                if re.search(re.escape(category), description, flags=re.IGNORECASE):
                    category = transaction["description"]
                    category_count[category] += 1
        if category_count == {}:
            print("Нет операций по заданным категориям")
        return category_count
    except Exception as e:  # pragma: nocover
        print(type(e).__name__)
        return {}


# categories = ["ПЕРЕВОД", "Открытие", "ОПЛАТА"]
# result = count_operations_by_category(transactions, categories)
# print(result)
