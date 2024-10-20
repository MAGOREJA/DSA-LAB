# Initial list of students
students = ["Alice", "Bob", "Charlie"]

def add_student(name):
    students.append(name)
    print(f"{name} has been added to the class.")

def remove_student(name):
    if name in students:
        students.remove(name)
        print(f"{name} has been removed from the class.")
    else:
        print(f"{name} is not in the class.")

def display_students():
    print("List of students in the class:")
    for student in students:
        print(student)

# Test the functions
add_student("David")
remove_student("Charlie")
display_students()
