phone_book = {}
n_searches = 0

while True:
    information = input()
    if information.isdigit():
        n_searches = int(information)
        break

    name, phone_number = information.split('-')
    phone_book[name] = phone_number

for _ in range(n_searches):
    contact = input()
    if contact in phone_book:
        print(f"{contact} -> {phone_book[contact]}")
    else:
        print(f"Contact {contact} does not exist.")
