from collections import deque

sequence = deque(list(input()))

fail_flag = False
if len(sequence) % 2 != 0:
    fail_flag = True

while sequence and not fail_flag:
    current_bracket = sequence.popleft()
    
    next_bracket = sequence.pop()

    if current_bracket == '(' and next_bracket == ')':
        continue

    elif current_bracket == '[' and next_bracket == ']':
        continue

    elif current_bracket == '{' and next_bracket == '}':
        continue

    else:
        fail_flag = True
        break

if fail_flag:
    print("NO")
else:
    print("YES")
