from collections import deque


def best_list_pureness(array_data, rotations):
    array = deque([int(n) for n in array_data])

    best_pureness_score = 0
    best_rotation = 0

    array.rotate(-1)
    for rotation in range(0, rotations+1):
        array.rotate(1)
        local_pureness_score = 0
        for i in range(len(array)):
            local_pureness_score += i * array[i]
        if local_pureness_score > best_pureness_score:
            best_pureness_score = local_pureness_score
            best_rotation = rotation
    return f"Best pureness {best_pureness_score} after {best_rotation} rotations"


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)

test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)

test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
