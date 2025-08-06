
"""This is the entry point for the student gradebook system.

The gradebook system will handle the following tasks:
    - Add a new student (without grading information)
    - Add a student grading information (accepts as many as user wants)
    - Search for students by their name
    - Search for student by their ID
    - Search for students studying a particular course
    - List all students with their ID, Name, Grade, Course
"""

gradebook = []

print("WELCOME TO THE GRADEBOOK MANAGEMENT SYSTEM\n\n")

actions = [
    "Add a new student",
    "Add a student grading information",
    "Search for students by their name",
    "Search for student by their ID",
    "Search for students studying a particular course",
    "Delete a student",
    "Delete a student grading information",
    "List all students with their ID, Name, Grade, Course",
    "Quit"
]
while True:
    for number, action in enumerate(actions, start=1):
        print(f"{number}. {action}")

    # getting to choose your option
    choice = input("Enter your choice: ")

    # Add student name and ID
    if choice == '1':
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ").title()
        gradebook.append({"id": student_id, "name": name,
                         "grades": {}, "marks": {}})
        print(f"{name.title()} added successfully.")

    # Adding student ID, course and grade
    elif choice == '2':
        student_id = input("Enter student ID to add grades: ")
        for student in gradebook:
            if student["id"] == student_id:
                course = input("Enter course name: ")
                marks = input(f"Enter the marks for {course.title()}: ")
                grade = input(f"Enter the grade for {course.title()}: ")
                student["marks"][course] = marks
                student["grades"][course] = grade
                print(f"Grades updated for {student['name']}.")
                break
        else:
            print("Student not found.")

    # Search for student by name
    elif choice == '3':
        name = input("Enter name to search: ")
        for student in gradebook:
            if student["name"].lower() == name.lower():
                print(f"\nID: {student['id']}, Name: {student['name']}")
                if student["grades"]:
                    print("Courses and Grades")
                    for course, grade in student["grades"].items():
                        print(f" {course}: {grade}")
                else:
                    print("No Grades Yet")
                    break
            else:
                print("no student found with that name.")
    elif choice == '4':
        student_id = input("Enter student ID to search: ")
        for student in gradebook:
            if student["id"] == student_id:
                print(f"\nID: {student['id']}, Name: {student['name']}")
                if student["grades"]:
                    print("Course, Marks and Grades")
                    for (course, marks, grade) in student["grades"].items():
                        print(f" {course}: {marks}: {grade}")
                        break
                else:
                    print("No Grades Yet")
            else:
                print("no student found with that name")
    elif choice == '5':
        course_name = input("Enter course name to search: ")
        for student in gradebook:
            if course_name in student["grades"]:
                print(f"\nID: {student['id']}, Name: {student['name']}")
                print(f"  {course_name}: {student['grades'][course_name]}")
        else:
            print("no students found studying that course.")
    elif choice == '6':
        student_id = input("Enter student ID to delete: ")
        for i, student in enumerate(gradebook):
            if student["id"] == student_id:
                del gradebook[i]
                print("Student deleted successfully.")
                break
        else:
            print("student not found.")
    elif choice == '7':
        student_id = input("Enter student ID to delete grading information: ")
        for student in gradebook:
            if student["id"] == student_id:
                course = input("Enter course name to delete grade: ")
                if course in student["grades"]:
                    del student["grades"][course]
                    print(f"Grade for {course} deleted successfully.")
                else:
                    print("No grade found for that course.")
                break
        else:
            print("Student not found.")
    elif choice == '8':
        if not gradebook:
            print("No students in the gradebook.")
        else:
            print("\nList of all students:")
            for student in gradebook:
                print(f"ID: {student['id']}, Name: {student['name']}")
                if student["grades"]:
                    print("Courses and Grades:")
                    for course, grade in student["grades"].items():
                        print(f"  {course}: {grade}")
                else:
                    print("  No Grades Yet")
    elif choice == '9':
        print("Exiting the gradebook system. Goodbye!")
        break
else:
    print("Invalid choice. Please try again.")
