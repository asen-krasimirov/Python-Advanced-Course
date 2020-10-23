

def santa_eats_a_cookie(matrix, row, column, counter, kid_counter, movement):
    cookied_cells = []

    for move in movement.values():
        i, y = row + move[0], column + move[1]

        if matrix[i][y] != "-":
            counter -= 1

            if matrix[i][y] == "V":
                kid_counter -= 1

            matrix[i][y] = "-"

            # if counter == 0 or kid_counter == 1:
            #     break

    return counter, kid_counter


# def santa_out_in_neighborhood(matrix_length, n):
#     if -1 < n < matrix_length:
#         return True
#     return False


presents = int(input())
neighborhood_size = int(input())

santa_position = 0, 0
good_kids_count = 0
neighborhood = []

for r in range(neighborhood_size):
    line = input().split()

    if "S" in line:
        santa_position = r, line.index("S")

    if "V" in line:
        good_kids_count += line.count("V")

    neighborhood.append(line)

print_kids = int(good_kids_count)

movement_of_santa = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}


while presents > 0 and good_kids_count > 0:
    command = input()
    if command == "Christmas morning":
        break

    cur_row, cur_column = santa_position

    new_row, new_column = cur_row + movement_of_santa[command][0],\
                          cur_column + movement_of_santa[command][1]

    # if not santa_out_in_neighborhood(neighborhood_size, new_row) or \
    #    not santa_out_in_neighborhood(neighborhood_size, new_column):
    #     break

    neighborhood[cur_row][cur_column] = "-"
    new_elem = neighborhood[new_row][new_column]

    santa_position = new_row, new_column
    neighborhood[new_row][new_column] = "S"

    if new_elem == "V":
        presents -= 1
        good_kids_count -= 1

    elif new_elem == "C":
        presents, good_kids_count = \
                    santa_eats_a_cookie(neighborhood, new_row, new_column, presents, good_kids_count, movement_of_santa)

if presents <= 0 and good_kids_count > 0:
    print("Santa ran out of presents!")

for cur_row in neighborhood:
    print(" ".join(cur_row))

if good_kids_count == 0:
    print(f"Good job, Santa! {print_kids} happy nice kid/s.")
else:
    print(f"No presents for {good_kids_count} nice kid/s.")
