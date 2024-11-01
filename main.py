from src.masks import get_mask_account, get_mask_card_number

print("Ведите номер карты")
name_card = input()
name_card_mask = get_mask_card_number(name_card)
print(name_card_mask)

print("Ведите номер счета")
num_check = input()
num_check_mask = get_mask_account(num_check)
print(num_check_mask)
