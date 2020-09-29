def get_input_into_list_in_int(separator=" "):
    return list(map(int, input().split(separator)))


def check_square(matrix_, row, column):
    char = matrix_[row][column]

    for i in range(row, row+2):
        for y in range(column, column+2):
            if matrix[i][y] != char:
                return False

    return True


row_count, column_count = get_input_into_list_in_int()
matrix = [input().split() for _ in range(row_count)]

total_equal_squares = 0

for r in range(row_count-1):
    for c in range(column_count-1):
        if check_square(matrix, r, c):
            total_equal_squares += 1

print(total_equal_squares)
