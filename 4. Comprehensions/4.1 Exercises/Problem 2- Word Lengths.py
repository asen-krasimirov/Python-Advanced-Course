names = input().split(", ")

lengths_names = [
    f"{name} -> {len(name)}"
    for name in names
]

print(", ".join(lengths_names))

# one-liner
# print(", ".join([f'{name} -> {len(name)}'for name in input().split(", ")]))
