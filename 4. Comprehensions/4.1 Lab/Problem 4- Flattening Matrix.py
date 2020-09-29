size = int(input())
matrix = [
    map(int, input().split(", "))
    for i in range(size)
]

flattened_matrix = [
    num
    for row in matrix
    for num in row
]

print(flattened_matrix)

# one-liner
# print([num for row in [map(int, input().split(", ")) for i in range(int(input()))] for num in row])
