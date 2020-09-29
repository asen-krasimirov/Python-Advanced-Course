from collections import deque
from datetime import datetime, timedelta


robot_data = input().split(";")
current_time = datetime.strptime(input(), "%H:%M:%S")
robots = {}

for robot in robot_data:
    name, process_time = robot.split("-")

    robots[name] = {
        "processing_time": int(process_time),
        "available_at": current_time
    }

products = deque()
while True:
    command = input()
    if command == "End":
        break

    products.append(command)

while products:
    current_time += timedelta(seconds=1)
    product_taken = False
    product = products.popleft()

    for robot in robots:
        if robots[robot]["available_at"] <= current_time:
            robots[robot]["available_at"] = current_time + timedelta(seconds=robots[robot]["processing_time"])
            product_taken = True

            print(f"{robot} - {product} [{current_time.strftime('%H:%M:%S')}]")
            break

    if not product_taken:
        products.append(product)
