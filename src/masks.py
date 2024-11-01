from typing import Union


def get_mask_card_number(card_number: Union[str | int]) -> str:
    """Функция маскировки номера банковской карты"""
    card_number = str(card_number)
    if card_number.isdigit() and len(card_number) == 16:
        card_number_mask = card_number[0:4] + " " + card_number[4:6] + "**" + " " + "****" + " " + card_number[-4:]
        return card_number_mask
    else:
        return "Неверный формат номера карты"


def get_mask_account(num_check: Union[str | int]) -> str:
    """Функция маскировки номера банковского счета"""
    num_check = str(num_check)
    if num_check.isdigit() and len(num_check) == 20:
        num_check_mask = "**" + num_check[-4:]
        return num_check_mask
    else:
        return "Неверный формат номера счета"
