def get_input_information_in_int(separator):
    return list(map(int, input().split(separator)))


row_count, column_count = get_input_information_in_int(", ")

# matrix = [get_input_information_in_int(", ") for _ in range(row_count)]
# print(matrix)

matrix = []
total_sum = 0
for r in range(row_count):
    current_column = get_input_information_in_int(", ")

    matrix.append(current_column)
    # total_sum += sum(current_column)

# print(total_sum)
# print(matrix)

for row in matrix:
    total_sum += sum(row)

print(total_sum)
print(matrix)
