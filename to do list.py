import tkinter as tk
from tkinter import messagebox
import json
import os

TASK_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, 'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(TASK_FILE, 'w') as file:
        json.dump(tasks, file)

def add_task():
    task = task_entry.get()
    if task:
        tasks.append({"task": task, "completed": False})
        save_tasks(tasks)
        update_task_list()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task description.")

def update_task_list():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        status = "✔" if task["completed"] else "✖"
        task_listbox.insert(tk.END, f"{task['task']} [{status}]")

def mark_task_completed():
    selected_index = task_listbox.curselection()
    if selected_index:
        task_index = selected_index[0]
        tasks[task_index]["completed"] = True
        save_tasks(tasks)
        update_task_list()
    else:
        messagebox.showwarning("Selection Error", "Please select a task.")

def delete_task():
    selected_index = task_listbox.curselection()
    if selected_index:
        task_index = selected_index[0]
        tasks.pop(task_index)
        save_tasks(tasks)
        update_task_list()
    else:
        messagebox.showwarning("Selection Error", "Please select a task.")

def on_closing():
    save_tasks(tasks)
    root.destroy()

tasks = load_tasks()

root = tk.Tk()
root.title("To-Do List")

frame = tk.Frame(root)
frame.pack(pady=20)

task_entry = tk.Entry(frame, width=30)
task_entry.pack(side=tk.LEFT, padx=(0, 10))

add_button = tk.Button(frame, text="Add Task", command=add_task)
add_button.pack(side=tk.LEFT)

task_listbox = tk.Listbox(root, width=50, height=10)
task_listbox.pack(pady=20)

button_frame = tk.Frame(root)
button_frame.pack()

complete_button = tk.Button(button_frame, text="Mark as Completed", command=mark_task_completed)
complete_button.pack(side=tk.LEFT, padx=10)

delete_button = tk.Button(button_frame, text="Delete Task", command=delete_task)
delete_button.pack(side=tk.LEFT, padx=10)

update_task_list()

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
