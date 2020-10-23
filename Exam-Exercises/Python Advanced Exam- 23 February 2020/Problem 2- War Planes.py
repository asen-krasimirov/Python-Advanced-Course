

def validate_index(matrix_length, number):
    if -1 < number < matrix_length:
        return True
    return False


field_size = int(input())
field = []

plane_position = 0, 0
total_targets = 0
targets_destroyed = 0


for r in range(field_size):
    line = input().split()

    if 'p' in line:
        plane_position = r, line.index('p')

    if 't' in line:
        total_targets += line.count('t')

    field.append(line)


commands = [input() for _ in range(int(input()))][::-1]

direction_bases = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}


while commands:

    command = commands.pop().split()
    task = command[0]
    direction = command[1]
    steps = int(command[2])

    cur_row, cur_column = plane_position
    new_row, new_column = cur_row+direction_bases[direction][0]*steps, \
                          cur_column+direction_bases[direction][1]*steps

    if not validate_index(field_size, new_row) or \
       not validate_index(field_size, new_column):
        continue

    if task == 'move':
        if field[new_row][new_column] != '.':
            continue

        field[cur_row][cur_column] = '.'
        field[new_row][new_column] = 'p'

        plane_position = new_row, new_column

    elif task == 'shoot':
        if field[new_row][new_column] == 't':
            targets_destroyed += 1

        field[new_row][new_column] = 'x'

    if targets_destroyed == total_targets:
        break


if targets_destroyed == total_targets:
    print(f"Mission accomplished! All {total_targets} targets destroyed.")
else:
    print(f"Mission failed! {total_targets-targets_destroyed} targets left.")

for row in field:
    print(" ".join(row))
