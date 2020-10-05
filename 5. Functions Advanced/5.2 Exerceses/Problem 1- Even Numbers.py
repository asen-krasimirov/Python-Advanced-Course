numbers = map(int, input().split())

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(even_numbers)


# Short Solution

# print(list(filter(lambda x: x % 2 == 0, map(int, input().split()))))
