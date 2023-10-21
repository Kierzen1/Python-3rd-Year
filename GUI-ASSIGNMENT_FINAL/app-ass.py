from tkinter import *
from tkinter import messagebox
from dbhelper import *
import tkinter as tk
from tkinter import ttk

class UserLogin():
    def __init__(self):
        
        self.root = Tk()
        self.root.geometry("500x345")
        self.root.title("BOOC, Kierzen Ivan Jay")
        self.root.eval("tk::PlaceWindow . center")
        self.root.resizable(False, False)
        self.frame = Frame(self.root, bd=20, bg = "#E2DADB")
        self.frame.grid()

        # LABELS
        self.lbl_idno = Label(self.frame, text="IDNO", font="Verdana", bd=10, bg = "#E2DADB")
        self.lbl_idno.grid(row=0, column=0)
        self.lbl_lastname = Label(self.frame, text="LASTNAME", font="Verdana", bd=10, bg = "#E2DADB")
        self.lbl_lastname.grid(row=1, column=0)
        self.lbl_firstname = Label(self.frame, text="FIRSTNAME", font="Verdana", bd=10, bg = "#E2DADB")
        self.lbl_firstname.grid(row=2, column=0)
        self.lbl_course = Label(self.frame, text="COURSE", font="Verdana", bd=10, bg = "#E2DADB")
        self.lbl_course.grid(row=3, column=0)
        self.lbl_level = Label(self.frame, text="LEVEL", font="Verdana", bd=10, bg = "#E2DADB")
        self.lbl_level.grid(row=4, column=0)

        # TEXTBOX
        self.txt_idno = Entry(self.frame, text="IDNO", font="Verdana")
        self.txt_idno.grid(row=0, column=1)
        self.txt_lastname = Entry(self.frame, text="LASTNAME", font="Verdana")
        self.txt_lastname.grid(row=1, column=1)
        self.txt_firstname = Entry(self.frame, text="FIRSTNAME", font="Verdana")
        self.txt_firstname.grid(row=2, column=1)

        # COMBO BOX
        idnocb = tk.StringVar()
        self.course_cb = ttk.Combobox(self.frame, width=18, textvariable=idnocb, font = "Verdana")
        self.course_cb['values'] = ('BSIS', 'BSCPE', 'BSIT', 'BSCS')
        self.course_cb.grid(row=3, column=1)

        levelcb = tk.StringVar()
        self.level_cb = ttk.Combobox(self.frame, width=18, textvariable=levelcb, font = "Verdana")
        self.level_cb['values'] = ('1', '2', '3', '4')
        self.level_cb.grid(row=4, column=1)

        #BUTTON FRAME
        button_frame = Frame(self.frame)
        button_frame.grid(row=6, column=0, columnspan=8, pady = 15, padx = 15)  

        # NEW BUTTON
        self.btn_new = Button(button_frame, text="NEW", font="Verdana,20", command=self.newstudent)
        self.btn_new.grid(row=0, column=0, padx = 22,  sticky="ew")

        # SAVE BUTTON
        self.btn_save = Button(button_frame, text="SAVE", font="Verdana,20", command=self.savestudent)
        self.btn_save.grid(row=0, column=1, padx = 22,  sticky="ew")

        # DELETE BUTTON
        self.btn_delete = Button(button_frame, text="DELETE", font="Verdana,20", command=self.deletestudent)
        self.btn_delete.grid(row=0, column=2, padx = 22,pady = 10,  sticky="ew")

        # UPDATE BUTTON
        self.btn_update = Button(button_frame, text="UPDATE", font="Verdana,20", command=self.updatestudent)
        self.btn_update.grid(row=0, column=3, padx = 22,  sticky="ew")

        #SHOW RECRODS FRAME
        showAll_frame = Frame(self.frame, bg="#E2DADB")
        showAll_frame.grid(row=8, column=0, columnspan=4)
        
        # SHOW ALL BUTTON
        self.btn_records = Button(showAll_frame, text="Get All Records", font="Verdana,20", command=self.get_all_records)
        self.btn_records.grid(row=0, column=6, padx = 20)
       
        # FIND BUTTON
        self.btn_find = Button(self.frame, text="FIND", font="Verdana,20", command = self.findstudent)
        self.btn_find.grid(row=0, column=2, padx = 10)

        self.root.mainloop()
        
    def savestudent(self):
        idno = self.txt_idno.get()
        lastname = self.txt_lastname.get()
        firstname = self.txt_firstname.get()
        course = self.course_cb.get()
        level = self.level_cb.get()

        if idno_already_exists(idno):
            self.newstudent()
            messagebox.showerror("Duplicate Entry", "IDNO already exists.")
        else:
            okey = addrecord('student', idno=idno, lastname=lastname, firstname=firstname, course=course, level=level)

            if okey:
                messagebox.showinfo("SUCCESS", "New Student Added")
                self.newstudent()
            else:
                messagebox.showerror("ERROR", "Error Adding Student")
                
    def deletestudent(self):
        idno:str = self.txt_idno.get()
        lastname:str = self.txt_lastname.get()
        firstname:str = self.txt_firstname.get()
        course:str = self.course_cb.get()
        level:str = self.level_cb.get()
        
        okey:bool = deleterecord('student', idno=idno,lastname=lastname,firstname=firstname,course=course,level=level)
        
        if okey:
            messagebox.showinfo("SUCCESS","STUDENT DELETED")
            self.newstudent()
        else:
            messagebox.showerror("ERROR","Error Deleting Student")
            
    def newstudent(self):
        self.txt_idno.delete(0, END)
        self.txt_lastname.delete(0, END)
        self.txt_firstname.delete(0, END)
        self.course_cb.delete(0, END)
        self.level_cb.delete(0, END)
        
    def findstudent(self):
        idno = self.txt_idno.get()
        lastname = self.txt_lastname.get()
        firstname = self.txt_firstname.get()
        course = self.course_cb.get()
        level = self.level_cb.get()

        students = getrecord('student', idno=idno, lastname=lastname, firstname=firstname, course=course, level=level)

        if students:
            student = students[0]

            self.txt_idno.delete(0, END)
            self.txt_lastname.delete(0, END)
            self.txt_firstname.delete(0, END)
            self.course_cb.set('')
            self.level_cb.set('')

            self.txt_idno.insert(0, student['idno'])
            self.txt_lastname.insert(0, student['lastname'])
            self.txt_firstname.insert(0, student['firstname'])
            self.course_cb.set(student['course'])
            self.level_cb.set(student['level'])
        else:
            messagebox.showerror("ERROR", "Student Not Found")
            
    def updatestudent(self):
        idno = self.txt_idno.get()
        lastname = self.txt_lastname.get()
        firstname = self.txt_firstname.get()
        course = self.course_cb.get()
        level = self.level_cb.get()

        if idno_already_exists(idno):
            okey = updaterecord('student', idno=idno, lastname=lastname, firstname=firstname, course=course, level=level)

            if okey:
                messagebox.showinfo("SUCCESS", "Student Updated")
            else:
                messagebox.showerror("", "Error Updating Student")
        else:
            messagebox.showerror("ERROR", "Student Not Found")

#############-----SHOW RECORDS--------##############
    def get_all_records(self):
        table_name = "student" 
        records = fetch_records(table_name) 
        self.display_records(records)

    def display_records(self, records):
        records_window = tk.Toplevel(self.root)
        records_window.title("Records")

        tree = ttk.Treeview(records_window, columns=["IDNO", "Last Name", "First Name", "Course", "Level"], show="headings")
        tree.pack()


        tree.heading("IDNO", text="IDNO", anchor="w")
        tree.heading("Last Name", text="Last Name", anchor="w")
        tree.heading("First Name", text="First Name", anchor="w")
        tree.heading("Course", text="Course", anchor="w")
        tree.heading("Level", text="Level", anchor="w")

        for row in records:
            tree.insert("", "end", values=(row["idno"], row["lastname"], row["firstname"], row["course"], row["level"]))
def main() -> None:
    UserLogin()

if __name__ == "__main__":
    main()