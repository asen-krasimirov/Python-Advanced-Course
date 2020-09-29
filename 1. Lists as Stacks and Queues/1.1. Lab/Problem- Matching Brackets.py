expression = list(input())
stack = []

for char in expression:

    if char == "(":
        stack.append("")

    for i in range(len(stack)):
        stack[i] += char

    if char == ")":
        sub_expression = stack.pop()
        print(sub_expression)
