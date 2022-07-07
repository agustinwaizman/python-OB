import tkinter
from tkinter import ttk

window = tkinter.Tk()
def salir(event):
    print("adios")
    window.quit()

def saludar(event):
    print("Han hecho click en saludar")

def saludarDobleClick(event):
    print("Han hecho doble click en saludar")

boton = tkinter.Button(window, text="Haz click")
boton.pack()
boton.bind("<Button-1>", saludar)
boton.bind("<Double-1>", saludarDobleClick)

botonSalir = tkinter.Button(window, text="Salir")
botonSalir.pack()
botonSalir.bind("<Button-1>", salir)
window.mainloop()