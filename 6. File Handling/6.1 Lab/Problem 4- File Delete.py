import os


file_path = r"my_first_file.txt"
if os.path.exists(file_path):
    os.remove(file_path)
else:
    print("File already deleted!")

# Alternative Solution

# file = open("my_first_file.txt", "x")
#
# try:
#     os.remove("my_first_file.txt")
# except FileNotFoundError:
#     print("File already deleted!")
#
