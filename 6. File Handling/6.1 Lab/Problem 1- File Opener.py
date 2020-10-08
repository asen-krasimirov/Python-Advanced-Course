

try:
    f = open(r".\08-File-Handling-Lab-Resources\File Opener\text.txt", "r")
    print("File found")
    f.close()
except FileNotFoundError:
    print("File not found")
