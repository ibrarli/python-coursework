courses = ("a","b", "c", "d", "e", "f", "g", "h", "i", "j")
students = []
cities = set()

for i in range(5):
    print (f"\n Student {i+1}")
    name = input("Enter student name: ")
    city = input("Enter student city: ")
    course = input(f"Enter student course {"/".join(courses)}: ")

    if course not in courses:
        print("Invalid course. Please try again.")
        continue

    student = {
        "name": name,
        "city": city,
        "course": course
    }  

    students.append(student)
    cities.add(city)

print ("\nSummary of Students:")
print (f"Total number of students: {len(students)}")
print (f"Unique cities: {cities}")

for student in students:
    print (f"Name: {student['name']}, City: {student['city']}, Course: {student['course']}")