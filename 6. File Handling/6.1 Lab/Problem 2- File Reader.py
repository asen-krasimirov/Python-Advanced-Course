file = open(r".\08-File-Handling-Lab-Resources\File Reader\numbers.txt", "r")

total_sum = 0
for line in file:
    total_sum += int(line)
print(total_sum)

file.close()


# Another Solution

# print(sum([int(line) for line in open(r".\08-File-Handling-Lab-Resources\File Reader\numbers.txt", "r")]))
