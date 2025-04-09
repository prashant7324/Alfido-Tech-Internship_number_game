import tkinter as tk
from tkinter import messagebox
import random

class NumberGuessingGame:
    def __init__(self, master):
        self.master = master
        master.title("🎯 Number Guessing Game")
        master.geometry("400x300")
        master.configure(bg="#f0f4f8")

        self.secret_number = random.randint(1, 100)
        self.attempts = 0

        self.title_label = tk.Label(master, text="Guess the Number (1–100)", font=("Helvetica", 16, "bold"), bg="#f0f4f8")
        self.title_label.pack(pady=20)

        self.entry = tk.Entry(master, font=("Helvetica", 14), justify="center")
        self.entry.pack(pady=10)

        self.guess_button = tk.Button(master, text="Guess", font=("Helvetica", 12), bg="#4CAF50", fg="white", command=self.check_guess)
        self.guess_button.pack(pady=5)

        self.reset_button = tk.Button(master, text="Reset", font=("Helvetica", 12), bg="#f44336", fg="white", command=self.reset_game)
        self.reset_button.pack(pady=5)

        self.feedback_label = tk.Label(master, text="", font=("Helvetica", 12), bg="#f0f4f8")
        self.feedback_label.pack(pady=10)

        self.attempts_label = tk.Label(master, text="Attempts: 0", font=("Helvetica", 12), bg="#f0f4f8")
        self.attempts_label.pack()

    def check_guess(self):
        guess = self.entry.get()
        if not guess.isdigit():
            self.feedback_label.config(text="Please enter a valid number.", fg="orange")
            return

        guess = int(guess)
        self.attempts += 1
        self.attempts_label.config(text=f"Attempts: {self.attempts}")

        if guess < self.secret_number:
            self.feedback_label.config(text="Too low! Try again.", fg="blue")
        elif guess > self.secret_number:
            self.feedback_label.config(text="Too high! Try again.", fg="blue")
        else:
            self.feedback_label.config(text="🎉 Correct! You guessed it!", fg="green")
            messagebox.showinfo("Congratulations!", f"You guessed the number in {self.attempts} attempts!")
            self.disable_game()

    def disable_game(self):
        self.guess_button.config(state="disabled")
        self.entry.config(state="disabled")

    def reset_game(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.attempts_label.config(text="Attempts: 0")
        self.feedback_label.config(text="")
        self.entry.delete(0, tk.END)
        self.entry.config(state="normal")
        self.guess_button.config(state="normal")

if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()
