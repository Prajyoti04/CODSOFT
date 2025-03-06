import customtkinter
from tkinter import *
from tkinter import messagebox
import json  # For saving tasks

# Initialize the main application
app = customtkinter.CTk()
app.title('To-Do List')
app.geometry('350x500')
app.config(bg='#000080')  # Navy Blue Background


font1 = ('Arial', 25, 'bold')
font2 = ('Arial', 16, 'bold')
font3 = ('Arial', 12)


def add_task():
    task = task_entry.get().strip()
    if task:
        tasks_list.insert(END, task)
        task_entry.delete(0, END)
        save_tasks()
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def remove_task():
    try:
        selected_task = tasks_list.curselection()[0]
        tasks_list.delete(selected_task)
        save_tasks()
    except IndexError:
        messagebox.showwarning("Warning", "No task selected!")

def mark_completed():
    try:
        selected_task_index = tasks_list.curselection()[0]
        task_text = tasks_list.get(selected_task_index)

        
        if task_text.startswith("[✓] "):
            messagebox.showinfo("Info", "Task is already completed!")
            return
        
        tasks_list.delete(selected_task_index)
        tasks_list.insert(selected_task_index, f"[✓] {task_text}")
        save_tasks()
    except IndexError:
        messagebox.showwarning("Warning", "No task selected!")

def save_tasks():
    """ Save tasks to a file """
    with open("tasks.json", "w") as file:
        tasks = tasks_list.get(0, END)
        json.dump(tasks, file)

def load_tasks():
    """ Load tasks from a file """
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
            tasks_list.delete(0, END)
            for task in tasks:
                tasks_list.insert(END, task)
    except FileNotFoundError:
        pass  


title_label = customtkinter.CTkLabel(app, font=font1, text='To-Do List', text_color='#fff', bg_color='#000080')
title_label.pack(pady=10)

task_entry = customtkinter.CTkEntry(app, font=font2, text_color='#000', fg_color='#fff', border_color='#fff', width=260)
task_entry.pack(pady=10)

button_frame = Frame(app, bg='#000080')
button_frame.pack(pady=5)

add_button = customtkinter.CTkButton(button_frame, font=font2, text_color='#fff', text='Add Task',
                                     fg_color='#1E90FF', hover_color='#1C86EE', bg_color='#000080',
                                     cursor='hand2', corner_radius=5, width=120, command=add_task)  
add_button.grid(row=0, column=0, padx=5, pady=5)

remove_button = customtkinter.CTkButton(button_frame, font=font2, text_color='#fff', text='Remove Task',
                                        fg_color='#FF4500', hover_color='#E63900', bg_color='#000080',
                                        cursor='hand2', corner_radius=5, width=120, command=remove_task)  
remove_button.grid(row=0, column=1, padx=5, pady=5)

complete_button = customtkinter.CTkButton(app, font=font2, text_color='#fff', text='Mark Completed',
                                          fg_color='#32CD32', hover_color='#2E8B57', bg_color='#000080',
                                          cursor='hand2', corner_radius=5, width=260, command=mark_completed) 
complete_button.pack(pady=5)


task_frame = Frame(app, bg='#000080')
task_frame.pack(pady=10)

scrollbar = Scrollbar(task_frame)
tasks_list = Listbox(task_frame, width=40, height=12, font=font3, yscrollcommand=scrollbar.set, bg='#fff')

scrollbar.pack(side=RIGHT, fill=Y)
tasks_list.pack(side=LEFT)

scrollbar.config(command=tasks_list.yview)

load_tasks()

app.mainloop()
