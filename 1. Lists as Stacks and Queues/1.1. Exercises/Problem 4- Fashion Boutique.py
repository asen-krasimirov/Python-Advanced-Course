
clothes = list(map(int, input().split()))
rack_capacity = int(input())

rack_count = 1
clothes_sum = 0

while clothes:

    if clothes_sum + clothes[-1] == rack_capacity:
        clothes.pop()
        clothes_sum = 0
        if clothes:
            rack_count += 1
        continue

    elif clothes_sum + clothes[-1] > rack_capacity:
        clothes_sum = 0
        rack_count += 1
        continue

    clothes_sum += clothes.pop()

print(rack_count)
