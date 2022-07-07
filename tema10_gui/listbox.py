import tkinter

window = tkinter.Tk()
# (0, 0) (1, 0) (2, 0)
# (0, 1) (1, 1) (2, 1)
# (0, 2) (1, 2) (2, 2)
# (0, 3) (1, 3) (2, 3)

window.columnconfigure(0, weight=1)
window.columnconfigure(0, weight=3)

lista = ["Python", "Java", "Go", "JavaScript", "C++", "C#", "Ruby"]
lista_items = tkinter.StringVar(value=lista)
listbox = tkinter.Listbox(window, height=50, listvariable=lista_items)
listbox.grid(column=0, row=0, sticky=tkinter.W)

window.mainloop()