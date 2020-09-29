from itertools import chain


def submatrix_sum(i, j, rows, cols, matrix):
    if i + 2 < rows and j + 2 < cols:  # check if a 3x3 submatrix can be constructed from current i and j
        m_3x3 = []
        for ii in range(i, i + 3):  # ii and jj are submatrix indices
            row = []
            for jj in range(j, j + 3):
                row.append(matrix[ii][jj])
            m_3x3.append(row)

        return sum(chain(*m_3x3)), m_3x3
    else:
        return 0, []  # if no 3x3 can be constructed from i and j, return 0 as sum and empty list


rows, cols = map(int, input().split())

matrix = []  # construct matrix from input
for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

submatrix_max = [[0 for _ in range(3)] for _ in
                 range(3)]  # default 3x3 matrix with zeroes, if no other 3x3 can be constructed!!!
submatrix_max_sum = 0

if rows >= 3 and cols >= 3:  # if the input matrix is not at least 3x3, skip checks and go to default
    for i in range(rows):
        for j in range(cols):
            submatrix_current_sum, submatrix_current = submatrix_sum(i, j, rows, cols,
                                                                     matrix)  # fetch 3x3 submatrix and its sum
            if submatrix_current_sum > submatrix_max_sum:  # overwrite current if sum > current max sum
                submatrix_max_sum = submatrix_current_sum
                submatrix_max = submatrix_current

submatrix_max_str = "\n".join(" ".join(str(element) for element in row) for row in submatrix_max)  # string for output

print(f"Sum = {submatrix_max_sum}")
