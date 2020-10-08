from collections import deque


males = deque(input().split()[::-1])
females = deque(input().split())

matches = 0

while males and females:

    male = int(males.popleft())
    female = int(females.popleft())

    if male <= 0:
        females.appendleft(str(female))
        continue

    if female <= 0:
        males.appendleft(str(male))
        continue

    if male % 25 == 0:
        if males:
            males.popleft()
        females.appendleft(str(female))
        continue

    if female % 25 == 0:
        if females:
            females.popleft()
        males.appendleft(str(male))
        continue

    if male == female:
        matches += 1
        continue

    male -= 2
    males.appendleft(str(male))

print(f"Matches: {matches}")

male_data, female_data = "none", "none"
if males:
    male_data = ', '.join(males)

if females:
    female_data = ', '.join(females)

print(f"Males left: {male_data}")
print(f"Females left: {female_data}")
