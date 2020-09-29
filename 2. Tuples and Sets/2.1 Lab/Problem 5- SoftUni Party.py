number_of_guests = int(input())

invited_guests = set()
for _ in range(number_of_guests):
    name = input()
    invited_guests.add(name)

guests_that_came = set()
while True:
    name = input()
    if name == "END":
        break

    guests_that_came.add(name)

guests_that_did_not_came = invited_guests - guests_that_came
print(len(guests_that_did_not_came))
print('\n'.join(sorted(guests_that_did_not_came)))
