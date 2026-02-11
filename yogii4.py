import mysql.connector
from datetime import date

class JackoProject:

    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",  # change this
            database="yogii4"
        )
        self.cursor = self.conn.cursor()
        print("Connected to JACKO Database Successfully!\n")

    def add_application(self):
        company = input("Enter Company Name: ")
        position = input("Enter Position: ")
        status = input("Enter Status (Applied/Interview/Selected/Rejected): ")
        applied_date = date.today()

        query = "INSERT INTO applications (company, position, status, applied_date) VALUES (%s, %s, %s, %s)"
        values = (company, position, status, applied_date)

        self.cursor.execute(query, values)
        self.conn.commit()
        print("Application Added Successfully!\n")

    def view_applications(self):
        self.cursor.execute("SELECT * FROM applications")
        records = self.cursor.fetchall()

        print("\n--- All Job Applications ---")
        for row in records:
            print(row)
        print()

    def update_status(self):
        app_id = int(input("Enter Application ID to Update: "))
        new_status = input("Enter New Status: ")

        query = "UPDATE applications SET status=%s WHERE id=%s"
        self.cursor.execute(query, (new_status, app_id))
        self.conn.commit()
        print("Status Updated Successfully!\n")

    def delete_application(self):
        app_id = int(input("Enter Application ID to Delete: "))

        query = "DELETE FROM applications WHERE id=%s"
        self.cursor.execute(query, (app_id,))
        self.conn.commit()
        print("Application Deleted Successfully!\n")

    def close_connection(self):
        self.conn.close()
        print("Connection Closed.")

# -------- Menu Driven Program --------
if __name__ == "__main__":
    jacko = JackoProject()

    while True:
        print("====== JACKO PROJECT ======")
        print("1. Add Application")
        print("2. View Applications")
        print("3. Update Status")
        print("4. Delete Application")
        print("5. Exit")

        choice = input("Enter Your Choice: ")

        if choice == "1":
            jacko.add_application()
        elif choice == "2":
            jacko.view_applications()
        elif choice == "3":
            jacko.update_status()
        elif choice == "4":
            jacko.delete_application()
        elif choice == "5":
            jacko.close_connection()
            break
        else:
            print("Invalid Choice!\n")