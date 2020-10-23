from collections import deque


def filter_secondary_colors(colors: list, secondary_color):

    for color in colors:
        if color in secondary_colors:
            if color == "orange":
                if "red" not in colors or "yellow" not in colors:
                    colors.remove(color)
            elif color == "purple":
                if "red" not in colors or "blue" not in colors:
                    colors.remove(color)
            elif color == "green":
                if "yellow" not in colors or "blue" not in colors:
                    colors.remove(color)

    return colors


original_collection = deque(input().split())

main_colors = ["red", "yellow", "blue"]
secondary_colors = ["orange", "purple", "green"]
all_colors = main_colors + secondary_colors

found_combinations = []

while original_collection:

    if len(original_collection) == 1:
        last_element = original_collection.pop()

        if last_element in all_colors:
            found_combinations.append(last_element)
        else:
            if len(last_element) > 1:
                original_collection.append(last_element[:-1])

        continue

    collection_middle = (len(original_collection) // 2) - 1

    first_elem, last_elem = original_collection.popleft(), original_collection.pop()
    combination = first_elem + last_elem
    second_combination = last_elem + first_elem

    if combination in all_colors:
        found_combinations.append(combination)
        continue

    if second_combination in all_colors:
        found_combinations.append(second_combination)
        continue

    if len(first_elem) > 1:
        original_collection.insert(collection_middle, first_elem[:-1])

    if len(last_elem) > 1:
        original_collection.insert(collection_middle, last_elem[:-1])

final_result = filter_secondary_colors(found_combinations, secondary_colors)
print(final_result)
