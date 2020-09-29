number_of_usernames = int(input())
usernames = set()

for _ in range(number_of_usernames):
    name = input()
    usernames.add(name)

print('\n'.join(usernames))
