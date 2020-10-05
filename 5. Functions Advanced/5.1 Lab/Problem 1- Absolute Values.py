

def absolute_values(args):
    return [abs(x) for x in args]


random_numbers = list(map(float, input().split()))

abs_values = absolute_values(random_numbers)

print(abs_values)

# Shorter Solution

# print([abs(x) for x in list(map(float, input().split()))])
