import json, os
import random
from typing import Any, Optional
from src.external_api import conversions_get


def transactions_read(path_file: Optional[str]) -> list[Any]:
    """ Функция, которая принимает на вход путь до JSON-файла и возвращает список словарей с данными
     о финансовых транзакциях."""
    try:
        with open(path_file, "r", encoding="utf-8") as json_file:
            transactions_list = json.load(json_file)
    except Exception as e:
        print(type(e).__name__)
        return []
    else:
        return transactions_list


base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path_file = os.path.join(base_dir, "data", "operations.json")
#path_file = "../data/operations.json"
transactions_list = transactions_read(path_file)
print(transactions_list)


def get_random_number(x: int, y: int) -> int:
    random_number = random.randint(x, y)
    return random_number


random_number = get_random_number(0, len(transactions_list))
transact = transactions_list[random_number]
# print(transact)
conversions_get(transact)


