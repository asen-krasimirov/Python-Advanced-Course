# numbers = list(map(int, input().split(", ")))
#
# sorted_numbers = {
#     "Positive": [str(num) for num in numbers if num >= 0],
#     "Negative": [str(num) for num in numbers if num < 0],
#     "Even": [str(num) for num in numbers if num % 2 == 0],
#     "Odd": [str(num) for num in numbers if num % 2 != 0]
# }
#
# for category in sorted_numbers:
#     print(f"{category}: {', '.join(sorted_numbers[category])}")

# Alternative Solution
numbers = list(map(int, input().split(", ")))

print(f"Positive: {', '.join([str(num) for num in numbers if num >= 0])}")
print(f"Negative: {', '.join([str(num) for num in numbers if num < 0])}")
print(f"Even: {', '.join([str(num) for num in numbers if num % 2 == 0])}")
print(f"Odd: {', '.join([str(num) for num in numbers if num % 2 != 0])}")
