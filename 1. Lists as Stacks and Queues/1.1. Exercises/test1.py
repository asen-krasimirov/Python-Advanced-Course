opposites = {"(": ")", "{": "}", "[": "]"}
parentheses_stack = []

data = input()

fail_flag = False

index = 0
while index < len(data) and not fail_flag:
    char = data[index]

    if char in opposites:
        opposite_parentheses = opposites[char]
        parentheses_stack.append(char)

        index += 1
        while True:
            char = data[index]

            if char == opposite_parentheses:
                parentheses_stack.pop()
                break
            elif char not in opposites:
                fail_flag = True
                break

            for i in range(len(parentheses_stack)):
                parentheses_stack[i] += char

            index += 1

    index += 1

if parentheses_stack or fail_flag:
    print("NO")
else:
    print("YES")
