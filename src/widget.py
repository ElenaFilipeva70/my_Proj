from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card: str) -> str:
    """Функция возвращает строку с замаскированным номером"""
    card_name = ""
    card_schet = ""
    for symbol in account_card:
        if symbol.isalpha():
            card_name += symbol
        elif symbol.isdigit():
            card_schet += symbol
    if card_name == "Счет":
        account_card = get_mask_account(card_schet)
    else:
        account_card = get_mask_card_number(card_schet)
    return card_name + " " + account_card
