from string import punctuation  # Import punctuations to make a check later (18 line)

# Open a file with the input and create/overwrite a new output file
with open("input.txt") as read_file, open("output.txt", "w") as write_file:
    line_counter = 0  # Create a line counter
    for line_ in read_file:
        line_counter += 1  # Increment on each line

        line = line_[:-1]  # Use slice to remove the new line symbol ("\n") on the end of the line

        letter_counter = 0  # Create a letter counter
        punctuation_counter = 0  # Create a punctuation counter

        for elem in line:  # Loop true each element of the line
            if elem.isalpha():  # Check if the element is a letter
                letter_counter += 1

            elif elem in punctuation:  # Check if the element is a punctuation mark
                punctuation_counter += 1

        # Print all the necessary information in the output file
        print(f"Line {line_counter}: {line} ({letter_counter})({punctuation_counter})", file=write_file)
