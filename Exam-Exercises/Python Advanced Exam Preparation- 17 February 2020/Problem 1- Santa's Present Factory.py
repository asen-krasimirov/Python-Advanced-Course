from collections import deque, defaultdict


def task_completed(data):
    if "Doll" in data and "Wooden train" in data:
        return True

    if "Teddy bear" in data and "Bicycle" in data:
        return True

    return False


presents = {150: "Doll", 250: "Wooden train", 300: "Teddy bear", 400: "Bicycle"}

box = deque(list(map(int, input().split()))[::-1])  # Reverses the list to remove and add elements the same way later
magic = deque(list(map(int, input().split())))

crafted_presents = defaultdict(int)

while box and magic:

    box_zero = False
    magic_zero = False

    cur_box = box.popleft()
    if cur_box == 0:
        box_zero = True
    cur_magic = magic.popleft()
    if cur_magic == 0:
        magic_zero = True

    if box_zero or magic_zero:

        if not box_zero:
            box.appendleft(cur_box)

        if not magic_zero:
            magic.appendleft(cur_magic)

        continue

    total_magic_level = cur_box * cur_magic

    if total_magic_level < 0:
        box.appendleft(cur_box + cur_magic)
        continue

    elif total_magic_level >= 0 and total_magic_level not in presents:
        box.appendleft(cur_box+15)
        continue

    cur_crafted = presents[total_magic_level]
    crafted_presents[cur_crafted] += 1

task_status = task_completed(crafted_presents)
if task_status:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if box:
    print(f"Materials left: {', '.join([str(x) for x in box])}")
if magic:
    print(f"Magic left: {', '.join([str(x) for x in magic])}")

for name, amount in sorted(crafted_presents.items(), key=lambda x: x[0]):
    print(f"{name}: {amount}")
