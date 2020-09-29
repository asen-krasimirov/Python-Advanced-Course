n_inputs = int(input())
chemical_elements = set()

for _ in range(n_inputs):
    elements = input().split()
    for element in set(elements):
        chemical_elements.add(element)

print('\n'.join(chemical_elements))
