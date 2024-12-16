import json
import os
# import random
from typing import Any, Dict, List

from src.external_api import conversions_get


def transactions_read(path_file: str) -> List[Dict[str, Any]]:
    """Функция, которая принимает на вход путь до JSON-файла и возвращает список словарей с данными
    о финансовых транзакциях."""
    try:
        with open(path_file, "r", encoding="utf-8") as json_file:
            transactions_list = json.load(json_file)
            return list(transactions_list)
    except Exception as e:
        print(type(e).__name__)
        return []


# def get_random_number(x: int, y: int) -> int:
#     random_number = random.randint(x, y)
#     return random_number


base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path_file = os.path.join(base_dir, "data", "operations_test.json")
# path_file = "../data/operations.json"
transactions_list = transactions_read(path_file)

# random_number = get_random_number(0, len(transactions_list)-1)
# transact = transactions_list[random_number]
# print(transact)
result_amount = conversions_get(transactions_list[1])
