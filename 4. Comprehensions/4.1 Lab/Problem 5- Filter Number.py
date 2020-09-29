start = int(input())
end = int(input())

filtered_numbers = [
    num
    for num in range(start, end+1)
    if any([num % n == 0 for n in range(2, 11)])
]

print(filtered_numbers)

# one-liner
# print([num for num in range(int(input()), int(input())+1) if any([num % n == 0 for n in range(2, 11)])])
