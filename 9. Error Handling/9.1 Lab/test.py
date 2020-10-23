

try:
    string = input()
    repeated_times = int(input())
    print(string*repeated_times)
except ValueError:
    print("Variable times must be an integer")

