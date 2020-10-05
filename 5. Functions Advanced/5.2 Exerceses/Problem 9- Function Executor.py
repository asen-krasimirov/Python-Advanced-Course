def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


def func_executor(*args):

    functions_results = []

    for arg in args:
        func, func_args = arg
        local_result = func(*func_args)
        functions_results.append(local_result)

    return functions_results


print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))
