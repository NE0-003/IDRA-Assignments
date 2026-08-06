students = []


def add_student():
    student = {}

    student["ID"] = input("Enter Student ID: ")
    student["Name"] = input("Enter Student Name: ")
    student["Age"] = int(input("Enter Age: "))
    student["Course"] = input("Enter Course: ")
    student["Marks"] = float(input("Enter Marks: "))

    students.append(student)
    print("Student added successfully.\n")


def view_students():
    if len(students) == 0:
        print("No student records found.\n")
        return

    print("\nStudent Records")
    print("-" * 60)

    for student in students:
        print("ID:", student["ID"])
        print("Name:", student["Name"])
        print("Age:", student["Age"])
        print("Course:", student["Course"])
        print("Marks:", student["Marks"])
        print("-" * 60)


def search_student():
    if len(students) == 0:
        print("No student records found.\n")
        return

    print("1. Search by ID")
    print("2. Search by Name")
    choice = input("Enter choice: ")

    found = False

    if choice == "1":
        sid = input("Enter Student ID: ")

        for student in students:
            if student["ID"] == sid:
                print(student)
                found = True
                break

    elif choice == "2":
        name = input("Enter Student Name: ").lower()

        for student in students:
            if student["Name"].lower() == name:
                print(student)
                found = True

    if not found:
        print("Student not found.\n")


def update_student():
    if len(students) == 0:
        print("No student records found.\n")
        return

    sid = input("Enter Student ID to update: ")

    for student in students:
        if student["ID"] == sid:
            student["Name"] = input("Enter New Name: ")
            student["Age"] = int(input("Enter New Age: "))
            student["Course"] = input("Enter New Course: ")
            student["Marks"] = float(input("Enter New Marks: "))
            print("Student updated successfully.\n")
            return

    print("Student not found.\n")


def delete_student():
    if len(students) == 0:
        print("No student records found.\n")
        return

    sid = input("Enter Student ID to delete: ")

    for student in students:
        if student["ID"] == sid:
            students.remove(student)
            print("Student deleted successfully.\n")
            return

    print("Student not found.\n")


while True:
    print("\nStudent Management System")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("Program Closed")
        break

    else:
        print("Invalid choice. Try again.\n")