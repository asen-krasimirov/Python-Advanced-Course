from itertools import product


def print_expressions(array_numbers, possible_operators):
    for possible_operator in possible_operators:
        ops = list(possible_operator)[::-1]
        numbers_ = array_numbers[::-1]

        expression = ""
        for _ in range(len(ops)):
            expression += ops.pop()
            expression += numbers_.pop()

        print(f"{expression}={eval(expression)}")


numbers = input().split(", ")
operators = list(product('+-', repeat=len(numbers)))

print_expressions(numbers, operators)
