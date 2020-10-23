

def valid_movement(length, number):
    if -1 < number < length:
        return True
    return False


string = input()
field_size = int(input())
field = []

current_position = 0, 0

for r in range(field_size):
    line = input()
    if "P" in line:
        current_position = r, line.index("P")

    field.append(list(line))

number_of_commands = int(input())

movements = {
        "up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1)
    }

for _ in range(number_of_commands):
    command = input()

    cur_row, cur_column = current_position
    new_row, new_column = cur_row + movements[command][0], \
                          cur_column + movements[command][1]

    if not valid_movement(field_size, new_row) or not \
            valid_movement(field_size, new_column):
        if string:
            string = string[:-1]
        break

    new_elem = field[new_row][new_column]
    if new_elem != "-":
        string += new_elem

    field[cur_row][cur_column] = "-"
    field[new_row][new_column] = "P"
    current_position = new_row, new_column

print(string)
for r in field:
    print(''.join(r))
