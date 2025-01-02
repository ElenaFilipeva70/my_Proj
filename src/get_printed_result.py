from typing import Any, Dict, List

from src.widget import get_date, mask_account_card


def printed_transaction(result_list: List[Dict[str, Any]]) -> None:
    """Функция печатает итоговый список транзакций"""
    if not result_list:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        print(f"Всего банковских операций в выборке: {len(result_list)}")
    for transaction in result_list:
        string_date = str(transaction.get("date"))
        account_card_to = str(transaction.get("to"))
        account_card_from = str(transaction.get("from"))
        currency_card = transaction.get("currency_code", "")
        if currency_card == "":
            if transaction.get("description") == "Открытие вклада":
                print(
                    f'{get_date(string_date)} {transaction["description"]}\n'
                    f"{mask_account_card(account_card_to)}\n"
                    f'Сумма: {transaction["operationAmount"]["amount"]}'
                    f' {transaction["operationAmount"]["currency"]["name"]}'
                )
            else:
                print(
                    f'{get_date(string_date)} {transaction["description"]}\n'
                    f"{mask_account_card(account_card_from)} -> {mask_account_card(account_card_to)}\n"
                    f'Сумма: {transaction["operationAmount"]["amount"]} '
                    f'{transaction["operationAmount"]["currency"]["name"]}'
                )
        if currency_card:
            if transaction.get("currency_code") == "RUB":
                transaction["currency_code"] = "руб."
            if transaction.get("description") == "Открытие вклада":
                print(
                    f'{get_date(string_date)} {transaction.get("description")}\n'
                    f"{mask_account_card(account_card_to)}\n"
                    f'Сумма: {transaction.get("amount")} {transaction["currency_code"]}'
                )
            else:
                print(
                    f'{get_date(string_date)} {transaction.get("description")}\n'
                    f"{mask_account_card(account_card_from)} -> {mask_account_card(account_card_to)}\n"
                    f'Сумма: {transaction.get("amount")} {transaction.get("currency_code")}'
                )
