import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get().strip()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        task_listbox.delete(selected_task)
    else:
        messagebox.showwarning("Warning", "Select a task to delete.")

def delete_all_tasks():
    if messagebox.askyesno("Confirm", "Delete all tasks?"):
        task_listbox.delete(0, tk.END)

def remove_task(event):
    selected_task = task_listbox.curselection()
    if selected_task:
        task_listbox.delete(selected_task)


root = tk.Tk()
root.title("Minimalist To-Do List")
root.geometry("300x350")
root.configure(bg="#f0f0f0")


task_entry = tk.Entry(root, width=30, font=("Arial", 12))
task_entry.pack(pady=10)


button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=5)

add_button = tk.Button(button_frame, text="Add Task", command=add_task, bg="#4caf50", fg="white", padx=10)
add_button.grid(row=0, column=0, padx=5)

delete_button = tk.Button(button_frame, text="Delete Task", command=delete_task, bg="#f44336", fg="white", padx=10)
delete_button.grid(row=0, column=1, padx=5)

delete_all_button = tk.Button(button_frame, text="Delete All", command=delete_all_tasks, bg="#ff9800", fg="white", padx=10)
delete_all_button.grid(row=0, column=2, padx=5)


task_listbox = tk.Listbox(root, width=40, height=15, font=("Arial", 12))
task_listbox.pack(pady=10)


task_listbox.bind("<Double-Button-1>", remove_task)


root.mainloop()
