

def make_triangle(size):
    for r in range(1, size + 2):
        print(*[x for x in range(r, size)])

    for r in range(size, 0, -1):
        print(*[x for x in range(r, size)])

