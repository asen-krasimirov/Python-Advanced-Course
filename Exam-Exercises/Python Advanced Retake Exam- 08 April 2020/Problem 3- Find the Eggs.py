

def find_strongest_eggs(*data):
    sequence, power = data[0], data[-1]
    strongest_eggs = []

    extracted_sequences = []
    start_index = -1
    for _ in range(power):
        new_sequence = []
        start_index += 1
        for i in range(start_index, len(sequence), power):
            new_sequence.append(sequence[i])

        extracted_sequences.append(new_sequence)

    for egg_sequence in extracted_sequences:
        middle_ = len(egg_sequence) // 2

        if not egg_sequence[middle_] > egg_sequence[middle_-1] or \
           not egg_sequence[middle_] > egg_sequence[middle_+1]:
            continue

        fail = False
        for i in range(middle_):
            left_elem = egg_sequence[i]
            right_elem = egg_sequence[i*-1-1]

            if not right_elem > left_elem:
                fail = True
                break
        if fail:
            continue

        strongest_eggs.append(egg_sequence[middle_])

    return strongest_eggs

test = ([-1, 7, 3, 15, 2, 12], 2)
print(find_strongest_eggs(*test))

test = ([-1, 0, 2, 5, 2, 3], 2)
print(find_strongest_eggs(*test))

test = ([51, 21, 83, 52, 55], 1)
print(find_strongest_eggs(*test))
