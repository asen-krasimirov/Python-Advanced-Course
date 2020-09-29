def turn_input_in_list_in_int(separator=" "):
    return list(map(int, input().split(separator)))


def index_validation(length, number):
    if -1 < number < length:
        return True
    return False


def validate_command(data: str, row, column):
    command_ = data.split()
    task = command_.pop(0)
    other_ = command_[0:]

    if task != "swap":
        return False

    if len(other_) != 4:
        return False

    r_1, c_1, r_2, c_2 = other_
    if not index_validation(row, int(r_1)) or \
            not index_validation(row, int(r_2)) or \
            not index_validation(column, int(c_1)) or \
            not index_validation(column, int(c_2)):

        return False

    return True


row_count, column_count = turn_input_in_list_in_int()
matrix = [[x for x in input().split()] for _ in range(row_count)]

while True:
    data = input()
    if data == "END":
        break

    if not validate_command(data, row_count, column_count):
        print("Invalid input!")
    else:
        command = data.split()
        _, *other = command
        r1, c1, r2, c2 = other

        first_element = matrix[int(r1)][int(c1)]
        second_element = matrix[int(r2)][int(c2)]

        matrix[int(r1)][int(c1)] = second_element
        matrix[int(r2)][int(c2)] = first_element

        for r in matrix:
            print(' '.join([str(x) for x in r]))
