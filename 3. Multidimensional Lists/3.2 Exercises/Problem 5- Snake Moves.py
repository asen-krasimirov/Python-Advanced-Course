from collections import deque


row_count, column_count = [int(x) for x in input().split()]
snake = deque(input())

for row in range(row_count):
    s = ''
    for column in range(column_count):
        piece = snake.popleft()
        s += piece
        snake.append(piece)

    if row % 2 == 0:
        print(s)
    else:
        print(s[::-1])
