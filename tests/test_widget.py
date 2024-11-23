import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "account_card, expected",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("Счет 64686 47367 88947 79589", "Счет **9589"),
        ("Счет-64686 47367 88947 79589", "Счет **9589"),
        ("Счет- 64686 47367 88947 79589", "Счет **9589"),
        ("Счет -64686 47367 88947 79589", "Счет **9589"),
        ("Счет - 64686 47367 88947 79589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
        ("Visa Gold 5999 4142 2842 6353", "Visa Gold 5999 41** **** 6353"),
        ("Visa Gold-5999414228426353", "Visa Gold 5999 41** **** 6353"),
        ("Visa Gold- 5999414228426353", "Visa Gold 5999 41** **** 6353"),
        ("Visa Gold -5999414228426353", "Visa Gold 5999 41** **** 6353"),
        ("Visa Gold - 5999414228426353", "Visa Gold 5999 41** **** 6353"),
    ],
)
def test_mask_account_card(account_card: str, expected: str) -> None:
    assert mask_account_card(account_card) == expected


def test_get_date(date_string: str) -> None:
    assert get_date(date_string) == "11.03.2024"


@pytest.mark.parametrize(
    "string_date, expected",
    [
        (" 2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2024_03_11T02:26:18.671407", "11.03.2024"),
        ("2024/03/11 T02:26:18.671407", "11.03.2024"),
        ("2024/03/11T02:26:18.671407", "11.03.2024"),
        ("24/03/11T02:26:18.671407", "Неверный формат данных"),
        ("03/11T02:26:18.671407", "Неверный формат данных"),
        ("2024/03/1102:26:18.671407", "Неверный формат данных"),
        ("T02:26:18.671407", "Неверный формат данных"),
        ("11 of February 2024T02:26:18.671407", "Неверный формат данных"),
    ],
)
def test_get_date_invalid(string_date: str, expected: str) -> None:
    assert get_date(string_date) == expected
