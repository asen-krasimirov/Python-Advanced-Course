size = int(input())

even_matrix = [
    [
        num
        for num in map(int, input().split(", "))
        if num % 2 == 0
    ]
    for _ in range(size)
]

print(even_matrix)

# one-liner
# print([[num for num in map(int, input().split(", ")) if num % 2 == 0] for _ in range(int(input()))])
