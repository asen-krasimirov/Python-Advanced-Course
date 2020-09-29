def get_input_numbers_in_int(separator=" "):
    return [int(x) for x in input().split(separator)]


row_count, column_count = get_input_numbers_in_int(", ")

matrix = []
for r in range(row_count):
    matrix.append(get_input_numbers_in_int())

for c in range(column_count):
    current_sum = 0
    for r in range(row_count):
        current_sum += matrix[r][c]
    print(current_sum)
