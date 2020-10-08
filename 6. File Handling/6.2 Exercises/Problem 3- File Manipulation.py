import os


while True:
    data = input().split("-")
    command = data[0]  # Saves the command

    if command == "End":  # If the command is "End" the program stops
        break

    file_name = data[1]  # Saves the name, all commands use it

    if command == "Create":
        """
        Creates a new file.
        If there is such file, overwrites it.
        """

        with open(file_name, "w"):
            pass

    elif command == "Add":
        """
        Adds to the end of a file.
        If there isn't such file, creates it and writes inside it.
        """

        content = data[2]
        with open(file_name, "a") as file:
            file.write(content + "\n")  # Adds additional new line symbol

    elif command == "Replace":
        """
        Opens a file, gets it's content and overwrites the file with replaced strings.
        """

        old_string = data[2]
        new_string = data[3]

        if not os.path.exists(file_name):  # If the file does not exists trows an skips the command
            print("An error occurred")
            continue

        with open(file_name) as file:  # Gets the content
            file_content = file.readlines()

        with open(file_name, "w") as file:  # Replaces all old strings with new ones

            for line_ in file_content:
                line = line_.replace(old_string, new_string)

                file.write(line)

    elif command == "Delete":
        """
        Deletes the file if it exists.
        """

        if not os.path.exists(file_name):
            print("An error occurred")
            continue

        os.remove(file_name)
