from msilib.schema import RadioButton
import random
import tkinter
from tkinter import ttk
import random

window = tkinter.Tk()
colors = ["blue", "red", "yellow", "purple", "green", "black", "salmon", "darkslateblue", "darksalmon", "grey", "pink", "orange", "lightblue", "darkred", "brown"]

for x in range(0, 50):
    color = random.randint(0, len(colors)-1)
    color2 = random.randint(0, len(colors)-1)
    label = tkinter.Label(window, text="etiqueta!", bg=colors[color], fg=colors[color], borderwidth=10)
    label.place(x = random.randint(0, 150), y = random.randint(0, 150))

window.mainloop()