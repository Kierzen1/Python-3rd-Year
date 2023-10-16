from tkinter import *
from tkinter import messagebox
from dbhelperwithdatabaselogin import *
import tkinter as tk
from tkinter import ttk

class UserLogin():
    def __init__(self):
        self.root = Tk()
        self.root.title("Records")
        self.root.geometry("450x250")
        self.root.resizable(False, False)
        self.root.eval("tk::PlaceWindow . center")
        self.frame = Frame(self.root, bd=20)
        self.frame.grid()

        self.lbl_username = Label(self.frame, text="USERNAME", font="Verdana,20", bd=20)
        self.lbl_username.grid(row=0, column=0)
        self.lbl_password = Label(self.frame, text="PASSWORD", font="Verdana,20", bd=20)
        self.lbl_password.grid(row=1, column=0)

        self.txt_username = Entry(self.frame, text="USERNAME", font="Verdana,20")
        self.txt_username.grid(row=0, column=1)
        self.txt_password = Entry(self.frame, text="PASSWORD", font="Verdana,20", show="*")
        self.txt_password.grid(row=1, column=1)

        self.btn_login = Button(self.frame, text="LOGIN", font="Verdana,20", command=self.login)
        self.btn_login.grid(row=3, column=1, columnspan=3)

        self.btn_records = Button(self.frame, text="Get All Records", font="Verdana,20", command=self.get_all_records)
        self.btn_records.grid(row=4, column=1)

        self.root.mainloop()  # Run the GUI program

    def login(self):
        usern = self.txt_username.get()
        passw = self.txt_password.get()

        # Assuming userLogin is a function that returns a list
        user = userLogin('user', username=usern, password=passw)
        if len(user) > 0:
            messagebox.showinfo("Login Status", "LOGIN ACCEPTED")
        else:
            messagebox.showerror("Login Status", "LOGIN FAILED!")

        self.txt_username.delete(0, END)
        self.txt_password.delete(0, END)

    def get_all_records(self):
        table_name = "student"  # Replace with your table name
        records_window = tk.Toplevel(self.root)
        records_window.title("Records")

        # Create a Treeview widget to display the table data
        tree = ttk.Treeview(records_window, columns=["IDNO", "Last Name", "First Name", "Course", "Level"], show="headings")
        tree.pack()

        # Define column headers and alignment
        columns = ["IDNO", "Last Name", "First Name", "Course", "Level"]
        for col in columns:
            tree.heading(col, text=col, anchor="w")
            tree.column(col, anchor="w")

        # Fetch records from the database using the dbhelper function
        records = getall(table_name)  # Use the getall function from your dbhelper module

        for row in records:
            tree.insert("", "end", values=row)

    # Close the database connection (if necessary)


def main() -> None:
    UserLogin()

if __name__ == "__main__":
    main()
