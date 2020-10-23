# Numbers Dictionary


numbers_dictionary = {}  # Creates a dict to keep the numbers

try:
    while True:  # First loop- Entering numbers as text and saving their values

        text_number = input()
        if text_number == "Search":  # if the name of the number is "Search" breaks the loop
            break

        number_value = int(input())
        numbers_dictionary[text_number] = number_value

    while True:  # Second loop- Searching in the dict by name (key)

        text_number = input()
        if text_number == "Remove":  # if the name is "Remove" continues with the next loop
            break

        print(numbers_dictionary[text_number])

    while True:  # Final loop- Removes by name (key)

        text_number = input()
        if text_number == "End":  # ends the loop when "End" is given as a number name
            break

        numbers_dictionary.pop(text_number)

except ValueError:  # expects an exception in the first loop and handles it
    print("The variable number must be an integer")

except KeyError:  # expects an exception in the second and third loop and handles it
    print("Number does not exist in dictionary")

finally:
    print(numbers_dictionary)  # no matter what, prints the final state of the dict
