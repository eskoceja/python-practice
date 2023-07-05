from bcolors import bcolors

students = []

def addStudents():
    name = input(bcolors.OKBLUE + "Enter student name: \n" + bcolors.ENDC)
    studentId = input(bcolors.OKBLUE + "Enter student ID: \n" + bcolors.ENDC)
    grade = input(bcolors.OKBLUE +
                  "Enter student grade-level: \n" + bcolors.ENDC)

    student = {
        'name': name,
        'id': studentId,
        'grade': grade
    }

    students.append(student)
    print(bcolors.OKGREEN + "Student added successfully!\n" + bcolors.ENDC)

def displayStudents():
    if not students:
        print(bcolors.WARNING +
              "Student not found in database, try another name or Id\n" + bcolors.ENDC)
    else:
        for student in students:
            print(bcolors.OKCYAN +
                  f"Name: {student['name']}\nID: {student['id']}\nGrade: {student['grade']}\n" + bcolors.ENDC)

def searchStudents():
    if not students:
        print(bcolors.WARNING +
              "Student not found in database, try another name or Id\n" + bcolors.ENDC)
        return

    searchKey = input(
        bcolors.OKBLUE + "Enter student name or ID to find: \n" + bcolors.ENDC)

    foundStudents = []

    for student in students:
        if searchKey.lower() in student['name'].lower() or searchKey.lower() in student['id'].lower():
            foundStudents.append(student)

    if foundStudents:
        for student in foundStudents:
            print(bcolors.OKCYAN +
                      f"Name: {student['name']}\nID: {student['id']}\nGrade: {student['grade']}\n" + bcolors.ENDC)
    else:
        print(
            bcolors.WARNING + "Student not found in database, try another name or Id\n" + bcolors.ENDC)

def deleteStudents():
    if not students:
        print(bcolors.WARNING +
              "Student not found in database, try another name or Id\n" + bcolors.ENDC)
        return

    searchKey = input(
        bcolors.OKBLUE + "Enter student name or ID to find: \n" + bcolors.ENDC)

    foundStudents = []

    for student in students:
        if searchKey.lower() in student['name'].lower() or searchKey.lower() in student['id'].lower():
            foundStudents.append(student)

    if foundStudents:
        for student in foundStudents:
            students.remove(student)
            print(bcolors.OKGREEN +
                      "Student deleted successfully!\n" + bcolors.ENDC)
    else:
        print(
            bcolors.WARNING + "Student not found in database, try another name or Id\n" + bcolors.ENDC)

def menu():
    options = """Student Management System
    1. Add student
    2. Search for a student
    3. Display all students
    4. Delete a student
    5. Exit"""

    while True:
        print(bcolors.HEADER + options + bcolors.ENDC)
        choice = int(
            input(bcolors.HEADER + "Enter your choice: \n" + bcolors.ENDC))

        try:
            if choice == 1:
                addStudents()
            elif choice == 2:
                searchStudents()
            elif choice == 3:
                displayStudents()
            elif choice == 4:
                deleteStudents()
            elif choice == 5:
                print(bcolors.BOLD + "Good-bye!" + bcolors.ENDC)
                break
            else:
                print(
                    bcolors.WARNING + "Invalid entry, choose an options between 1-5\n" + bcolors.ENDC)
        except Exception as e:
            print(bcolors.FAIL + f"Error: {str(e)}" + bcolors.ENDC)

menu()
