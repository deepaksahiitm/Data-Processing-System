from tkinter import *
from tkinter import messagebox

def Add():
    Roll = t1.get()
    Roll_no = t2.get()
    Student_Name = t3.get()
    Course = t4.get()
    Course_Instructor = t5.get()
    Phone = t6.get()

    messagebox.showinfo("information", "Record inserted successfully...")
    print(Roll_no,Student_Name,Course,Course_Instructor,Phone )
    file = open("Records.txt", "a")
    file.write(Roll_no)
    file.write(", ")
    file.write(Student_Name)
    file.write(", ")
    file.write(Course)
    file.write(", ")
    file.write(Course_Instructor)
    file.write(", ")
    file.write(Phone)
    file.write("\n") 
        
def clear():
    t1.delete(0,END)
    t2.delete(0, END)
    t3.delete(0, END)
    t4.delete(0, END)
    t5.delete(0, END)
    t6.delete(0, END)
    messagebox.showinfo("information", "Entry cleared...")
            
def search():
    
    try:
        text  = t1.get()
        file_read = open("Records.txt", "r")
        lines = file_read.readlines()
        new_list = []
        c = 0
        for line in lines:
         
            if text in line:
                new_list.insert(c, line)
                c += 1
        file_read.close()
      
        if len(new_list)==0:
            print("\n\"" +text+ "\" Roll no.not found in Records\""+ "\"!")
        else:
           
            lineLen = len(new_list)
            for i in range(lineLen):
                end=new_list[i]

                print(end)

            print()
            messagebox.showinfo("information",end )
    except :
        print("\nThe file doesn't exist!")
  
root = Tk()
root.title("Course Registration IIT Mandi ")
root.geometry("400x500")
root.configure(bg='green')
global t1
global t2
global t3
global t4
global t5
global t6

Label(root, text="Roll_no").place(x=10, y=10)
Label(root, text="Student_Name").place(x=10, y=40)
Label(root, text="Course").place(x=10, y=70)
Label(root, text="Course_Instructor").place(x=10, y=100)
Label(root, text="Phone").place(x=10, y=140)
Label(root, text="Roll").place(x=50, y=170)

t1 = Entry(root)
t1.place(x=10, y=250)

t2 = Entry(root)
t2.place(x=140, y=10)
 
t3 = Entry(root)
t3.place(x=140, y=40)
 
t4 = Entry(root)
t4.place(x=140, y=70)

t5 = Entry(root)
t5.place(x=140, y=100)

t6 = Entry(root)
t6.place(x=140, y=140)
 
Button(root, text="Add", command=Add ,height = 3, width = 13).place(x=10, y=170)
Button(root, text="Clear",command=clear ,height = 3, width = 13).place(x=120, y=170)
Button(root, text="Search",command=search ,height = 3, width = 13).place(x=10, y=280)

root.mainloop()



