import logging
from typing import Union

logging.basicConfig(
    level=logging.DEBUG,
    filename="logs/masks.log",
    filemode="w",
    format="%(asctime)s %(name)s %(levelname)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    encoding="utf-8",
)
card_number_logger = logging.getLogger("masks.card_number")
account_logger = logging.getLogger("masks.account")


def get_mask_card_number(card_number: Union[str | int]) -> str:
    """Функция маскировки номера банковской карты"""
    try:
        card_number_logger.info("Запуск функции маскировки номера банковской карты")
        card_number = str(card_number)
        new_card_number = card_number.replace(" ", "")
        if new_card_number.isdigit() and len(new_card_number) == 16:
            card_number_logger.info("Маскировка номера банковской карты")
            card_number_mask = (
                new_card_number[0:4] + " " + new_card_number[4:6] + "**" + " " + "****" + " " + new_card_number[-4:]
            )
            return card_number_mask
        else:
            card_number_logger.warning("Неверный формат номера карты")
            return "Неверный формат номера карты"
    except Exception as e:
        print(type(e).__name__)
        card_number_logger.error(f"Возникла ошибка {e}", exc_info=True)
        return f"Возникла ошибка {e}"
    finally:
        card_number_logger.info("Функция маскировки номера банковской карты завершила работ")


def get_mask_account(num_check: Union[str | int]) -> str:
    """Функция маскировки номера банковского счета"""
    try:
        account_logger.info("Запуск функции маскировки номера банковского счета")
        num_check = str(num_check)
        new_num_check = num_check.replace(" ", "")
        if new_num_check.isdigit() and len(new_num_check) == 20:
            account_logger.info("Маскировка номера банковского счета")
            num_check_mask = "**" + new_num_check[-4:]
            return num_check_mask
        else:
            account_logger.warning("Неверный формат номера счета")
            return "Неверный формат номера счета"
    except Exception as e:
        print(type(e).__name__)
        account_logger.error(f"Возникла ошибка {e}", exc_info=True)
        return f"Возникла ошибка {e}"
    finally:
        account_logger.info("Функция маскировки номера банковского счета завершила работ")


# card_number = 7000792289606361
# mask_card_number = get_mask_card_number(card_number)
# num_check = 73654108430135874305
# mask_account = get_mask_account(num_check)
