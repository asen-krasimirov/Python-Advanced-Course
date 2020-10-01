hero_information = {
    name: {
        "Inventory": [],
        "Total_Cost": 0
    }
    for name in input().split(", ")
}

while True:
    command = input()
    if command == "End":
        break

    name, item, cost = command.split("-")

    if item in hero_information[name]["Inventory"]:
        continue

    hero_information[name]["Inventory"].append(item)
    hero_information[name]["Total_Cost"] += int(cost)

for name in hero_information:
    inventory = hero_information[name]["Inventory"]
    total_cost = hero_information[name]["Total_Cost"]

    print(f"{name} -> Items: {len(inventory)}, Cost: {total_cost}")
