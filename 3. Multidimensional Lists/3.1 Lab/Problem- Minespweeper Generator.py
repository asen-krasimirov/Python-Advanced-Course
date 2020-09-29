

def in_matrix_validate(matrix_length, n):
    if 0 <= n <= matrix_length-1:
        return True
    return False


def find_new_value(matrix_, row_, column_):
    new_value = 0
    n = len(matrix_)

    for row in range(row_-1, row_+2):
        for column in range(column_-1, column_+2):

            if in_matrix_validate(n, row) and in_matrix_validate(n, column):

                if matrix_[row][column] == "*":
                    new_value += 1

    return f"{new_value}"


size = int(input())
bomb_count = int(input())
matrix = [["0"]*size for _ in range(size)]


for _ in range(bomb_count):
    bomb_information = list(input())
    bomb_row, bomb_column = bomb_information[1], bomb_information[4]

    matrix[int(bomb_row)][int(bomb_column)] = "*"


for r in range(size):
    for c in range(size):
        if matrix[r][c] != "*":
            matrix[r][c] = find_new_value(matrix, r, c)

for r in range(size):
    print(" ".join(matrix[r]))
