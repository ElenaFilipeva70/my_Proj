from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card: str) -> str:
    """Функция возвращает строку с замаскированным номером"""
    card_name = ""
    card_schet = ""
    for symbol in account_card:
        if symbol.isalpha() or symbol == " ":
            card_name += symbol
        elif symbol.isdigit():
            index = account_card.find(symbol)
            card_schet = account_card[index:]
            break
    if card_name[0:4] == "Счет":
        account_card = get_mask_account(card_schet)
    else:
        account_card = get_mask_card_number(card_schet)
    if card_name[-2] == " ":
        new_card_name = card_name[0: len(card_name) - 1]
        return new_card_name + account_card
    if card_name[-1] == " ":
        return card_name + account_card
    else:
        return card_name + " " + account_card


def get_date(string_date: str) -> str:
    """Функция возвращает строку с датой в формате ДД.ММ.ГГГГ"""
    string_date = string_date.replace(" ", "")
    if "T" in string_date:
        index_date = string_date.index("T")
        if index_date > 1:
            new_string_date = string_date[:index_date]
        else:
            new_string_date = string_date[: index_date + 1]
    else:
        return "Неверный формат данных"
    # new_string_date = string_date[8:10] + "." + string_date[5:7] + "." + string_date[0:4]
    new_date = ""
    if len(new_string_date) == 10:
        for number in new_string_date:
            if number.isdigit():
                new_date += number
            else:
                number = "-"
                new_date += number
        splited_string_date = new_date.split("-")
        formated_string_date = ".".join(splited_string_date[-1::-1])
        return formated_string_date
    else:
        return "Неверный формат данных"
