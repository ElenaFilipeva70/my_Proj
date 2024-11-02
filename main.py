from src.widget import get_date, mask_account_card

print("Ведите номер карты")
name_card = input()
name_card_mask = mask_account_card(name_card)
print(name_card_mask)

print("Ведите номер счета")
num_check = input()
num_check_mask = mask_account_card(num_check)
print(num_check_mask)

new_string_date = get_date("2024-03-11T02:26:18.671407")
print("Дата ", new_string_date)
