import tkinter as tk
from tkinter import messagebox
import random


class RockPaperScissors(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Rock Paper Scissors")
        self.geometry("400x300")
        self.resizable(0, 0)

        self.user_score = 0
        self.computer_score = 0

        self.choices = ["Rock", "Paper", "Scissors"]
        self.user_choice = tk.StringVar()
        self.result_text = tk.StringVar()

        tk.Label(self, text="Choose Rock, Paper, or Scissors", font=("Arial", 14)).pack(pady=10)

        for choice in self.choices:
            tk.Radiobutton(self, text=choice, variable=self.user_choice, value=choice, font=("Arial", 12)).pack(
                anchor=tk.W)

        tk.Button(self, text="Play", command=self.play_game, font=("Arial", 12)).pack(pady=10)
        tk.Label(self, textvariable=self.result_text, font=("Arial", 12)).pack(pady=10)

        self.score_text = tk.StringVar()
        self.update_score_text()
        tk.Label(self, textvariable=self.score_text, font=("Arial", 12)).pack(pady=10)

        tk.Button(self, text="Play Again", command=self.reset_game, font=("Arial", 12)).pack(pady=10)
        tk.Button(self, text="Quit", command=self.quit_game, font=("Arial", 12)).pack(pady=10)

    def play_game(self):
        user_choice = self.user_choice.get()
        if not user_choice:
            messagebox.showwarning("Input Error", "Please select an option!")
            return

        computer_choice = random.choice(self.choices)
        result = self.determine_winner(user_choice, computer_choice)

        self.result_text.set(f"You chose {user_choice}, computer chose {computer_choice}.\n{result}")
        self.update_score_text()

    def determine_winner(self, user, computer):
        if user == computer:
            return "It's a tie!"

        if (user == "Rock" and computer == "Scissors") or \
                (user == "Scissors" and computer == "Paper") or \
                (user == "Paper" and computer == "Rock"):
            self.user_score += 1
            return "You win!"

        self.computer_score += 1
        return "You lose!"

    def update_score_text(self):
        self.score_text.set(f"User Score: {self.user_score} | Computer Score: {self.computer_score}")

    def reset_game(self):
        self.user_choice.set("")
        self.result_text.set("")

    def quit_game(self):
        self.destroy()


if __name__ == "__main__":
    app = RockPaperScissors()
    app.mainloop()
