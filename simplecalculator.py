import tkinter as tk
import customtkinter as ctk
import time

# Function for animation
def animate_result(result_text):
    result_label.configure(text="")
    for i in range(len(result_text) + 1):
        result_label.configure(text=result_text[:i])
        app.update()
        time.sleep(0.05)  

# Function to perform calculation
def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()
        
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                animate_result("Error: Division by zero!")
                return
            result = num1 / num2
        elif operation == "%":
            if num2 == 0:
                animate_result("Error: Modulo by zero!")
                return
            result = num1 % num2
        else:
            animate_result("Invalid operation!")
            return
        
        animate_result(f"Result: {result}")
    except ValueError:
        animate_result("Invalid input! Enter numbers.")


app = ctk.CTk()
app.title("Animated Calculator")
app.geometry("350x400")
app.config(bg="#C3E4CD")  # Set pastel green background


ctk.CTkLabel(app, text="Simple Calculator", font=("Arial", 20, "bold"), text_color="#000000", bg_color="#C3E4CD").pack(pady=10)

entry_num1 = ctk.CTkEntry(app, width=200)
entry_num1.pack(pady=5)
entry_num2 = ctk.CTkEntry(app, width=200)
entry_num2.pack(pady=5)

operation_var = tk.StringVar()
operation_var.set("+")
operations = ["+", "-", "*", "/", "%"]
operation_menu = ctk.CTkOptionMenu(app, variable=operation_var, values=operations)
operation_menu.pack(pady=5)

calculate_button = ctk.CTkButton(app, text="Calculate", command=calculate, fg_color="#6B8E23", hover_color="#556B2F", text_color="#FFFFFF")
calculate_button.pack(pady=10)

result_label = ctk.CTkLabel(app, text="", font=("Arial", 16), text_color="#000000", bg_color="#C3E4CD")
result_label.pack(pady=10)

app.mainloop()
