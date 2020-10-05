

def print_all_combinations(array, index):
    test_presence_ = "".join(array)
    if index >= len(array):
        print("".join(array))
        return

    print_all_combinations(array, index+1)
    for y in range(index+1, len(array)):
        array[index], array[y] = array[y], array[index]
        print_all_combinations(array, index+1)
        array[index], array[y] = array[y], array[index]


listed_string = input()
print_all_combinations(list(listed_string), 0)

# for _ in range(length):
#     test_presence = "".join(listed_string)
#     if test_presence not in combinations:
#         combinations.add(test_presence)
#
#     for i in range(length):
#         if i + 1 == length:
#             break
#
#         listed_string[i], listed_string[i+1] = listed_string[i+1], listed_string[i]
#
#         test_presence = "".join(listed_string)
#         if test_presence not in combinations:
#             combinations.add(test_presence)
#
# print(combinations)
