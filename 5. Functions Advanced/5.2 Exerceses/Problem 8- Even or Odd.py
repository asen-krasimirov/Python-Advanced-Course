

def even_odd(*args):
    arguments = list(args)
    command = arguments.pop(-1)

    commands = {
        "even": list(filter(lambda x: x % 2 == 0, arguments)),
        "odd": list(filter(lambda x: x % 2 != 0, arguments))
    }

    return commands[command]


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))