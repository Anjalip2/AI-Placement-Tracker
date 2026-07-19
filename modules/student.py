from modules.database import get_connection
from modules.validation import validate_name, validate_usn, validate_cgpa


def add_student():
    name = input("Enter your name: ")

    if not validate_name(name):
        print("Invalid Name!")
        return

    usn = input("Enter your USN: ")

    if not validate_usn(usn):
        print("Invalid USN!")
        return

    branch = input("Enter your branch: ")

    try:
        cgpa = float(input("Enter your CGPA: "))

        if not validate_cgpa(cgpa):
            print("CGPA should be between 0 and 10.")
            return

    except ValueError:
        print("Invalid CGPA!")
        return

    connection = get_connection()
    cursor = connection.cursor()

    query = """
    INSERT INTO students (usn, name, branch, cgpa)
    VALUES (%s, %s, %s, %s)
    """

    values = (usn, name, branch, cgpa)

    try:
        cursor.execute(query, values)
        connection.commit()
        print("Student added successfully!")

    except Exception as e:
        if "Duplicate entry" in str(e):
            print("USN already exists!")
        else:
            print("Error:", e)

    finally:
        cursor.close()
        connection.close()


def view_students():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    if not students:
        print("No students found.")
    else:
        print("\n========== Student Records ==========\n")

        for student in students:
            print(f"USN    : {student[0]}")
            print(f"Name   : {student[1]}")
            print(f"Branch : {student[2]}")
            print(f"CGPA   : {student[3]}")
            print("-" * 35)

    cursor.close()
    connection.close()


def search_student():
    usn = input("Enter USN to search: ")

    connection = get_connection()
    cursor = connection.cursor()

    query = "SELECT * FROM students WHERE usn = %s"
    cursor.execute(query, (usn,))

    student = cursor.fetchone()

    if student:
        print("\nStudent Found")
        print("-" * 30)
        print(f"USN    : {student[0]}")
        print(f"Name   : {student[1]}")
        print(f"Branch : {student[2]}")
        print(f"CGPA   : {student[3]}")
    else:
        print("Student not found.")

    cursor.close()
    connection.close()
def update_student():
    usn = input("Enter USN to update: ")

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM students WHERE usn = %s", (usn,))
    student = cursor.fetchone()

    if not student:
        print("Student not found.")
        cursor.close()
        connection.close()
        return

    name = input("Enter new name: ")
    branch = input("Enter new branch: ")

    try:
        cgpa = float(input("Enter new CGPA: "))

        if not validate_cgpa(cgpa):
            print("CGPA must be between 0 and 10.")
            cursor.close()
            connection.close()
            return

    except ValueError:
        print("Invalid CGPA")
        cursor.close()
        connection.close()
        return

    query = """
    UPDATE students
    SET name=%s, branch=%s, cgpa=%s
    WHERE usn=%s
    """

    cursor.execute(query, (name, branch, cgpa, usn))
    connection.commit()

    print("Student updated successfully!")

    cursor.close()
    connection.close()


def delete_student():
    usn = input("Enter USN to delete: ")

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM students WHERE usn=%s", (usn,))
    student = cursor.fetchone()

    if not student:
        print("Student not found.")
        cursor.close()
        connection.close()
        return

    cursor.execute("DELETE FROM students WHERE usn=%s", (usn,))
    connection.commit()

    print("Student deleted successfully!")

    cursor.close()
    connection.close()

def student_count():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT COUNT(*) FROM students")
    count = cursor.fetchone()[0]

    print(f"\nTotal Students: {count}")

    cursor.close()
    connection.close()