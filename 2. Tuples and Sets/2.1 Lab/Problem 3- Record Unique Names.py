num_names = int(input())
names = set()

for _ in range(num_names):
    name = input()
    names.add(name)

print('\n'.join(list(names)))
