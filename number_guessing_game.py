import tkinter as tk
import random

app = tk.Tk()
app.title("Number Guessing Game")
app.geometry("400x300")

random_number = random.randint(1, 100)
attempts = 0 

def check_guess():
    global attempts
    try:
        guess = int(entry_guess.get()) 
        attempts += 1
        if guess < random_number:
            label_result.config(text="Too Low! Try again.")
        elif guess > random_number:
            label_result.config(text="Too High! Try again.")
        else:
            label_result.config(text=f"Correct! You guessed it in {attempts} attempts.")
            button_submit.config(state=tk.DISABLED)  
    except ValueError:
        label_result.config(text="Invalid input! Please enter a number.")

def restart_game():
    global random_number, attempts
    random_number = random.randint(1, 100)
    attempts = 0
    entry_guess.delete(0, tk.END) 
    label_result.config(text="New game started! Guess the number.")
    button_submit.config(state=tk.NORMAL)  


label_welcome = tk.Label(app, text="Welcome to the Number Guessing Game!", font=("Arial", 14))
label_welcome.pack(pady=10)

entry_guess = tk.Entry(app, font=("Arial", 12))
entry_guess.pack(pady=10)

button_submit = tk.Button(app, text="Submit Guess", font=("Arial", 12), command=check_guess)
button_submit.pack(pady=5)

label_result = tk.Label(app, text="Guess a number between 1 and 100", font=("Arial", 12))
label_result.pack(pady=10)

button_restart = tk.Button(app, text="Restart Game", font=("Arial", 12), command=restart_game)
button_restart.pack(pady=5)

app.mainloop()
