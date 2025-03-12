import random
import string
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import time

def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation
    
    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special
        
    pwd = ""
    has_number = has_special = False
    
    while len(pwd) < min_length or (numbers and not has_number) or (special_characters and not has_special):
        new_char = random.choice(characters)
        pwd += new_char
        
        if new_char in digits:
            has_number = True
        if new_char in special:
            has_special = True
    
    return pwd

def animate_text(label, text):
    label.config(text="")
    for i in range(len(text) + 1):
        label.after(i * 100, lambda t=text[:i]: label.config(text=t))

def on_generate():
    try:
        min_length = int(length_var.get())
        numbers = num_var.get()
        special = special_var.get()
        
        if not numbers and not special:
            messagebox.showwarning("Warning", "It's recommended to include at least numbers or special characters for security.")
        
        password = generate_password(min_length, numbers, special)
        animate_text(result_label, password)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number for length.")

# GUI Setup
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")
root.configure(bg="#2C3E50")

frame = tk.Frame(root, bg="#34495E", padx=20, pady=20)
frame.pack(pady=20, padx=20, fill="both", expand=True)

tk.Label(frame, text="Minimum Length:", fg="white", bg="#34495E", font=("Arial", 12)).grid(row=0, column=0, sticky="w")
length_var = tk.StringVar()
tk.Entry(frame, textvariable=length_var, font=("Arial", 12)).grid(row=0, column=1)

num_var = tk.BooleanVar()
tk.Checkbutton(frame, text="Include Numbers", variable=num_var, fg="white", bg="#34495E", font=("Arial", 12)).grid(row=1, column=0, columnspan=2, sticky="w")

special_var = tk.BooleanVar()
tk.Checkbutton(frame, text="Include Special Characters", variable=special_var, fg="white", bg="#34495E", font=("Arial", 12)).grid(row=2, column=0, columnspan=2, sticky="w")

generate_btn = tk.Button(frame, text="Generate Password", command=on_generate, font=("Arial", 12, "bold"), bg="#E74C3C", fg="white")
generate_btn.grid(row=3, column=0, columnspan=2, pady=10)

result_label = tk.Label(frame, text="", fg="#1ABC9C", bg="#34495E", font=("Arial", 14, "bold"))
result_label.grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()