total_information = {
    "Categories":
    {
        category: []
        for category in input().split(", ")
    },
    "Quantity": 0,
    "Quality": 0
}

command_number = int(input())
for _ in range(command_number):
    category, item, *other = input().split(' - ')

    quantity_information, quality_information = other[0].split(";")
    _, quantity = quantity_information.split(":")
    _, quality = quality_information.split(":")

    total_information["Categories"][category].append(item)
    total_information["Quantity"] += int(quantity)
    total_information["Quality"] += int(quality)

total_quantity = total_information["Quantity"]
total_quality = total_information["Quality"]
all_categories = total_information["Categories"]

print(f"Count of items: {total_quantity}")
print(f"Average quality: {total_quality/len(all_categories) :.2f}")

for category in all_categories:
    print(f"{category} -> {', '.join(all_categories[category])}")
