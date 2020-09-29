from collections import deque

from builtins import list

cups = deque(list(map(int, input().split())))
bots = input().split()
bottles = deque(list(map(int, bots[::-1])))

wasted_water = 0

while cups and bottles:

    cup = cups.popleft()

    while cup > 0:

        bottle = bottles.popleft()
        cup -= bottle

        if cup > 0:
            continue
        elif cup <= 0:
            wasted_water += abs(cup)
            break

if bottles and not cups:
    bottles = list(map(str, bottles))
    print(f"Bottles: {' '.join(bottles)}")
else:
    cups = list(map(str, cups))
    print(f"Cups: {' '.join(cups)}")

print(f"Wasted litters of water: {wasted_water}")

