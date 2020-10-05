def get_magic_triangle(n):
    triangle = [[1], [1, 1]]
    while len(triangle) < n:
        latest_row = triangle[-1]
        new_row = [1]
        for i in range(len(latest_row)-1):
            new_row.append(latest_row[i] + latest_row[i+1])
        new_row.append(1)
        triangle.append(new_row)
    return triangle


print(get_magic_triangle(5))