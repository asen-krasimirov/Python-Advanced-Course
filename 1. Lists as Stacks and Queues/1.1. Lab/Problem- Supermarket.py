from collections import deque

queue = deque()

while True:
    command = input()

    if command == "Paid":
        for _ in range(len(queue)):
            person = queue.popleft()
            print(person)
        continue

    elif command == "End":
        print(f"{len(queue)} people remaining.")
        break

    queue.append(command)
