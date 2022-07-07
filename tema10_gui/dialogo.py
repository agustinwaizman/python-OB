import tkinter
from tkinter import colorchooser

window = tkinter.Tk()
filename = colorchooser.askcolor(initialcolor="#fff")
window.mainloop()