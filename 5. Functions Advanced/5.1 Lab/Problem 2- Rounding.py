numbers = list(map(float, input().split()))

rounded_numbers = [
    round(num)
    for num in numbers
]

print(rounded_numbers)

# Shorter Solution

# print([round(num) for num in list(map(float, input().split()))])
