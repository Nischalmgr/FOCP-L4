import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt

root = tk.Tk()
root.title("Student Marks Display")
root.geometry("600x600")

# Subjects and Marks Initialization
subjects = ["science", "social", "maths"]
marks = {}

# Input Frame
input_frame = tk.Frame(root)
input_frame.grid(row=0, column=0, padx=10, pady=10)

# Name Entry Label and Field
tk.Label(input_frame, text="Name").grid(row=0, column=0)
name = tk.Entry(input_frame)
name.grid(row=0, column=1)

# Subject Marks Labels and Entries
for subject in subjects:
    marks[subject] = tk.IntVar(value=0)

for i, subject in enumerate(subjects):
    tk.Label(input_frame, text=f"Marks of {subject}").grid(row=i + 1, column=0)
    tk.Entry(input_frame, textvariable=marks[subject]).grid(row=i + 1, column=1)

# Treeview for Displaying Records
tree = ttk.Treeview(root, columns=("Name", "science", "social", "math", "action"), show='headings')
tree.heading("Name", text="Name")
tree.column("Name", anchor=tk.CENTER, width=100)
tree.heading("science", text="Science")
tree.column("science", anchor=tk.CENTER, width=80)
tree.heading("social", text="Social")
tree.column("social", anchor=tk.CENTER, width=80)
tree.heading("math", text="Math")
tree.column("math", anchor=tk.CENTER, width=80)
tree.heading("action", text="Grade")
tree.column("action", anchor=tk.CENTER, width=80)
tree.grid(row=1, column=0, padx=10, pady=10)

# Grade Calculation Function
def gradeFinding(mark):
    if mark >= 80:
        return "A"
    elif mark >= 70:
        return "B"
    elif mark >= 50:
        return "C"
    else:
        return "D"

# Generate Report Function and Add Row to Treeview
def generate_report():
    student_name = name.get()
    total_marks = 0
    grade_info = []

    for subject in subjects:
        subject_mark = marks[subject].get()
        grade = gradeFinding(subject_mark)
        grade_info.append((subject_mark, grade))

    # Add data to the Treeview
    tree.insert("", "end", values=(student_name, grade_info[0][0], grade_info[1][0], grade_info[2][0], f"{grade_info[0][1]}, {grade_info[1][1]}, {grade_info[2][1]}"))

# Graph Generation Function
def graph():
    subject_names = subjects
    subject_marks = [marks[subject].get() for subject in subjects]

    plt.bar(subject_names, subject_marks, color='skyblue')
    plt.title("Marks Distribution")
    plt.xlabel("Subjects")
    plt.ylabel("Marks")
    plt.show()

# Function to Call Both Report Generation and Graph
def okk():
    generate_report()
    graph()

# Button to Generate Report and Display Graph
tk.Button(input_frame, text="OK", command=okk).grid(row=5, column=0)

root.mainloop()
