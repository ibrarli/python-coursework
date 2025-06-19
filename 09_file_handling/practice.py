

with open("test.txt", "w") as file:
    for i in range(3):
        name = input("Enter a name: ")
        file.write(name + "\n")
     
with open("test.txt", "r") as file:
    contents = file.readlines()
   
    for index, content in enumerate(contents, start=1):
        print(f"{index}. {content.strip()}")