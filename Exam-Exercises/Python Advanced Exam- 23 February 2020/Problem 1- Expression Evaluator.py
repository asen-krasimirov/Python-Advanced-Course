from functools import reduce


def true_values(expression):
    new_values = []
    for elem in expression:
        if elem.isdigit() or elem.lstrip("-").isdigit():
            new_values.append(int(elem))
        else:
            new_values.append(elem)

    return new_values


def expression_evaluator(expression: list):
    operators = {
        "*": lambda *args: reduce(lambda a, b: a * b, args),
        "+": lambda *args: reduce(lambda a, b: a + b, args),
        "-": lambda *args: reduce(lambda a, b: a - b, args),
        "/": lambda *args: int(reduce(lambda a, b: a / b, args))
    }

    i = 0
    while True:
        elem = expression[i]
        value = i
        if elem in operators:
            value = 0
            if not i+1 > len(expression):
                value = i+1

            new_value = operators[elem](*expression[:i])
            expression[:value] = [new_value]

            i -= value

        i += 1
        if i >= len(expression):
            break

    return expression[0]


data = true_values(input().split())
print(expression_evaluator(data))
