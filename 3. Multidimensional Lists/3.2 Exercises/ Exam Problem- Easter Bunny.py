import sys


def get_sum_of_direction(matrix_, direction_, row, column):
    current_sum = 0
    current_list = []
    n = len(matrix_)

    if direction_ == "up":
        for i in range(row-1, -1, -1):
            egg_value = matrix_[i][column]
            if egg_value == "X":
                break

            current_sum += int(egg_value)
            current_list.append([i, column])

    elif direction_ == "down":
        for i in range(row+1, n):
            egg_value = matrix_[i][column]
            if egg_value == "X":
                break

            current_sum += int(egg_value)
            current_list.append([i, column])

    elif direction_ == "left":
        for i in range(column-1, -1, -1):
            egg_value = matrix_[row][i]
            if egg_value == "X":
                break

            current_sum += int(egg_value)
            current_list.append([row, i])

    elif direction_ == "right":
        for i in range(column+1, n):
            egg_value = matrix_[row][i]
            if egg_value == "X":
                break

            current_sum += int(egg_value)
            current_list.append([row, i])

    return current_sum, current_list


best_direction_sums = {
    "up": 0,
    "down": 0,
    "left": 0,
    "right": 0,
}

best_direction_coordinates = {
    "up": [],
    "down": [],
    "left": [],
    "right": []
}

field_size = int(input())
bunny_position = None

field = []
for r in range(field_size):
    line = input().split()
    if "B" in line:
        bunny_position = r, line.index("B")

    field.append(line)


best_sum = -sys.maxsize
best_direction = None

possible_directions = ["up", "down", "left", "right"]
for direction in possible_directions:
    bunny_r, bunny_c = bunny_position
    local_sum, local_list = get_sum_of_direction(field, direction, bunny_r, bunny_c)

    best_direction_sums[direction] += local_sum
    best_direction_coordinates[direction].extend(local_list)

    if local_sum > best_sum:
        best_sum = local_sum
        best_direction = direction

print(best_direction)
data_print = best_direction_coordinates[best_direction]
print('\n'.join([str(x) for x in data_print]))
print(best_direction_sums[best_direction])
