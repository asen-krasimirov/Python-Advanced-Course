number_of_commands = int(input())
stack = []

for _ in range(number_of_commands):
    command = input().split()
    query = command[0]

    if query == "1":

        element = int(command[1])
        stack.append(element)

    elif query == "2":

        if stack:
            stack.pop()

    elif query == "3":

        print(max(stack))

    elif query == "4":

        print(min(stack))

stack = list(map(str, stack))
print(", ".join(stack[::-1]))
