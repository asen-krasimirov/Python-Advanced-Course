from collections import defaultdict


occurrences = defaultdict(int)
numbers = list(map(float, input().split()))

for number in numbers:

    occurrences[number] += 1

for number, occurrence_times in occurrences.items():
    print(f"{number} - {occurrence_times} times")
