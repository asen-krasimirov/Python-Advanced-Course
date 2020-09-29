vowels = {'a', 'o', 'u', 'e', 'i'}
text = input()
new_text = [
    n
    for n in text
    if n.lower() not in vowels
]
print(''.join(new_text))

# one-liner
# print(''.join([n for n in input() if n.lower() not in {"a", "o", "u", "e", "i"}]))
