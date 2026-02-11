import mysql.connector

class StudentDatabase:
    
    def __init__(self):
        # Connect to MySQL
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",   # change this
            database="yogi3"           # create this database first
        )
        self.cursor = self.conn.cursor()
        print("Connected to Database Successfully!")

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS students (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            age INT,
            course VARCHAR(100)
        )
        """
        self.cursor.execute(query)
        print("Table created successfully!")

    def insert_student(self, name, age, course):
        query = "INSERT INTO students (name, age, course) VALUES (%s, %s, %s)"
        values = (name, age, course)
        self.cursor.execute(query, values)
        self.conn.commit()
        print("Student inserted successfully!")

    def display_students(self):
        self.cursor.execute("SELECT * FROM students")
        result = self.cursor.fetchall()
        print("\nStudent Records:")
        for row in result:
            print(row)

    def update_student(self, student_id, new_course):
        query = "UPDATE students SET course = %s WHERE id = %s"
        values = (new_course, student_id)
        self.cursor.execute(query, values)
        self.conn.commit()
        print("Student updated successfully!")

    def delete_student(self, student_id):
        query = "DELETE FROM students WHERE id = %s"
        self.cursor.execute(query, (student_id,))
        self.conn.commit()
        print("Student deleted successfully!")

    def close_connection(self):
        self.conn.close()
        print("Database connection closed.")


# -------- Main Program --------
if __name__ == "__main__":
    db = StudentDatabase()

    db.create_table()

    db.insert_student("Yogi", 21, "Python")
    db.insert_student("Rahul", 22, "Data Science")

    db.display_students()

    db.update_student(1, "Machine Learning")

    db.display_students()

    db.delete_student(2)

    db.display_students()

    db.close_connection()