from mathops import calculate, prepare


expression = input()
values = prepare.prepare_calculation(expression)
result = calculate.make_calculation(*values)
print(result)
