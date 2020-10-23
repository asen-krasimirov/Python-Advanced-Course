

class OutOfField(Exception):
    pass


def find_in_matrix(matrix, matrix_length, element):
    for r in range(matrix_length):
        for c in range(matrix_length):

            if matrix[r][c] == element:
                return r, c


def validate_index(matrix_length, number):
    if -1 < number < matrix_length:
        return
    raise OutOfField()


def move_worm(direction):
    global field, worm_position, string
    field_length = len(field)
    # new_row, new_column = worm_position[0]+direction[0], worm_position[1]+direction[1]

    cur_row, cur_column = worm_position
    new_row, new_column = cur_row+direction[0], cur_column+direction[1]

    try:
        validate_index(field_length, new_row)
        validate_index(field_length, new_column)
        elem = field[new_row][new_column]
        worm_position = new_row, new_column
        if elem.isalpha():
            string += elem
        field[cur_row][cur_column] = "-"
        field[new_row][new_column] = "P"
    except OutOfField:
        if string:
            string = string[:-1]


def print_final_result():
    print(string)
    for row in field:
        print(''.join(row))


string = input()
field_size = int(input())
field = [list(input()) for _ in range(field_size)]
worm_position = find_in_matrix(field, field_size, "P")

possible_directions = {"up": (-1, 0), "down": (1, 0),
                       "left": (0, -1), "right": (0, 1)}

number_of_commands = int(input())
for _ in range(number_of_commands):
    command = input()
    move_worm(possible_directions[command])

print_final_result()
