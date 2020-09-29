

def get_input_into_list_in_int(separator):
    return list(map(int, input().split(separator)))


def get_sum_of_sub_matrix(matrix_, row_, column_):
    return matrix_[row_][column_] + matrix_[row_][column_+1]\
           + matrix_[row_+1][column_] + matrix_[row_+1][column_+1]


def print_sub_matrix(matrix_, row_, column_):
    for r in range(row_, row_+2):
        for c in range(column_, column_+2):
            print(matrix_[r][c], end=" ")
        print()


row_counter, column_counter = get_input_into_list_in_int(", ")
matrix = [get_input_into_list_in_int(", ") for _ in range(row_counter)]

best_sub_matrix_sum = get_sum_of_sub_matrix(matrix, 0, 0)
best_position = 0, 0

for r in range(row_counter-1):
    for c in range(column_counter-1):
        local_sub_matrix = get_sum_of_sub_matrix(matrix, r, c)
        if local_sub_matrix > best_sub_matrix_sum:
            best_sub_matrix_sum = local_sub_matrix
            best_position = r, c

best_row, best_column = best_position
print_sub_matrix(matrix, best_row, best_column)
print(best_sub_matrix_sum)
