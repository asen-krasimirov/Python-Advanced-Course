def index_validation(matrix_length, number):
    if -1 < number < matrix_length:
        return True
    return False


def detonate_bomb(matrix_, row, column, damage_value):
    n = len(matrix_)
    matrix_[row][column] = 0

    for r in range(row-1, row+2):
        for c in range(column-1, column+2):

            if not index_validation(n, r) or not index_validation(n, c):
                continue

            if matrix_[r][c] > 0:
                matrix_[r][c] -= damage_value


size = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(size)]
bomb_coordinates = input().split()

for bomb in bomb_coordinates:
    bomb_row, bomb_column = [int(x) for x in bomb.split(",")]
    elem_value = matrix[bomb_row][bomb_column]

    if elem_value > 0:
        detonate_bomb(matrix, bomb_row, bomb_column, elem_value)

alive_sum = 0
alive_count = 0
for r in matrix:
    for elem in r:
        if elem > 0:
            alive_sum += elem
            alive_count += 1

print(f"Alive cells: {alive_count}")
print(f"Sum: {alive_sum}")
for r in matrix:
    print(' '.join([str(x) for x in r]))
