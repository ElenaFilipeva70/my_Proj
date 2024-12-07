import os
from dotenv import load_dotenv
import requests
from typing import Any


# Загрузка переменных из .env-файла
load_dotenv()
API_KEY = os.getenv('API_KEY')
Base_URL = os.getenv('Base_URL')
# print(API_KEY)
# print(Base_URL)


def conversions_get(transactions_list: dict[Any]) -> float:
    """ Функция, которая принимает на вход транзакцию и возвращает сумму транзакции в рублях """
    try:
        amount = float(transactions_list["operationAmount"]["amount"])
        cyrrency_code = transactions_list["operationAmount"]["currency"]["code"]
        if cyrrency_code != "RUB":
            url = Base_URL
            payload = {
                "amount": amount,
                "from": cyrrency_code,
                "to": "RUB"
            }
            headers = {"apikey": API_KEY}
            response = requests.get( url, headers=headers, params=payload)
            status_code = response.status_code
            print(status_code)
            result = response.json()
            amount = result["result"]
        print(amount)
        return amount
    except Exception as e:
        print(type(e).__name__)



# {'success': True, 'query': {'from': 'USD', 'to': 'RUB', 'amount': 8221.37}, 'info': {'timestamp': 1733551503, 'rate': 100.475628}, 'date': '2024-12-07', 'result': 826047.31377}
# 200
# {'success': True, 'query': {'from': 'USD', 'to': 'RUB', 'amount': 9824.07}, 'info': {'timestamp': 1733551503, 'rate': 100.475628}, 'date': '2024-12-07', 'result': 987079.602766}
# 200
# {'success': True, 'query': {'from': 'USD', 'to': 'RUB', 'amount': 79114.93}, 'info': {'timestamp': 1733551503, 'rate': 100.475628}, 'date': '2024-12-07', 'result': 7949122.275926}
# 200
# {'success': True, 'query': {'from': 'USD', 'to': 'RUB', 'amount': 70946.18}, 'info': {'timestamp': 1733551503, 'rate': 100.475628}, 'date': '2024-12-07', 'result': 7128361.989701}
# 200
# {'success': True, 'query': {'from': 'USD', 'to': 'RUB', 'amount': 51463.7}, 'info': {'timestamp': 1733551503, 'rate': 100.475628}, 'date': '2024-12-07', 'result': 5170847.576704}
# 200
# {'success': True, 'query': {'from': 'USD', 'to': 'RUB', 'amount': 56883.54}, 'info': {'timestamp': 1733551503, 'rate': 100.475628}, 'date': '2024-12-07', 'result': 5715409.404363}