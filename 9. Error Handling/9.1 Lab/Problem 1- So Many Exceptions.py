numbers_list = list(map(int, input().split(", ")))
result = 1

for i in range(len(numbers_list)):
    number = numbers_list[i]

    if number <= 5:
        result *= number
    else:
        result /= number

print(int(result))
