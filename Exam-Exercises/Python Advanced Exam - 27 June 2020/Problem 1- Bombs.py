from collections import deque


def is_pouch_full(bomb_pouch_):

    # counter = 0
    # for count in bomb_pouch_.values():
    #     if count >= 3:
    #         counter += 1
    #
    # if counter == 3:
    #     return True
    # return False

    return all([count >= 3 for count in bomb_pouch_.values()])


def print_final_results(bomb_pouch_full_, bomb_effects_, bomb_casings_, bomb_pouch_):

    if bomb_pouch_full_:
        print("Bene! You have successfully filled the bomb pouch!")
    else:
        print("You don't have enough materials to fill the bomb pouch.")

    # if bomb_effects_:
    #     print(f"Bomb Effects: {', '.join([str(x) for x in bomb_effects])}")
    # else:
    #     print("Bomb Effects: empty")

    print(f"Bomb Effects: {', '.join([str(x) for x in bomb_effects]) if bomb_effects_ else 'empty'}")

    # if bomb_casings_:
    #     print(f"Bomb Casings: {', '.join([str(x) for x in bomb_casings])}")
    # else:
    #     print("Bomb Casings: empty")

    print(f"Bomb Casings: {', '.join([str(x) for x in bomb_casings]) if bomb_casings_ else 'empty'}")

    for bomb_name_, count in sorted(bomb_pouch_.items()):
        print(f"{bomb_name_}: {count}")


bomb_pouch = {
    "Cherry Bombs": 0,
    "Datura Bombs": 0,
    "Smoke Decoy Bombs": 0
}

bomb_pouch_full = False

bomb_effects = deque(map(int, input().split(", ")))
bomb_casings = deque(map(int, input().split(", ")[::-1]))

bomb_values = {
    40: "Datura Bombs",
    60: "Cherry Bombs",
    120: "Smoke Decoy Bombs"
}

while bomb_effects and bomb_casings:

    loc_effect = bomb_effects.popleft()
    loc_casing = bomb_casings.popleft()

    loc_sum = loc_effect + loc_casing

    if loc_sum in bomb_values:
        bomb_name = bomb_values[loc_sum]
        bomb_pouch[bomb_name] += 1

        bomb_pouch_full = is_pouch_full(bomb_pouch)

        if bomb_pouch_full:
            break

        continue

    loc_casing -= 5
    if loc_casing >= 0:
        bomb_casings.appendleft(loc_casing)
    bomb_effects.appendleft(loc_effect)


print_final_results(bomb_pouch_full, bomb_effects, bomb_casings, bomb_pouch)
