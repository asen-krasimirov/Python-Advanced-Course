n_names = int(input())

even_set = set()
odd_set = set()

for line in range(1, n_names+1):
    name = sum(map(ord, input()))
    name = name // line

    if name % 2 == 0:
        even_set.add(name)
    else:
        odd_set.add(name)

even_sum = sum(even_set)
odd_sum = sum(odd_set)

final_set = []
if odd_sum > even_sum:
    final_set = map(str, odd_set - even_set)
elif odd_sum < even_sum:
    final_set = map(str, odd_set ^ even_set)
else:
    final_set = map(str, odd_set | even_set)

print(', '.join(list(final_set)))
