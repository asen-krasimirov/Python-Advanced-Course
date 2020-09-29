def isBalanced(string):
    if len(string) % 2 != 0:
        return "NO"

    for i in range(len(string) // 2):
        char = string[i]
        next_char = string[len(string)-(i+1)]
        if char == '(' and next_char != ')':
            return "NO"

        if char == '[' and next_char != ']':
            return "NO"

        if char == '{' and next_char != '}':
            return "NO"

    return "YES"


sequence = input()
result = isBalanced(sequence)
print(result)

# for i in range(len(sequence) // 2):
#     char = sequence[i]
#     next_char = sequence[len(sequence) - (i + 1)]
#     if char == '(' and next_char != ')':
#         # return "NO"
#         print("NO")
#         break
#
#     if char == '[' and next_char != ']':
#         # return "NO"
#         print("NO")
#         break
#
#     if char == '{' and next_char != '}':
#         # return "NO"
#         print("NO")
#         break
