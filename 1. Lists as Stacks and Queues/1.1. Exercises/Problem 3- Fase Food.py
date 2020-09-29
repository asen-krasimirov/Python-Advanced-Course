from collections import deque

quantity_of_food = int(input())
queue = deque(list(map(int, input().split())))

# biggest_order = 0
# for _ in range(len(queue)):
#     current_order = queue.popleft()
#     if current_order > biggest_order:
#         biggest_order = current_order
#
#     queue.append(current_order)

biggest_order = max(queue)
print(biggest_order)

while True:

    if not queue:
        break

    if quantity_of_food - queue[0] < -1:
        break

    quantity_of_food -= queue.popleft()

queue = list(map(str, queue))
if queue:
    print(f"Orders left: {' '.join(queue)}")
else:
    print("Orders complete")
