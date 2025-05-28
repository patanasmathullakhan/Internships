import json
import os

FILENAME = "students.json"

# Load data
def load_data():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, "r") as file:
        return json.load(file)

# Save data
def save_data(data):
    with open(FILENAME, "w") as file:
        json.dump(data, file, indent=4)

# Add student
def add_student():
    student = {
        "roll_no": input("Enter Roll Number: "),
        "name": input("Enter Name: "),
        "age": input("Enter Age: "),
        "branch": input("Enter Branch: ")
    }
    data = load_data()
    data.append(student)
    save_data(data)
    print("Student added successfully!")

# View all students
def view_students():
    data = load_data()
    if not data:
        print("No student records found.")
        return
    for student in data:
        print(f"Roll No: {student['roll_no']}, Name: {student['name']}, Age: {student['age']}, Branch: {student['branch']}")

# Search student
def search_student():
    roll_no = input("Enter Roll Number to Search: ")
    data = load_data()
    for student in data:
        if student["roll_no"] == roll_no:
            print(f"Found: {student}")
            return
    print("Student not found.")

# Update student
def update_student():
    roll_no = input("Enter Roll Number to Update: ")
    data = load_data()
    for student in data:
        if student["roll_no"] == roll_no:
            student["name"] = input("Enter New Name: ")
            student["age"] = input("Enter New Age: ")
            student["branch"] = input("Enter New Branch: ")
            save_data(data)
            print("Student record updated.")
            return
    print("Student not found.")

# Delete student
def delete_student():
    roll_no = input("Enter Roll Number to Delete: ")
    data = load_data()
    new_data = [s for s in data if s["roll_no"] != roll_no]
    if len(data) == len(new_data):
        print("Student not found.")
    else:
        save_data(new_data)
        print("Student deleted.")

# Menu
def menu():
    while True:
        print("\nStudent Record Management")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            update_student()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

# Run the app
menu()
