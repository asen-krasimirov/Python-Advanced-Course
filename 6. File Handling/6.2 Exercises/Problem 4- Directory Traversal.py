from collections import defaultdict
import os
import re


directory = input("Enter a directory to traverse through: ")  # Gets a directory to traverse through

# Creates or overwrites a file report.txt on the desktop
# (the desktop may have different directory on different computes)
with open("C:\\Users\\Game\\Desktop\\report.txt", "w") as report_file:

    file = tuple(os.walk(directory))  # Creates a tuple with a tree of the given directory
    level_one_files = file[0][2]  # Gets only the first level of files (open the os.walk documentation to read more)

    all_files = defaultdict(list)  # Creates a dictionary with a list default value

    for file in level_one_files:  # Goes through all files in the level

        file_extension = re.findall(r".+\.([A-Za-z]+)", file)[0]  # Gets the extension of the file
        all_files[file_extension].append(file)  # Appends the file in a list with all files with the same extension


# Get the extension and the list of files with the same extension.The extensions and all files are sorted alphabetically
    for extension, files in sorted(all_files.items(), key=lambda x: (x[0], x[1])):
        print(f".{extension}", file=report_file)  # Print the extension in the report.txt file on the desktop
        for file in files:  # Print every element from the list in the report.txt file
            print(f"- - - {file}", file=report_file)

# To see the process better delete the comments and use the debugger
