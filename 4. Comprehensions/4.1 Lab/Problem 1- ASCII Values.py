letters = input().split(", ")
ascii_values = {letter: ord(letter) for letter in letters}
print(ascii_values)

# one-line
# print({n: ord(n) for n in input().split(", ")})
