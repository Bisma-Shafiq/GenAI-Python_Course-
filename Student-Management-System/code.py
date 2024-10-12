def manage_student_database():
    students = []
    student_names = set()
    student_id = 1

    while True:
        name = input("Enter student name (or type 'stop' to finish): ").strip()

        if name.lower() == "stop":
            break

        if name in student_names:
            print("Duplicate name found. Please enter a different name.")
            continue

        student_names.add(name)
        students.append((student_id, name))
        student_id += 1

    print("\nList of students:")
    for student in students:
        print(student)

    print("\nIndividual student details:")
    for student in students:
        print(f"ID: {student[0]}, Name: {student[1]}")

    total_students = len(students)
    print(f"\nTotal number of students: {total_students}")

    total_length = sum(len(student[1]) for student in students)
    print(f"Total length of all student names combined: {total_length}")

    if students:
        longest_student = max(students, key=lambda student: len(student[1]))
        shortest_student = min(students, key=lambda student: len(student[1]))
        print(f"\nStudent with the longest name: ID: {longest_student[0]}, Name: {longest_student[1]}")
        print(f"Student with the shortest name: ID: {shortest_student[0]}, Name: {shortest_student[1]}")
    else:
        print("No students were entered.")
manage_student_database()