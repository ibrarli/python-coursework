filename = input("Enter file name: ")

try:
    with open(filename, "r") as file:
        print(file.read())
except FileNotFoundError:
    print("❌ File not found.")
