countries = input().split(", ")
capitals = input().split(", ")

total_count = len(countries)

combined_information = {countries[i]: capitals[i] for i in range(total_count)}

for name, capital in combined_information.items():
    print(f"{name} -> {capital}")

# Alternative Solution
# countries = input().split(", ")
# capitals = input().split(", ")
#
# combined_information = zip(countries, capitals)
#
# for name, capital in combined_information:
#     print(f"{name} -> {capital}")

# Alternative Solution  #2
# countries = input().split(", ")
# capitals = input().split(", ")
#
# [print(f"{name} -> {capital}") for name, capital in zip(countries, capitals)]
