filename = "ru.txt"
file_mode = "a+"  # a+ mode allows reading and appending to the file

# Try to open the file for reading and appending
try:
    with open(filename, file_mode) as file:
        print("File exists. Appending text...")
        file.write("This is some additional text.\n")
except FileNotFoundError:
    # If the file doesn't exist, create it and write some text to it
    with open(filename, "w") as file:
        print("File does not exist. Creating file...")
        file.write("This is some text.\n")

# Read the contents of the file
with open(filename, "r") as file:
    file_contents = file.read()
    print("File contents:", file_contents)
