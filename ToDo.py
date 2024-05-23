import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task != "":
        todo_list.append(task)
        update_listbox()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

def remove_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        del todo_list[selected_task_index]
        update_listbox()
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to remove.")

def clear_list():
    global todo_list
    todo_list = []
    update_listbox()

def update_listbox():
    task_listbox.delete(0, tk.END)
    for task in todo_list:
        task_listbox.insert(tk.END, task)

# Initialize main window
root = tk.Tk()
root.title("To-Do List App")

# Initialize to-do list
todo_list = []

# Create and place widgets
frame = tk.Frame(root)
frame.pack(pady=10)

title = tk.Label(frame, text="To-Do List", font=("Helvetica", 16))
title.pack()

task_listbox = tk.Listbox(frame, width=50, height=10)
task_listbox.pack(pady=10)

task_entry = tk.Entry(frame, width=50)
task_entry.pack(pady=5)

add_button = tk.Button(frame, text="Add Task", command=add_task)
add_button.pack(pady=5)

remove_button = tk.Button(frame, text="Remove Task", command=remove_task)
remove_button.pack(pady=5)

clear_button = tk.Button(frame, text="Clear List", command=clear_list)
clear_button.pack(pady=5)

# Run the application
root.mainloop()
