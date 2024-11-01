from src.widget import mask_account_card

print("Ведите номер карты")
name_card = input()
name_card_mask = mask_account_card(name_card)
print(name_card_mask)

print("Ведите номер счета")
num_check = input()
num_check_mask = mask_account_card(num_check)
print(num_check_mask)
