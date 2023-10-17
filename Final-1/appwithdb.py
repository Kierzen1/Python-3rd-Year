from tkinter import *
from tkinter import messagebox
from dbhelperwithdatabaselogin import *
import tkinter as tk
from tkinter import ttk

class UserLogin():
    def __init__(self):
        self.root = Tk()
        self.root.title("User Log-in")
        self.root.geometry("450x250")
        self.root.resizable(False, False)
        self.root.eval("tk::PlaceWindow . center")
        self.frame = Frame(self.root, bd=20)
        self.frame.grid()

        self.lbl_username = Label(self.frame, text="USERNAME", font="Verdana,20", bd=20)
        self.lbl_username.grid(row=0, column=0)
        self.lbl_password = Label(self.frame, text="PASSWORD", font="Verdana,20", bd=20)
        self.lbl_password.grid(row=1, column=0)

        self.txt_username = Entry(self.frame, font="Verdana,20")
        self.txt_username.grid(row=0, column=1)
        self.txt_password = Entry(self.frame, font="Verdana,20", show="*")
        self.txt_password.grid(row=1, column=1)

        self.btn_login = Button(self.frame, text="LOGIN", font="Verdana,20", command=self.login)
        self.btn_login.grid(row=3, column=1, sticky="nsew", pady=10) 

        self.btn_records = Button(self.frame, text="Get All Records", font="Verdana,20", command=self.get_all_records)
        self.btn_records.grid(row=4, column=1, sticky="nsew", pady=10)

        self.records_frame = Frame(self.root, bd=20) 
        self.records_title = Label(self.records_frame, text="Records", font="Verdana,20", bd=20)
        self.records_title.pack()
        self.records_frame.grid()


        self.root.mainloop()  # Run the GUI program

    def login(self):
        usern = self.txt_username.get()
        passw = self.txt_password.get()

        user = userLogin('user', username=usern, password=passw)
        if len(user) > 0:
            messagebox.showinfo("Login Status", "LOGIN ACCEPTED")
        else:
            messagebox.showerror("Login Status", "LOGIN FAILED!")

        self.txt_username.delete(0, END)
        self.txt_password.delete(0, END)

    def get_all_records(self):
        table_name = "student" 
        records = fetch_records(table_name) 
        self.display_records(records)

    def display_records(self, records):
        records_window = tk.Toplevel(self.root)
        records_window.title("Records")

        tree = ttk.Treeview(records_window, columns=["ID","IDNO", "Last Name", "First Name", "Course", "Level"], show="headings")
        tree.pack()

        tree.heading("ID", text="ID", anchor="w")
        tree.heading("IDNO", text="IDNO", anchor="w")
        tree.heading("Last Name", text="Last Name", anchor="w")
        tree.heading("First Name", text="First Name", anchor="w")
        tree.heading("Course", text="Course", anchor="w")
        tree.heading("Level", text="Level", anchor="w")

        for row in records:
            tree.insert("", "end", values=(row["id"],row["idno"], row["lastname"], row["firstname"], row["course"], row["level"]))

def main() -> None:
    UserLogin()

if __name__ == "__main__":
    main()
