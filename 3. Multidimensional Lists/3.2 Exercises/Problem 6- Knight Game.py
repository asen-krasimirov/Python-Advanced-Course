def index_validate(matrix_length, number):
    if -1 < number < matrix_length:
        return True
    return False


def knight_attack_sum(matrix_, row, column, possible_moves_: list):
    attack_sum = 0
    matrix_length = len(matrix_)

    for move in possible_moves_:
        row_addition, column_addition = move
        if index_validate(matrix_length, row+row_addition) and \
           index_validate(matrix_length, column+column_addition):

            if matrix_[row+row_addition][column+column_addition] == "K":
                attack_sum += 1

    return attack_sum


n = int(input())
matrix = [list(input()) for _ in range(n)]

possible_moves = [
    (-2, -1),
    (-2, 1),
    (-1, 2),
    (-1, -2),
    (1, -2),
    (1, 2),
    (2, -1),
    (2, 1)
]

total_removes = 0

while True:
    most_dangerous = 0, 0
    most_dangerous_sum = 0

    for r in range(n):
        for c in range(n):
            if matrix[r][c] == "K":
                local_attack_sum = knight_attack_sum(matrix, r, c, possible_moves)
                if local_attack_sum > most_dangerous_sum:
                    most_dangerous_sum = local_attack_sum
                    most_dangerous = r, c

    if most_dangerous_sum != 0:
        row_remove, column_remove = most_dangerous
        matrix[row_remove][column_remove] = "0"
        total_removes += 1
    else:
        break

print(total_removes)
