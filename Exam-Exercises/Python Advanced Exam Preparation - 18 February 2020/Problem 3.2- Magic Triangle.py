

def get_magic_triangle(number_of_rows):
    magic_triangle = [[1], [1, 1]]
    for r in range(1, number_of_rows-1):
        new_row = [1]
        for i in range(len(magic_triangle[r])-1):
            new_row.append(magic_triangle[r][i] + magic_triangle[r][i+1])
        new_row.append(1)
        magic_triangle.append(new_row)
    return magic_triangle


print(get_magic_triangle(5))
