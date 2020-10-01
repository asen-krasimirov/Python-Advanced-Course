matrix_size = int(input())

matrix = [
    [
        int(x)
        for x in input().split(', ')
    ]
    for _ in range(matrix_size)
]

first_diagonal = [
    matrix[r][c]
    for r in range(matrix_size) for c in range(matrix_size)
    if r == c
]

second_diagonal = [
    matrix[r][matrix_size - 1 - r]
    for r in range(matrix_size)
]

print(f"First diagonal: {', '.join([str(x) for x in first_diagonal])}. Sum: {sum(first_diagonal)}")
print(f"Second diagonal: {', '.join([str(x) for x in second_diagonal])}. Sum: {sum(second_diagonal)}")

# Alternative Solution

# matrix = [[int(x) for x in input().split(', ')] for _ in range(int(input()))]
# print(f"First diagonal: {', '.join([str(x) for x in [matrix[r][c] for r in range(len(matrix)) for c in range(len(matrix)) if r == c]])}. Sum: {sum([matrix[r][c] for r in range(len(matrix)) for c in range(len(matrix)) if r == c])}")
# print(f"Second diagonal: {', '.join([str(x) for x in [matrix[r][len(matrix) - 1 - r] for r in range(len(matrix))]])}. Sum: {sum([matrix[r][len(matrix) - 1 - r] for r in range(len(matrix))])}")
