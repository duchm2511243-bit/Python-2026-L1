def input_students():
    n = int(input("Enter the number of students in class: "))
    students = []
    
    for i in range(n):
        print(f"\n--- Enter info for student {i} ---")
        student_id = input("Enter student ID: ")
        name = input("Enter name: ")
        dob = input("Enter date of birth: ")
                
        student = {
            "id": student_id,
            "name": name,
            "dob": dob,
            "marks": {}
        }
        students.append(student)
        
    return students


def select_course():
    courses = ["Python", "Math", "English"]
    print("\nAvailable courses:")
    for number, course in enumerate(courses, start=1):
        print(f"{number}. {course}")

    choice = int(input("Select a course (1-3): "))
    if 1 <= choice <= len(courses):
        return courses[choice - 1]
    
    print("Invalid course selection")
    return None


def input_marks_for_all(students, course):
    print(f"\n--- Entering marks for course: {course} ---")
    for student in students:
        while True:
            marks = float(input(f"Enter marks for {student['name']} (ID: {student['id']}) (0-20): "))
            if 0 <= marks <= 20:
                student["marks"][course] = marks
                break
            else:
                print("Marks must be between 0 and 20. Try again!")


def display_results(students):
    print("\n CLASS RESULTS ")
    for s in students:
        print(f"ID: {s['id']} | Name: {s['name']} | DoB: {s['dob']}")
        print("   Marks:", s["marks"])


students_list = input_students()
selected_course = select_course()

if selected_course and students_list:
    input_marks_for_all(students_list, selected_course)
    display_results(students_list)


    