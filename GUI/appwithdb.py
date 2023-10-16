from tkinter import *
from tkinter import messagebox
from dbhelperwithdatabaselogin import *
import tkinter as tk
from tkinter import ttk

class UserLogin():
    def __init__(self):
        self.root = Tk()
        self.root.title("User Login")
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
        self.btn_login.grid(row=3, column=0, columnspan = 3)
        
        self.btn_records = Button(self.frame, text="Show Tables", font="Verdana,20", command=self.showStudent)
        self.btn_records.grid(row=4, column=2)

        self.root.mainloop()  # run the GUI program

    def login(self):
        usern: str = self.txt_username.get()
        passw: str = self.txt_password.get()

        # Assuming userLogin is a function that returns a list
        user: list = userLogin('user', username=usern, password=passw)
        if len(user)>0:
            messagebox.showinfo("login status", "LOGIN ACCEPTED")
        else:
            messagebox.showerror("login status", "LOGIN FAILED !")

        self.txt_username.delete(0, END)
        self.txt_password.delete(0, END)
        
    def showStudent(self):
        root = tk.Tk()

        tree = ttk.Treeview(root, columns=("c1", "c2", "c3", "c4", "c5"), show='headings')
        tree.column("#1", anchor=tk.CENTER)
        tree.heading("#1", text="IDNO")
        tree.column("#2", anchor=tk.CENTER)
        tree.heading("#2", text="Lastname")
        tree.column("#3", anchor=tk.CENTER)
        tree.heading("#3", text="Firstname")
        tree.column("#4", anchor=tk.CENTER)
        tree.heading("#4", text="Course")
        tree.column("#5", anchor=tk.CENTER)
        tree.heading("#5", text="Level")
        tree.pack()

        keys = ['column1', 'column2']  # Replace with your column names
        vals = ['value1', 'value2']  # Replace with the values to search for

        showTableStudent("students", keys, vals, tree)

def main() -> None:
    UserLogin()

if __name__ == "__main__":
    main()
