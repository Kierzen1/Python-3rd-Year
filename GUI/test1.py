import tkinter as tk
from tkinter import ttk
import mysql.connector

# Create a tkinter application window
root = tk.Tk()
root.title("Database Table Viewer")

# Connect to your MariaDB database
try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="python_booc"
    )
except mysql.connector.Error as err:
    print("Error connecting to the database:", err)
    exit(1)

cursor = conn.cursor()

# Execute a SQL query to fetch data from your database table
try:
    cursor.execute("SELECT * FROM student")
    data = cursor.fetchall()
except mysql.connector.Error as err:
    print("Error executing the query:", err)
    conn.close()
    exit(1)

# Check if data is empty
if not data:
    print("No data found in the 'student' table.")
    conn.close()
    exit(1)

# Create a Treeview widget to display the table data
tree = ttk.Treeview(root, columns=range(len(data[0])), show="headings")

# Add column headers
for i, column in enumerate(data[0]):
    tree.heading(i, text=column)
    tree.column(i, width=100)  # Adjust width as needed

# Insert data into the Treeview
for row in data[1:]:
    tree.insert("", "end", values=row)

tree.pack()

# Start the tkinter main loop
root.mainloop()

# Close the database connection when done
conn.close()
