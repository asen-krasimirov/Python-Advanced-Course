

def validate_index(matrix_length, number):
    if -1 < number < matrix_length:
        return True
    return False


def collected_eggs(value, cur_position, matrix_length, matrix):
    egg_count = 0
    positions_list = []

    cur_row, cur_column = cur_position
    add_row, add_column = value

    while validate_index(matrix_length, cur_row+add_row) and \
          validate_index(matrix_length, cur_column+add_column):

        cur_row, cur_column = cur_row+add_row, cur_column+add_column

        if matrix[cur_row][cur_column] == "X":
            break

        egg_count += int(matrix[cur_row][cur_column])
        positions_list.append(f"{[cur_row, cur_column]}")

    return egg_count, positions_list


def print_final_result(print_direction, print_positions, print_egg_count):
    print(print_direction)
    if print_positions:
        print("\n".join(print_positions) if print_positions else "[]")
    # else:
    #     print("[]")
    print(print_egg_count)


field_size = int(input())
field = []

bunny_position = 0, 0

for r in range(field_size):
    line = input().split()

    if "B" in line:
        bunny_position = r, line.index("B")

    field.append(line)

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

best_direction = None
best_positions = []
best_egg_count = -10000

for direction in directions:
    direction_value = directions[direction]

    local_egg_count, local_positions = collected_eggs(direction_value, bunny_position, field_size, field)

    if local_egg_count >= best_egg_count:
        best_direction = direction
        best_egg_count = local_egg_count
        best_positions = local_positions


print_final_result(best_direction, best_positions, best_egg_count)
