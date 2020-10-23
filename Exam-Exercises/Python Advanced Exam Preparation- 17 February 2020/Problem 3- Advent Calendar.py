

def fix_calendar(array):
    swaps = -1

    while True:
        if swaps == 0:
            break

        swaps = 0

        for i in range(len(array)-1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                swaps += 1

    return array


numbers = [3, 2, 1]
fixed = fix_calendar(numbers)
print(fixed)
