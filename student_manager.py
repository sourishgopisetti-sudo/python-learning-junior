# student_manager.py
# A simple command-line program to manage student records

import json
import os

DATA_FILE = "students.json"


def load_students():
    # Load student data from the JSON file, if it exists
    if os.path.exists(DATA_FILE):
        file = open(DATA_FILE, "r")
        students = json.load(file)
        file.close()
        return students
    else:
        return []


def save_students(students):
    # Save the current list of students to the JSON file
    file = open(DATA_FILE, "w")
    json.dump(students, file, indent=4)
    file.close()
    print("Data saved to", DATA_FILE)


def add_student(students):
    name = input("Enter student name: ")
    major = input("Enter student major: ")
    year = input("Enter student year: ")

    new_student = {
        "name": name,
        "major": major,
        "year": year
    }

    students.append(new_student)
    print(name, "was added.")


def remove_student(students):
    name = input("Enter the name of the student to remove: ")
    found = False

    for student in students:
        if student["name"].lower() == name.lower():
            students.remove(student)
            found = True
            print(name, "was removed.")
            break

    if not found:
        print("Student not found.")

def update_student(students):
    name = input("Enter the name of the student to update: ")
    found = False

    for student in students:
        if student["name"].lower() == name.lower():
            found = True
            new_major = input("Enter new major (leave blank to keep the same): ")
            new_year = input("Enter new year (leave blank to keep the same): ")

            if new_major != "":
                student["major"] = new_major
            if new_year != "":
                student["year"] = new_year

            print(name, "was updated.")

    if not found:
        print("Student not found.")


def search_student(students):
    name = input("Enter the name of the student to search for: ")
    found = False

    for student in students:
        if student["name"].lower() == name.lower():
            found = True
            print("Name:", student["name"])
            print("Major:", student["major"])
            print("Year:", student["year"])

    if not found:
        print("Student not found.")


def show_all_students(students):
    if len(students) == 0:
        print("No students yet.")
    else:
        for student in students:
            print(student["name"], "-", student["major"], "- Year", student["year"])


def main():
    students = load_students()

    while True:
        print("\n--- Student Management Menu ---")
        print("1. Add a student")
        print("2. Remove a student")
        print("3. Search for a student")
        print("4. Show all students")
        print("5. Update a student")
        print("6. Save and quit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            remove_student(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            show_all_students(students)
        elif choice == "5":
            update_student(students)
        elif choice == "6":
            save_students(students)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()