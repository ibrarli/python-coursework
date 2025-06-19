# Ask the user to enter 3 names. Save all names to a file called names.txt, one name per line.

with open("names.txt", "w") as file:
    for i in range(3):
        name = input("Enter a name: ")
        file.write(name + "\n")

with open("class.txt", "a" ) as file:
    for i in range(3):
        classroom = input("Enter a class: ")
        file.write (classroom + "\n")