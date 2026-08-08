students = []

while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Student Name: ")
        roll = input("Enter Roll Number: ")

        student = {
            "name": name,
            "roll": roll
        }

        students.append(student)

        print("\nStudent Added Successfully!")
        print("Name:", name)
        print("Roll:", roll)

    elif choice == "2":
        print("\n====STUDENTS====")
        for student in students:
            print("name:",student["name"])
            print("roll:",student["roll"])
        

    elif choice == "3":
        print("Search Student")

    elif choice == "4":
        print("Update Student")

    elif choice == "5":
        print("Delete Student")

    elif choice == "6":
        print("Thank you for using Student Management System!")
        break

    else:
        print("Invalid choice!")