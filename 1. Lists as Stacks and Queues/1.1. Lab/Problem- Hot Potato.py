from collections import deque

kid_circle = deque(input().split())
tosses = int(input())

while len(kid_circle) > 1:
    kid_circle.rotate(-tosses)
    leaves = kid_circle.pop()

    print(f"Removed {leaves}")

winner = kid_circle.popleft()
print(f"Last is {winner}")
