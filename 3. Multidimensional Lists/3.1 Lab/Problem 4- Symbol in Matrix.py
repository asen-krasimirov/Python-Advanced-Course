# def get_input_as_list_in_int(separator=" "):
#     return list(map(int, input().split(separator)))


def find_symbol_in_matrix(matrix_, size_, symbol_):
    for row in range(size_):
        for column in range(size_):
            element = matrix_[row][column]
            if element == symbol_:
                return f"({row}, {column})"
    return f"{symbol_} does not occur in the matrix"


size = int(input())

matrix = []
for _ in range(size):
    line = list(input())
    matrix.append(line)

symbol = input()

result = find_symbol_in_matrix(matrix, size, symbol)
print(result)
