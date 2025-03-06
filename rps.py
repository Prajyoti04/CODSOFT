import random
import customtkinter as ctk

# Initialize main application
app = ctk.CTk()
app.title("Rock Paper Scissors")
app.geometry("400x500")
app.config(bg="#fce4ec")  # Light pink background

# Game logic
def play_game(user_choice):
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])
    result = "It's a tie!" if user_choice == computer_choice else (
        "You win!" if (user_choice == "Rock" and computer_choice == "Scissors") or
                     (user_choice == "Scissors" and computer_choice == "Paper") or
                     (user_choice == "Paper" and computer_choice == "Rock")
        else "Computer wins!"
    )
    result_label.configure(text=f"Computer chose: {computer_choice}\n{result}")

# UI Components
title_label = ctk.CTkLabel(app, text="Rock Paper Scissors", font=("Comic Sans MS", 20, "bold"), text_color="#ff4081", bg_color="#fce4ec")
title_label.pack(pady=10)

buttons = {"🪨 Rock": "Rock", "📜 Paper": "Paper", "✂️ Scissors": "Scissors"}
for text, choice in buttons.items():
    ctk.CTkButton(app, text=text, command=lambda c=choice: play_game(c), width=120, fg_color="#ffccbc", text_color="#5d4037").pack(pady=5)

result_label = ctk.CTkLabel(app, text="", font=("Comic Sans MS", 16), text_color="#ff4081", bg_color="#fce4ec")
result_label.pack(pady=10)

app.mainloop()
