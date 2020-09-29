text = input()

chars = sorted(set(text))

for char in chars:
    print(f"{char}: {text.count(char)} time/s")
