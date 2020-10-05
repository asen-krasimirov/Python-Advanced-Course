numbers = list(map(int, input().split()))

negatives = sum(filter(lambda x: x < 0, numbers))
positives = sum(filter(lambda x: x >= 0, numbers))

print(negatives)
print(positives)

if positives > abs(negatives):
    print("The positives are stronger than the negatives")
else:
    print("The negatives are stronger than the positives")
