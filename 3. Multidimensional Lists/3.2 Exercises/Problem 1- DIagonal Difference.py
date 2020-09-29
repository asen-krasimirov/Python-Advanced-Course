def get_input_into_list_in_int(separator=" "):
    return [int(x) for x in input().split(separator)]


def get_diagonal_difference(matrix_, n):
    primary_diagonal_sum = 0
    secondary_diagonal_sum = 0

    for i in range(n):
        primary_diagonal_sum += matrix_[i][i]
        secondary_diagonal_sum += matrix_[i][n-i-1]

    return abs(primary_diagonal_sum - secondary_diagonal_sum)


size = int(input())
matrix = [get_input_into_list_in_int() for _ in range(size)]

result = get_diagonal_difference(matrix, size)
print(result)
