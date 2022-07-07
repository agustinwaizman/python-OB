import tkinter
from tkinter import ttk

window = tkinter.Tk()
# (0, 0) (1, 0) (2, 0)
# (0, 1) (1, 1) (2, 1)
# (0, 2) (1, 2) (2, 2)
# (0, 3) (1, 3) (2, 3)

window.columnconfigure(0, weight=1)
window.columnconfigure(0, weight=3)

selected = tkinter.StringVar()
r1 = ttk.Radiobutton(window, text="Si", value="1", variable=selected)
r2 = ttk.Radiobutton(window, text="No", value="2", variable=selected)
r3 = ttk.Radiobutton(window, text="Tal Véz", value="3", variable=selected)
r1.grid(column=0, row=1, pady=5, padx=5)
r2.grid(column=0, row=2, pady=5, padx=5)
r3.grid(column=0, row=3, pady=5, padx=5)

selected2 = tkinter.StringVar()
rs1 = ttk.Radiobutton(window, text="Si", value="1", variable=selected2)
rs2 = ttk.Radiobutton(window, text="No", value="2", variable=selected2)
rs3 = ttk.Radiobutton(window, text="Tal Véz", value="3", variable=selected2)
rs1.grid(column=1, row=1, pady=5, padx=5)
rs2.grid(column=1, row=2, pady=5, padx=5)
rs3.grid(column=1, row=3, pady=5, padx=5)
window.mainloop()