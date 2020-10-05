

def concatenate(*args):
    if len(args) == 1:
        return args[0]

    return args[0] + concatenate(*args[1:])


# Alternative Function

# def concatenate(*args):
#     res = ""
#
#     for arg in args:
#         res += arg
#
#     return res
#
