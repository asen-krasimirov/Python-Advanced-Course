# string = input()
# stacked_string = [string[i] for i in range(len(string))]
# stack_length = len(stacked_string)
#
# for _ in range(stack_length):
#     letter = stacked_string.pop()
#     print(f"{letter}", end="")


string = list(input())
stack = []

for i in range(len(string)):
    stack.append(string.pop())

print("".join(stack))
