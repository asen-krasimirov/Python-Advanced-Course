import sys


def get_input_into_list_in_int(separator=" "):
    return list(map(int, input().split(separator)))


def create_default_3x3_matrix():
    return [[0]*3 for _ in range(3)]


def get_tree_x_tree_sub_matrix(matrix_, row, column):
    sub_matrix = []

    for i in range(row, row+3):
        sub_matrix.append(matrix_[i][column:column+3])

    return sub_matrix


row_count, column_count = get_input_into_list_in_int()

# matrix = []
# if row_count < 3 or column_count < 3:
#
#     matrix = create_default_matrix(column_count)
#     for r in range(row_count):
#         line = get_input_into_list_in_int()
#         for c in range(column_count):
#             matrix[r][c] = line[c]
#
#     if row_count < 3:
#         row_count += abs(3-row_count)
#
#     if column_count < 3:
#         column_count += abs(3-column_count)

# else:
# matrix = [get_input_into_list_in_int() for _ in range(row_count)]
matrix = [input().split() for _ in range(row_count)]

best_sum = -99999
best_sub_matrix = create_default_3x3_matrix()

for r in range(row_count-2):
    for c in range(column_count-2):
        tree_x_tree_sub_matrix = get_tree_x_tree_sub_matrix(matrix, r, c)
        local_sub_matrix_sum = 0

        for row_ in range(len(tree_x_tree_sub_matrix)):
            # local_sub_matrix_sum += sum(tree_x_tree_sub_matrix[row_])
            for elem in tree_x_tree_sub_matrix[row_]:
                if elem.isdigit():
                    local_sub_matrix_sum += int(elem)

        if local_sub_matrix_sum > best_sum:
            best_sum = local_sub_matrix_sum
            best_sub_matrix = tree_x_tree_sub_matrix

if not best_sum > -99999:
    print(f"Sum = 0")
else:
    print(f"Sum = {best_sum}")

for r in best_sub_matrix:
    print(' '.join([str(x) for x in r]))
