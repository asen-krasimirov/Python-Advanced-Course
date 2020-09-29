data = input().split()
stack = []

for _ in range(len(data)):
    element = data.pop()
    print(element, end=" ")
