

def out_validate(matrix_length, n):
    if 0 <= n <= matrix_length-1:
        return False
    return True


size = int(input())
matrix = []

current_position = 0, 0
food_collected = 0

for r in range(size):
    line = input()
    destructed_line = [line[i] for i in range(size)]

    # start snake position
    if "S" in destructed_line:
        c = destructed_line.index("S")
        current_position = r, c

    matrix.append(destructed_line)

out_of_territory = False
snake_fed = False

while True:
    direction = input()

    movement = {
        "up": (-1, 0),
        "down": (+1, 0),
        "left": (0, -1),
        "right": (0, +1)
    }

    old_row = current_position[0]
    old_column = current_position[1]
    matrix[old_row][old_column] = "."

    new_row = current_position[0] + movement[direction][0]
    new_column = current_position[1] + movement[direction][1]

    current_position = new_row, new_column

    if out_validate(size, new_row) or out_validate(size, new_column):
        out_of_territory = True
        break

    if matrix[new_row][new_column] == "*":
        food_collected += 1
        matrix[new_row][new_column] = "S"

        if food_collected == 10:
            snake_fed = True
            break

    elif matrix[new_row][new_column] == "B":
        matrix[new_row][new_column] = "."

        for r in range(size):
            for c in range(size):
                if matrix[r][c] == "B":
                    matrix[r][c] = "S"
                    current_position = r, c
                    break

    else:
        matrix[new_row][new_column] = "S"

if out_of_territory:
    print("Game over!")
elif snake_fed:
    print("You won! You fed the snake.")

print(f"Food eaten: {food_collected}")
for r in matrix:
    print(''.join(r))
