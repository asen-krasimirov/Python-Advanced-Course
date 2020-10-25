

def valid_index(number):
    if -1 < number < 8:
        return True
    return False


def is_queen_attaching(matrix, directions, *cur_position):

    for direction in directions:
        local_row, local_column = cur_position
        row_delta, column_delta = direction
        for _ in range(8):
            local_row += row_delta
            local_column += column_delta

            if not valid_index(local_row) or not valid_index(local_column):
                break

            if matrix[local_row][local_column] == "Q":
                break
            if matrix[local_row][local_column] == "K":
                return True
    return False


field = [input().split() for _ in range(8)]

possible_directions = [
    (-1, 0), (1, 0),
    (0, -1), (0, 1),
    (-1, -1), (-1, 1), (1, -1), (1, 1)
]

attacking_queens = []

for r in range(8):
    for c in range(8):
        if field[r][c] == "Q":
            if is_queen_attaching(field, possible_directions, r, c):
                attacking_queens.append([r, c])

if attacking_queens:
    for queen in attacking_queens:
        print(queen)
else:
    print("The king is safe!")
