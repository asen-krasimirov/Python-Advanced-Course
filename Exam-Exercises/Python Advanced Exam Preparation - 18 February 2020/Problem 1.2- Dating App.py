from collections import deque


def get_value(gender):
    global males, females
    if gender == "males":

        while True:
            value = males.popleft()
            if value <= 0:
                if males:
                    continue
                break
            if value % 25 == 0:
                if males:
                    males.popleft()
                    if males:
                        continue
                    break
            return value

    elif gender == "females":

        while True:
            value = females.popleft()
            if value <= 0:
                if females:
                    continue
                break
            if value % 25 == 0:
                if females:
                    females.popleft()
                    if females:
                        continue
                    break
            return value


def print_final_data(matches_local, males_local, females_local):
    print(f"Matches: {matches_local}")
    print(f"Males left: {', '.join([str(x) for x in males_local])}" if males_local else "Males left: none")
    print(f"Females left: {', '.join([str(x) for x in females_local])}" if females_local else "Females left: none")


males = deque([int(x) for x in input().split()][::-1])
females = deque([int(x) for x in input().split()])
matches = 0

while males and females:

    cur_male = get_value("males")
    cur_female = get_value("females")

    if not cur_male:
        females.appendleft(cur_female)
        continue

    if not cur_female:
        males.appendleft(cur_male)
        continue

    if cur_male == cur_female:
        matches += 1
        continue

    males.appendleft(cur_male-2)

print_final_data(matches, males, females)
