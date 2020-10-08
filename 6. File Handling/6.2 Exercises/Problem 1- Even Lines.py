banned_symbols = ["-", ",", ".", "!", "?"]  # We save the banned symbols in a variable


with open("input.txt") as file:  # We open the input file

    line_counter = -1  # We make a line counter, to track witch line we are on
    for line in file:

        line_counter += 1  # We increment 1 index to the counter
        if line_counter % 2 != 0:  # We check if the line is even
            continue

        new_line = line  # We save the line in a variable to save all changes
        for symbol in banned_symbols:  # We loop true all banned symbols and replace them with "@"
            new_line = new_line.replace(symbol, "@")

        reversed_line_list = new_line.split()[::-1]  # We cast the new line to list and we reverse the words with slice
        print(" ".join(reversed_line_list))  # We print the new line with reversed words
