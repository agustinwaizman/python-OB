from tkinter import *
master = Tk()
elemento = StringVar()
listbox = Listbox(master)
for item in ["Python", "Java", "HTML", "CSS", "JavaScript", "SQL", "Django"]:
    listbox.insert(END, item)
listbox.pack()
label = Label(text="Lista de conocimientos")
label.pack()
master.mainloop()