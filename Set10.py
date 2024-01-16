import tkinter as tk
from random import randint

def roll_dice():
    result = randint(1, 6)
    label.config(text=f'Result: {result}')

window = tk.Tk()
window.title("Dice Roll Simulator")

button = tk.Button(window, text="Roll the Dice", command=roll_dice)
button.pack(pady=30)

label = tk.Label(window, text="Result: ")
label.pack()

window.mainloop()
