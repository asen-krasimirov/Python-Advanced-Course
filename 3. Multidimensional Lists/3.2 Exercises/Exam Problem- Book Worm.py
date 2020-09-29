from collections import deque


def validate_index(field_length, number):
    if -1 < number < field_length:
        return True
    return False
    

snake_position = (0, 0)
string = input()

field_size = int(input())
field = []
for r in range(field_size):
    line = list(input())
    if "P" in line:
        snake_position = r, line.index("P")
    
    field.append(line)

commands_count = int(input())
commands = deque([input() for _ in range(commands_count)])

possible_movements = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

while commands:
    command = commands.popleft()
    
    cur_row, cur_column = snake_position
    new_row, new_column = cur_row+possible_movements[command][0], \
                          cur_column+possible_movements[command][1]
    
    if not validate_index(field_size, new_row) or not validate_index(field_size, new_column):
        if string:
            string = string[:-1]
        continue

    elem = field[new_row][new_column]

    snake_position = new_row, new_column
    field[cur_row][cur_column] = "-"

    if elem != "-":
        string += elem
    field[new_row][new_column] = "P"

print(string)
for r in field:
    print(''.join([str(x) for x in r]))
