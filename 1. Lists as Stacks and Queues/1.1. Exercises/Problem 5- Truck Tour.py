from collections import deque

main_circle = deque()

number_of_pumps = int(input())
for _ in range(number_of_pumps):
    fuel, kilometers = input().split()
    main_circle.append(int(fuel) - int(kilometers))


position = 0

while True:
    local_circle = deque(main_circle)
    local_sum = 0

    while local_circle:
        local_sum += local_circle.popleft()
        if local_sum < 0:
            break

    if local_sum < 0:
        main_circle.rotate(-1)
        position += 1
    else:
        print(position)
        break
