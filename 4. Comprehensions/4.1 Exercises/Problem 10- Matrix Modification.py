def index_validation(matrix_length, number):
    if -1 < number < matrix_length:
        return True
    return False


size = int(input())
matrix = [
    list(map(int, input().split()))
    for _ in range(size)
]

while True:
    command = input().split()
    task = command[0]
    if task == "END":
        break

    row = int(command[1])
    column = int(command[2])
    value = int(command[3])

    if not index_validation(size, row) or not index_validation(size, column):
        print("Invalid coordinates")
        continue

    current_value = matrix[row][column]

    if task == "Add":
        current_value += value
    elif task == "Subtract":
        current_value -= value

    matrix[row][column] = current_value

[print(' '.join([str(x) for x in row]))for row in matrix]

# for row in matrix:
#     print(' '.join([str(x) for x in row]))
