import csv
import json
import os

CSV_FILE = "students.csv"
JSON_FILE = "students.json"


def load_students():
    """Load student records from JSON if available, otherwise from CSV."""
    if os.path.exists(JSON_FILE):
        try:
            with open(JSON_FILE, "r", encoding="utf-8") as file:
                data = json.load(file)
                return data if isinstance(data, list) else []
        except (json.JSONDecodeError, OSError):
            print("Warning: Could not read JSON data. Starting with an empty list.")

    if os.path.exists(CSV_FILE):
        try:
            with open(CSV_FILE, "r", newline="", encoding="utf-8") as file:
                return list(csv.DictReader(file))
        except OSError:
            print("Warning: Could not read CSV data.")

    return []


def save_students(students):
    """Save student records to both JSON and CSV."""
    with open(JSON_FILE, "w", encoding="utf-8") as file:
        json.dump(students, file, indent=4)

    with open(CSV_FILE, "w", newline="", encoding="utf-8") as file:
        fieldnames = ["id", "name", "age", "course", "email"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(students)


def get_student_id(students):
    existing_ids = []
    for student in students:
        try:
            existing_ids.append(int(student["id"]))
        except (KeyError, ValueError):
            pass
    return max(existing_ids, default=0) + 1


def add_student(students):
    print("\n--- Add Student ---")
    name = input("Name: ").strip()
    age = input("Age: ").strip()
    course = input("Course: ").strip()
    email = input("Email: ").strip()

    if not name or not age or not course or not email:
        print("All fields are required.")
        return

    try:
        age = int(age)
        if age <= 0:
            raise ValueError
    except ValueError:
        print("Age must be a positive whole number.")
        return

    student = {
        "id": str(get_student_id(students)),
        "name": name,
        "age": str(age),
        "course": course,
        "email": email
    }

    students.append(student)
    save_students(students)
    print("Student added successfully.")


def view_students(students):
    print("\n--- Student Records ---")
    if not students:
        print("No student records found.")
        return

    for student in students:
        print(
            f"ID: {student['id']} | "
            f"Name: {student['name']} | "
            f"Age: {student['age']} | "
            f"Course: {student['course']} | "
            f"Email: {student['email']}"
        )


def find_student(students, student_id):
    return next(
        (student for student in students if student["id"] == str(student_id)),
        None
    )


def update_student(students):
    print("\n--- Update Student ---")
    student_id = input("Enter student ID: ").strip()
    student = find_student(students, student_id)

    if student is None:
        print("Student not found.")
        return

    print("Press Enter to keep the existing value.")
    name = input(f"Name [{student['name']}]: ").strip()
    age = input(f"Age [{student['age']}]: ").strip()
    course = input(f"Course [{student['course']}]: ").strip()
    email = input(f"Email [{student['email']}]: ").strip()

    if name:
        student["name"] = name

    if age:
        try:
            new_age = int(age)
            if new_age <= 0:
                raise ValueError
            student["age"] = str(new_age)
        except ValueError:
            print("Invalid age. Existing age was kept.")

    if course:
        student["course"] = course

    if email:
        student["email"] = email

    save_students(students)
    print("Student updated successfully.")


def delete_student(students):
    print("\n--- Delete Student ---")
    student_id = input("Enter student ID: ").strip()
    student = find_student(students, student_id)

    if student is None:
        print("Student not found.")
        return

    students.remove(student)
    save_students(students)
    print("Student deleted successfully.")


def search_student(students):
    print("\n--- Search Student ---")
    keyword = input("Enter name, course, or email: ").strip().lower()

    matches = [
        student for student in students
        if keyword in student["name"].lower()
        or keyword in student["course"].lower()
        or keyword in student["email"].lower()
    ]

    if not matches:
        print("No matching student found.")
        return

    for student in matches:
        print(
            f"ID: {student['id']} | Name: {student['name']} | "
            f"Age: {student['age']} | Course: {student['course']} | "
            f"Email: {student['email']}"
        )


def main():
    students = load_students()

    while True:
        print("\n===== Student Record Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        try:
            if choice == "1":
                add_student(students)
            elif choice == "2":
                view_students(students)
            elif choice == "3":
                search_student(students)
            elif choice == "4":
                update_student(students)
            elif choice == "5":
                delete_student(students)
            elif choice == "6":
                print("Thank you for using the Student Record Management System.")
                break
            else:
                print("Please enter a number from 1 to 6.")
        except (OSError, IOError) as error:
            print(f"File operation error: {error}")
        except Exception as error:
            print(f"Unexpected error: {error}")


if __name__ == "__main__":
    main()
