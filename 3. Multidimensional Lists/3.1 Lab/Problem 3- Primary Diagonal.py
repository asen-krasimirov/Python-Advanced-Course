

def transfer_input_data_in_int_list(separator=" "):
    return list(map(int, input().split(separator)))


def get_primary_diagonal_sum(matrix_):
    local_sum = 0
    for i in range(len(matrix_)):
        local_sum += matrix_[i][i]
    return local_sum


def get_secondary_sum(matrix_):
    local_sum = 0
    n = len(matrix_)
    for r in range(n):
        local_sum += matrix_[r][n-r-1]
    return local_sum


def get_sum_under_primary_diagonal(matrix_):
    local_sum = 0
    for r in range(len(matrix_)):
        for c in range(r):
            local_sum += matrix_[r][c]
    return local_sum


def get_sum_above_primary_diagonal(matrix_):
    local_sum = 0
    n = len(matrix_)
    for r in range(n):
        for c in range(n-1, r, -1):
            local_sum += matrix_[r][c]
    return local_sum


def get_sum_under_secondary_diagonal(matrix_):
    local_sum = 0
    n = len(matrix_)
    for r in range(n-1, -1, -1):
        for c in range(n-1, n-1-r, -1):
            local_sum += matrix[r][c]
    return local_sum


def get_sum_above_secondary_diagonal(matrix_):
    local_sum = 0
    n = len(matrix_)
    for r in range(n):
        for c in range(n-r-1):
            local_sum += matrix_[r][c]
    return local_sum


size = int(input())
matrix = [transfer_input_data_in_int_list() for _ in range(size)]

# result = get_primary_diagonal_sum(matrix)
# result = get_secondary_sum(matrix)
# result = get_sum_above_primary_diagonal(matrix)
# result = get_sum_under_primary_diagonal(matrix)
# result = get_sum_under_secondary_diagonal(matrix)
result = get_sum_above_secondary_diagonal(matrix)

print(result)
