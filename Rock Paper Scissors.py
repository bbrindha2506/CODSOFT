import tkinter as tk
from tkinter import messagebox
import random

def get_computer_choice():
    """Randomly select Rock, Paper, or Scissors for the computer."""
    choices = ["Rock", "Paper", "Scissors"]
    return random.choice(choices)

def determine_winner(player_choice, computer_choice):
    """Determine the winner of the game."""
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Paper" and computer_choice == "Rock") or \
         (player_choice == "Scissors" and computer_choice == "Paper"):
        return "You win!"
    else:
        return "You lose!"

def play_game(choice):
    """Handle a player's choice and determine the outcome."""
    computer_choice = get_computer_choice()
    result = determine_winner(choice, computer_choice)
    messagebox.showinfo("Result", f"Computer chose: {computer_choice}\n{result}")


root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
root.geometry("400x400")  
root.configure(bg="#f0f0f0") 


title_label = tk.Label(root, text="Rock-Paper-Scissors", font=("Arial", 20), bg="#f0f0f0", fg="#333333")
title_label.pack(pady=20)


rock_button = tk.Button(root, text="Rock", width=15, bg="#ff6666", fg="white", font=("Arial", 12),
                        command=lambda: play_game("Rock"))
rock_button.pack(pady=10)

paper_button = tk.Button(root, text="Paper", width=15, bg="#66b3ff", fg="white", font=("Arial", 12),
                         command=lambda: play_game("Paper"))
paper_button.pack(pady=10)

scissors_button = tk.Button(root, text="Scissors", width=15, bg="#66ff66", fg="white", font=("Arial", 12),
                            command=lambda: play_game("Scissors"))
scissors_button.pack(pady=10)


root.mainloop()
