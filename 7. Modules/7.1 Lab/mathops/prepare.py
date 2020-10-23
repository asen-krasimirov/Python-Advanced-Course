

def prepare_calculation(data):
    info = data.split()
    number_one = float(info[0])
    sign = info[1]
    number_two = int(info[2])

    operation = {
        "/": lambda a, b: a / b,
        "*": lambda a, b: a * b,
        "-": lambda a, b: a - b,
        "+": lambda a, b: a + b,
        "^": lambda a, b: a ** b,
    }[sign]

    return operation, number_one, number_two

