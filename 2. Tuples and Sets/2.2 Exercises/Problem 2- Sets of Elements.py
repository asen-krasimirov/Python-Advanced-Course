# & - intersection

length_one, length_two = list(map(int, input().split()))

first_set = set()
second_set = set()

for _ in range(length_one):
    number = int(input())
    first_set.add(number)

for _ in range(length_two):
    number = int(input())
    second_set.add(number)

intersection_set = set(map(str, (first_set & second_set)))
print('\n'.join(intersection_set))
