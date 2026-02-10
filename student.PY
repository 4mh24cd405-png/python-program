import mysql.connector

# Database connection
db = mysql.connector.connect( 
    host="localhost",
    user="root",        # change if needed
    password="1234",  # put your MySQL password
    database="yogesh"
)

cursor = db.cursor()

def add_student():
    name = input("Enter student name: ")
    age = int(input("Enter age: "))
    course = input("Enter course: ")

    sql = "INSERT INTO students (name, age, course) VALUES (%s, %s, %s)"
    values = (name, age, course)

    cursor.execute(sql, values)
    db.commit()
    print("Student added successfully")

def delete_student():
    student_id = int(input("Enter student ID to delete: "))

    sql = "DELETE FROM students WHERE id = %s"
    cursor.execute(sql, (student_id,))
    db.commit()

    if cursor.rowcount > 0:
        print("🗑️ Student deleted successfully")
    else:
        print("Student not found")

def view_students():
    cursor.execute("SELECT * FROM students")
    result = cursor.fetchall()

    print("\n--- Student Records ---")
    for row in result:
        print(row)

def menu():
    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. Delete Student")
        print("3. View Students")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            delete_student()
        elif choice == "3":
            view_students()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice")

menu()

