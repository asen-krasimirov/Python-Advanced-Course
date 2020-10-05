

def print_all_combinations(listed_string):
    test_presence = ''.join(listed_string)

    if test_presence not in unique_combinations:
        print(test_presence)
        unique_combinations.add(test_presence)
        return

    else:
        for _ in range(len(listed_string)):
            for i in range(len(listed_string)):
                if i + 1 == len(listed_string):
                    return

                listed_string[i], listed_string[i+1] = listed_string[i+1], listed_string[i]
                print_all_combinations(listed_string)


initial_listed_string = input()
unique_combinations = {initial_listed_string, }

print_all_combinations(list(initial_listed_string))
