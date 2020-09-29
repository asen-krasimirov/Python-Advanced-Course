from collections import deque

green_time = int(input())
free_time = int(input())

cars = deque()

cars_passed = 0

while True:
    command = input()

    if command == "END":
        break

    # green light cycle
    if command == "green":
        local_green_time = int(green_time)
        while local_green_time != 0 and cars:

            car_in = cars.popleft()
            if local_green_time - len(car_in) >= 0:
                local_green_time -= len(car_in)
                cars_passed += 1

            else:
                if (local_green_time + free_time) - len(car_in) >= 0:
                    cars_passed += 1
                    break

                else:
                    print("A crash happened!")
                    print(f"{car_in} was hit at {car_in[(local_green_time + free_time) - len(car_in)]}.")
                    exit()

        continue

    cars.append(command)

print("Everyone is safe.")
print(f"{cars_passed} total cars passed the crossroads.")
