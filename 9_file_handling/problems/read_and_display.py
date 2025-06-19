#Read from names.txt and display each name with numbering.

with open("names.txt", "r") as file:
    lines = file.readlines()
    for index, name in enumerate(lines, start=1):
        print(f"{index}. {name.strip()}")
