from tkinter import *
from tkinter import messagebox
from dbhelper import *
import tkinter as tk
from tkinter import ttk

class UserLogin():
    def __init__(self):
        self.root=Tk()
        self.root.geometry("500x400")
        self.root.eval("tk::PlaceWindow  .  center")
        self.root.resizable(False,False)
        self.frame = Frame(self.root,bd=20)
        self.frame.grid()
        #LABELS
        self.lbl_idno=Label(self.frame,text ="IDNO",font="Verdana",bd = 10)
        self.lbl_idno.grid(row=0,column=0)
        self.lbl_lastname=Label(self.frame,text ="LASTNAME",font="Verdana",bd = 10)
        self.lbl_lastname.grid(row=1,column=0)
        self.lbl_firstname=Label(self.frame,text ="FIRSTNAME",font="Verdana",bd = 10)
        self.lbl_firstname.grid(row=2,column=0)
        self.lbl_course=Label(self.frame,text ="COURSE",font="Verdana",bd = 10)
        self.lbl_course.grid(row=3,column=0)
        self.lbl_level=Label(self.frame,text ="LEVEL",font="Verdana",bd = 10)
        self.lbl_level.grid(row=4,column=0)
        
        #TEXTBOX
        self.txt_idno=Entry(self.frame,text ="IDNO",font="Verdana")
        self.txt_idno.grid(row=0,column=1)
        self.txt_lastname=Entry(self.frame,text ="LASTNAME",font="Verdana")
        self.txt_lastname.grid(row=1,column=1)
        self.txt_firstname=Entry(self.frame,text ="FIRSTNAME",font="Verdana")
        self.txt_firstname.grid(row=2,column=1)
        
        #COMBO BOX
        idnocb = tk.StringVar()
        self.course_cb= ttk.Combobox(self.frame, width =30, textvariable = idnocb)
        self.course_cb['values'] = ('BSIS','BSCPE','BSIT','BSCS')
        self.course_cb.grid(row=3,column=1)
        
        levelcb = tk.StringVar()
        self.level_cb= ttk.Combobox(self.frame, width =30, textvariable = levelcb)
        self.level_cb['values'] = ('1','2','3','4')
        self.level_cb.grid(row=4,column=1)
        
        # NEW BUTTON
        self.btn_new = Button(self.frame, text="NEW", font="Verdana,20", command=self.newstudent)
        self.btn_new.grid(row=5, column=0)
        
        # SAVE BUTTON
        self.btn_save = Button(self.frame, text="SAVE", font="Verdana,20", command=self.savestudent)
        self.btn_save.grid(row=5, column=1)

        # DELETE BUTTON
        self.btn_delete = Button(self.frame, text="DELETE", font="Verdana,20", command=self.deletestudent)
        self.btn_delete.grid(row=5, column=2)

        # FIND BUTTON (in a different row)
        self.btn_find = Button(self.frame, text="FIND", font="Verdana,20", command = self.findstudent)
        self.btn_find.grid(row=0, column=2)

        # SHOW ALL BUTTON
        self.btn_records = Button(self.frame, text="Get All Records", font="Verdana,20", command=self.get_all_records)
        self.btn_records.grid(row=6, column=1 )

        
        
        #RECORDS FRAME
        self.records_frame = Frame(self.root, bd=20) 
        self.records_title = Label(self.records_frame, font="Verdana,20", bd=20)
        self.records_title.pack()
        self.records_frame.grid()
        
        self.root.mainloop()
        
    def savestudent(self):
        idno:str = self.txt_idno.get()
        lastname:str = self.txt_lastname.get()
        firstname:str = self.txt_firstname.get()
        course:str = self.course_cb.get()
        level:str = self.level_cb.get()
        
        okey:bool = addrecord('student', idno=idno,lastname=lastname,firstname=firstname,course=course,level=level)
        
        if okey:
            messagebox.showinfo("","New Student Added")
        else:
            messagebox.showerror("","Error Adding Student")
    def deletestudent(self):
        idno:str = self.txt_idno.get()
        lastname:str = self.txt_lastname.get()
        firstname:str = self.txt_firstname.get()
        course:str = self.course_cb.get()
        level:str = self.level_cb.get()
        
        okey:bool = deleterecord('student', idno=idno,lastname=lastname,firstname=firstname,course=course,level=level)
        
        if okey:
            messagebox.showinfo("","STUDENT DELETED")
        else:
            messagebox.showerror("","Error Deleting Student")
            
    def newstudent(self):
        self.txt_idno.delete(0, END)
        self.txt_lastname.delete(0, END)
        self.txt_firstname.delete(0, END)
        self.course_cb.delete(0, END)
        self.level_cb.delete(0, END)
        
    def findstudent(self):
        idno:str = self.txt_idno.get()
        lastname:str = self.txt_lastname.get()
        firstname:str = self.txt_firstname.get()
        course:str = self.course_cb.get()
        level:str = self.level_cb.get()
        
        okey = getrecord('student', idno=idno,lastname=lastname,firstname=firstname,course=course,level=level)
        
        if okey:
            self.txt_idno.insert(0, okey['idno'])
        else:
            messagebox.showerror("","Error Deleting Student")
    ############################################################
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
            tree.insert("", "end", values=(row["IDNO"], row["lastname"], row["firstname"], row["course"], row["level"]))
def main() -> None:
    UserLogin()

if __name__ == "__main__":
    main()