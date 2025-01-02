import os
from typing import Any, Optional

import requests
from dotenv import load_dotenv

# Загрузка переменных из .env-файла
load_dotenv()
API_KEY = os.getenv("API_KEY")
Base_URL = os.getenv("Base_URL")
print(API_KEY)
print(Base_URL)


def conversions_get(transactions_list: dict[str, Any]) -> Optional[Any | None]:
    """Функция, которая принимает на вход транзакцию и возвращает сумму транзакции в рублях"""
    try:
        amount = float(transactions_list["operationAmount"]["amount"])
        currency_code = transactions_list["operationAmount"]["currency"]["code"]
        if currency_code == "RUB":
            result_amount = round(amount, 4)
            return result_amount
        else:
            api_convert = get_convert_info(amount, currency_code)
            if api_convert != {}:
                result_amount = round(api_convert.get("result"), 4)
                return result_amount
    except requests.exceptions.RequestException:
        print("An error occurred. Please try again later.")
        return None


def get_convert_info(amount: float, currency: str) -> dict[str, Any]:
    """Функция выполняет обращение к внешнему API для получения текущего курса валют
    и конвертации суммы операции в рубли."""
    url = Base_URL
    payload = {"amount": amount, "from": currency, "to": "RUB"}
    headers = {"apikey": API_KEY}
    response = requests.get(url, headers=headers, params=payload)
    status_code = response.status_code
    if status_code == 200:
        result = response.json()
        return dict(result)
    else:
        print(f"Запрос завершился ошибкой: {response.reason}")
        return {}
