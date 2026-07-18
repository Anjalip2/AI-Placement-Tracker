import json

FILE_NAME = "data/students.json"

def load_students():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except:
        return []
def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)