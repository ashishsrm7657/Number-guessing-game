import tkinter as tk
import random

# Game logic remains the same
secret_number = random.randint(1, 50)
attempts_left = 5

def check_guess():
    global attempts_left
    try:
        guess = int(guess_entry.get())
        attempts_left -= 1
        
        if guess == secret_number:
            feedback_label.config(text=f"🎉 You win! The number was {secret_number}.", fg="green")
            check_button.config(state=tk.DISABLED) # Disable button on win
        elif attempts_left > 0:
            if guess < secret_number:
                feedback_label.config(text=f"📈 Go higher! You have {attempts_left} attempts left.")
            else:
                feedback_label.config(text=f"📉 Go lower! You have {attempts_left} attempts left.")
        else:
            feedback_label.config(text=f"Game over. The secret number was: {secret_number}", fg="red")
            check_button.config(state=tk.DISABLED) # Disable button on game over
            
    except ValueError:
        feedback_label.config(text="⚠️ Please enter a valid number!")

# Create the main window
root = tk.Tk()
root.title("Guess the Number")
root.geometry("300x200")

# Create and place widgets
instructions_label = tk.Label(root, text="Guess the number (1 to 50)!")
instructions_label.pack(pady=10)

guess_entry = tk.Entry(root)
guess_entry.pack(pady=5)

check_button = tk.Button(root, text="Check Guess", command=check_guess)
check_button.pack(pady=5)

feedback_label = tk.Label(root, text="")
feedback_label.pack(pady=10)

# Start the application's main loop
root.mainloop()