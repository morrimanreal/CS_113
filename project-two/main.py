import sqlite3
import os


def connect_database():
    database = "players.db"

    # Check if database exists
    if not os.path.exists(database):
        print("Database does not exist.")
        print("Creating database...")

    # Connect to database
    # This also creates it if it doesn't exist
    connection = sqlite3.connect(database)

    print("Connected to database.")

    return connection

def create_table(connection):
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            name TEXT,
            grade TEXT,
            email TEXT
        )
    """)

    connection.commit()

    print("Students table created.")
    
    
# Validate ID
def get_id(message):
    while True:
        try:
            student_id = int(input(message))
            return student_id
        except ValueError:
            print("Invalid ID. Please enter a whole number.")


# Validate email
def get_email():
    while True:
        email = input("Enter student email: ")

        if "@" in email:
            return email
        else:
            print("Invalid email. Email must contain @.")
    
    
def add_student(connection):
    student_id = get_id("Enter student ID: ")
    name = input("Enter student name: ")
    grade = input("Enter student grade: ")
    email = get_email()

    cursor = connection.cursor()

    try:
        cursor.execute("""
            INSERT INTO students (id, name, grade, email)
            VALUES (?, ?, ?, ?)
        """, (student_id, name, grade, email))

        connection.commit()
        print("Student added successfully!")

    except sqlite3.IntegrityError:
        print("That student ID already exists.")


def view_students(connection):
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM students")

    students = cursor.fetchall()
    
    if len(students) == 0:
        print("No student records found.")
        return

    print("\n--- Student Records ---")

    for student in students:
        print("ID:", student[0])
        print("Name:", student[1])
        print("Grade:", student[2])
        print("Email:", student[3])
        print("----------------------")


def update_student(connection):
    student_id = get_id("Enter student ID to update: ")

    name = input("Enter new name: ")
    grade = input("Enter new grade: ")
    email = get_email()

    cursor = connection.cursor()

    cursor.execute("""
        UPDATE students
        SET name = ?, grade = ?, email = ?
        WHERE id = ?
    """, (name, grade, email, student_id))

    connection.commit()

    print("Student updated successfully!")


def delete_student(connection):
    student_id = get_id("Enter student ID to delete: ")

    cursor = connection.cursor()
    
     # Check if student exists
    cursor.execute(
        "SELECT * FROM students WHERE id = ?",
        (student_id,)
    )

    student = cursor.fetchone()

    if student is None:
        print("Student not found.")
        return

    print("\nStudent:", student[1])
    print("Grade:", student[2])
    print("Email:", student[3])

    # Ask before deleting
    confirm = input("Are you sure you want to delete this student? (y/n): ")

    if confirm.lower() == "y":
        cursor.execute(
            "DELETE FROM students WHERE id = ?",
            (student_id,)
        )

        connection.commit()
        print("Student deleted successfully!")

    else:
        print("Delete canceled.")

    
    # cursor.execute("""
    #     DELETE FROM students
    #     WHERE id = ?
    # """, (student_id,))

    # connection.commit()

    # print("Student deleted successfully!")


def display_menu():
    print("\n--- Student Database ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")



def main():
    connection = connect_database()

    # Database code goes here
    create_table(connection)
    
    while True:

        display_menu()

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student(connection)

        elif choice == "2":
            view_students(connection)

        elif choice == "3":
            update_student(connection)

        elif choice == "4":
            delete_student(connection)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1-5.")

    connection.close()


main()