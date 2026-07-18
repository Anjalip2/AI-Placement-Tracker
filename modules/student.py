from modules.database import load_students, save_students

students=load_students()

def add_student():

    name = input("Enter your name: ")
    usn = input("Enter your usn: ")
    branch = input("Enter your branch: ")
    cgpa = float(input("Enter your cgpa: "))

    student = {
        "name" : name,
        "usn" : usn,
        "branch" : branch,
        "cgpa" : cgpa 
    }

    students.append(student)
    save_students(students)

    print("\nStudent added successfully!")

def view_students():

    if len(students)==0:
        print("\nNo Students Found. ")
        return
    
    print("\n-----------------Students list-----------------")
    for student in students:
        print(f"Name     :  {student['name']}")
        print(f"USN      :  {student['usn']}")
        print(f"Branch   :  { student['branch']}")
        print(f"CGPA     :  {student['cgpa']}")

    print("-------------------------------------------------")

def search_student():
    usn = input("Enter USN to search: ")

    for student in students:
        if student["usn"]==usn:
            print("\nStudent found ")
            print("----------------------------")
            print(f"Name      :  {student['name']}")
            print(f"USN       :  {student['usn']}")
            print(f"Branch    :  {student['branch']}")
            print(f"CGPA      :  {student['cgpa']}")
            return
    print("Student not Found.")

def update_student():
    usn=input("Enter the USN to update: ")

    for student in students:
        if student["usn"]==usn:
            print("\nStudent Found")
            student["name"]=input("Enter the new name: ")
            student["branch"]=input("Enter the new branch: ")
            student["cgpa"]=float(input("Enter the new cgpa: "))

            save_students(students)

            print("\nStudent Updated successfully! ")
            return
        
    print("Student not found.")

def delete_student():
    usn = input("Enter USN to delete: ")

    for student in students:
        if student["usn"]==usn:
            students.remove(student)

            save_students(students)
            
            print("\nStudent deleted successfully!")
            return
    print("Student not found.")


