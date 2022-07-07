from tkinter import *

def seleccionar():
    monitor.config(text="{}".format(opcion.get()))
def reset():
    opcion.set(None)
    monitor.config(text="")

window = Tk()
opcion = StringVar()
opcion.set(None)

Radiobutton(window, text="OPCION 1", variable = opcion, value = 1, command=seleccionar).pack(anchor=W)
Radiobutton(window, text="OPCION 2", variable = opcion, value = 2, command=seleccionar).pack(anchor=W)
Radiobutton(window, text="OPCION 3", variable = opcion, value = 3, command=seleccionar).pack(anchor=W)
Radiobutton(window, text="OPCION 4", variable = opcion, value = 4, command=seleccionar).pack(anchor=W)
monitor = Label(window)
monitor.pack()
Button(window, text="Reiniciar", command=reset).pack()

window.mainloop()