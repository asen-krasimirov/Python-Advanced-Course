from itertools import combinations

names = input().split(", ")
chairs = int(input())

all_combinations = list(combinations(names, chairs))

for combination in all_combinations:
    print(', '.join(list(combination)))
