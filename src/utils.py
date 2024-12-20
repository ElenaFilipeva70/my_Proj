import json
import logging
import os
# import random
from typing import Any, Dict, List

from src.external_api import conversions_get

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("logs/utils.log", "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def transactions_read(path_file: str) -> List[Dict[str, Any]]:
    """Функция, которая принимает на вход путь до JSON-файла и возвращает список словарей с данными
    о финансовых транзакциях."""
    try:
        with open(path_file, "r", encoding="utf-8") as json_file:
            transactions_list = json.load(json_file)
            logger.debug("Успешное преобразование JSON-файла")
            return list(transactions_list)
    except Exception as e:
        print(type(e).__name__)
        logger.error(f"Возникла ошибка {e}", exc_info=True)
        return []
    finally:
        logger.info("Функция завершила работу")


# def get_random_number(x: int, y: int) -> int:
#     random_number = random.randint(x, y)
#     return random_number


base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path_file = os.path.join(base_dir, "data", "operations_test1.json")
# path_file = "../data/operations.json"
transactions_list = transactions_read(path_file)

# random_number = get_random_number(0, len(transactions_list)-1)
# transact = transactions_list[random_number]
# print(transact)
if transactions_list:
    result_amount = conversions_get(transactions_list[1])
    print(result_amount)
