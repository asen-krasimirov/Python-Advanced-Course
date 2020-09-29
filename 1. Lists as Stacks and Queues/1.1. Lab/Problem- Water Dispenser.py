from collections import deque

water = int(input())

dispenser_queue = deque()

while True:
    command = input()
    if command == "Start":
        break
    dispenser_queue.append(command)

while True:
    command = input().split()
    task = command[0]
    if task == "End":
        print(f"{water} liters left")

        break

    if task.isdigit():
        person = dispenser_queue.popleft()

        if int(task) <= water:
            water -= int(task)
            print(f"{person} got water")
        else:
            print(f"{person} must wait")

    else:
        liters = int(command[1])
        water += liters
