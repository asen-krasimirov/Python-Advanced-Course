command = input()
numbers = list(map(int, input().split()))
res = 0

if command == "Odd":
    res = sum(filter(lambda x: x % 2 != 0, numbers))
else:
    res = sum(filter(lambda x: x % 2 == 0, numbers))

print(res * len(numbers))
