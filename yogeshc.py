import mysql.connector
from mysql.connector import Error

class Library:

    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="your_password",   # change this
                database="library_db"
            )
            self.cursor = self.conn.cursor()
            print("Connected to Library Database Successfully!\n")

        except Error as e:
            print("Database Connection Error:", e)

    def add_book(self):
        try:
            title = input("Enter Book Title: ")
            author = input("Enter Author Name: ")
            quantity = int(input("Enter Quantity: "))

            query = "INSERT INTO books (title, author, quantity) VALUES (%s, %s, %s)"
            values = (title, author, quantity)

            self.cursor.execute(query, values)
            self.conn.commit()
            print("Book Added Successfully!\n")

        except ValueError:
            print("Quantity must be a number!\n")

        except Error as e:
            print("Database Error:", e)

    def view_books(self):
        try:
            self.cursor.execute("SELECT * FROM books")
            records = self.cursor.fetchall()

            print("\nBook Records:")
            for row in records:
                print(row)
            print()

        except Error as e:
            print("Error Fetching Data:", e)

    def update_book(self):
        try:
            book_id = int(input("Enter Book ID to Update: "))
            new_quantity = int(input("Enter New Quantity: "))

            query = "UPDATE books SET quantity=%s WHERE id=%s"
            self.cursor.execute(query, (new_quantity, book_id))
            self.conn.commit()

            if self.cursor.rowcount > 0:
                print("Book Updated Successfully!\n")
            else:
                print("Book ID Not Found!\n")

        except ValueError:
            print("Invalid Input! Enter numbers only.\n")

        except Error as e:
            print("Database Error:", e)

    def delete_book(self):
        try:
            book_id = int(input("Enter Book ID to Delete: "))

            query = "DELETE FROM books WHERE id=%s"
            self.cursor.execute(query, (book_id,))
            self.conn.commit()

            if self.cursor.rowcount > 0:
                print("Book Deleted Successfully!\n")
            else:
                print("Book ID Not Found!\n")

        except ValueError:
            print("Invalid Input! Enter numbers only.\n")

        except Error as e:
            print("Database Error:", e)

    def close_connection(self):
        try:
            if self.conn.is_connected():
                self.cursor.close()
                self.conn.close()
                print("Database Connection Closed.")
        except Error as e:
            print("Error Closing Connection:", e)


# -------- Main Menu --------
if __name__ == "__main__":
    library = Library()

    while True:
        print("====== LIBRARY MANAGEMENT SYSTEM ======")
        print("1. Add Book")
        print("2. View Books")
        print("3. Update Book Quantity")
        print("4. Delete Book")
        print("5. Exit")

        choice = input("Enter Your Choice: ")

        try:
            if choice == "1":
                library.add_book()
            elif choice == "2":
                library.view_books()
            elif choice == "3":
                library.update_book()
            elif choice == "4":
                library.delete_book()
            elif choice == "5":
                library.close_connection()
                break
            else:
                print("Invalid Choice!\n")

        except Exception as e:
            print("Unexpected Error:", e)