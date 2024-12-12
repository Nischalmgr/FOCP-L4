import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import matplotlib.pyplot as plt
root=tk.Tk()
root.title("Student Marks Display")
root.geometry("700x700")
subjects=["science","social","maths"]
marks={}
input_frame=tk.Frame(root)
input_frame.grid(row=1,column=0)
tk.Label(input_frame,text="Name").grid(row=0,column=0)
name=tk.Entry(input_frame)
name.grid(row=0,column=1)

 
for subject in subjects:
    marks[subject]=tk.IntVar(value=0)

for i, subject in enumerate(subjects):
    tk.Label(input_frame,text=f"mark of {subject}").grid(row=i+1,column=0)
    tk.Entry(input_frame,textvariable=marks[subject]).grid(row=i+1,column=1)
tree=ttk.Treeview(input_frame,columns=("Name", "science", "social","math","total","grade"),show='headings')
tree.heading("Name",text="Name")
tree.column("Name",anchor=tk.CENTER,width=100)
tree.heading("science",text="science")
tree.column("science",anchor=tk.CENTER,width=80)
tree.heading("social",text="social")
tree.column("social",anchor=tk.CENTER,width=80)
tree.heading("math",text="math")
tree.column("math",anchor=tk.CENTER,width=80)
tree.heading("total",text="total")
tree.column("total",anchor=tk.CENTER,width=80)
tree.heading("grade",text="grade")
tree.column("grade",anchor=tk.CENTER,width=80)
tree.grid(row=7,column=0)


def gradeFinding(marks):
    if marks>=360:
        return"A"
    elif marks<360 and marks>=280:
        return"B"
    elif marks <280 and marks>=240:
        return"C"
    else:
        return"D"
def generate_report():
    print(marks['science'].get())
    print(marks['social'].get())
    student=name.get()
    gradeinfo=[]
    print()
    total_marks=0
    result_text=""
    for subject in subjects:
        total_marks+=marks[subject].get()
        mark=marks[subject].get()
        gradeinfo.append(mark)
 
        print(gradeinfo)
    grade=gradeFinding(total_marks)
    gradeinfo.append(total_marks)
    gradeinfo.append(grade)
    tree.insert("","end",values=(student,gradeinfo[0],gradeinfo[1],gradeinfo[2],gradeinfo[3],gradeinfo[4]))

         
    result_label.config(text=result_text)
    print("in here")
def graph():
    subject=subjects
    mark=[marks[subject].get() for subject in subjects]
    plt.bar(subject,mark)
    plt.title("marks bar")
    plt.xlabel("subject")
    plt.ylabel("marks")
    plt.show()
def okk():
    generate_report()
    graph()


    

tk.Button(input_frame,text="ok",command=okk).grid(row=5,column=0)
result_label=tk.Label(input_frame,text="Result")
result_label.grid(row=6,column=0)




root.mainloop()
