data = [numbers.split() for numbers in input().split("|")]

flatten_list = [
    number
    for numbers in reversed(data)
    for number in numbers
]

print(' '.join(flatten_list))
