from functools import reduce

result = lambda *args: reduce(lambda a, b: a / b, args)

print(result(*[2, 2]))
