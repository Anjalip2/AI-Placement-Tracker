import streamlit as st
import pandas as pd
from modules.database import get_connection

st.set_page_config(
    page_title="AI Placement Tracker",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 AI-Powered Student Placement Tracker")

st.sidebar.title("Navigation")

option = st.sidebar.radio(
    "Choose an option",
    (
        "🏠 Home",
        "➕ Add Student",
        "📋 View Students",
        "🔍 Search Student",
        "✏️ Update Student",
        "🗑 Delete Student"
    )
)

if option == "🏠 Home":
    st.header("Dashboard")
    st.success("Welcome to AI Placement Tracker!")

elif option == "➕ Add Student":
    st.header("➕ Add Student")

    name = st.text_input("Student Name")
    usn = st.text_input("USN")
    branch = st.text_input("Branch")
    cgpa = st.number_input(
        "CGPA",
        min_value=0.0,
        max_value=10.0,
        step=0.1
    )

    if st.button("Add Student"):
        connection = get_connection()
        cursor = connection.cursor()

        try:
            query = """
            INSERT INTO students(usn, name, branch, cgpa)
            VALUES(%s,%s,%s,%s)
            """

            cursor.execute(query, (usn, name, branch, cgpa))
            connection.commit()

            st.success("Student Added Successfully!")

        except Exception as e:
            st.error(e)

        finally:
            cursor.close()
            connection.close()

elif option == "📋 View Students":
    st.header("📋 Student Records")

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    cursor.close()
    connection.close()

    if students:
        df = pd.DataFrame(
            students,
            columns=["USN", "Name", "Branch", "CGPA"]
        )

        st.dataframe(df, use_container_width=True)

    else:
        st.warning("No students found.")

elif option == "🔍 Search Student":
    st.header("🔍 Search Student")

    usn = st.text_input("Enter USN")

    if st.button("Search"):

        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            "SELECT * FROM students WHERE usn=%s",
            (usn,)
        )

        student = cursor.fetchone()

        cursor.close()
        connection.close()

        if student:
            st.success("Student Found")

            st.write("USN :", student[0])
            st.write("Name :", student[1])
            st.write("Branch :", student[2])
            st.write("CGPA :", student[3])

        else:
            st.error("Student not found")

elif option == "✏️ Update Student":
    st.header("✏️ Update Student")

    usn = st.text_input("Enter USN")

    name = st.text_input("New Name")
    branch = st.text_input("New Branch")
    cgpa = st.number_input(
        "New CGPA",
        min_value=0.0,
        max_value=10.0,
        step=0.1
    )

    if st.button("Update Student"):

        connection = get_connection()
        cursor = connection.cursor()

        query = """
        UPDATE students
        SET name=%s, branch=%s, cgpa=%s
        WHERE usn=%s
        """

        cursor.execute(query, (name, branch, cgpa, usn))
        connection.commit()

        if cursor.rowcount > 0:
            st.success("Student Updated Successfully!")
        else:
            st.error("Student not found!")

        cursor.close()
        connection.close()

elif option == "🗑 Delete Student":
    st.header("🗑 Delete Student")

    usn = st.text_input("Enter USN to Delete")

    if st.button("Delete Student"):

        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            "DELETE FROM students WHERE usn=%s",
            (usn,)
        )

        connection.commit()

        if cursor.rowcount > 0:
            st.success("Student Deleted Successfully!")
        else:
            st.error("Student not found!")

        cursor.close()
        connection.close()
