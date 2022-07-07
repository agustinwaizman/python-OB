import tkinter

window = tkinter.Tk()
label1 = tkinter.Label(window, text="label1", bg="yellow", fg="black")
label1.pack(ipadx=45, ipady=15, fill="x")

label2 = tkinter.Label(window, text="label2", bg="purple", fg="darkslateblue")
label2.pack(ipadx=45, ipady=15, fill="x")

label3 = tkinter.Label(window, text="label3", bg="red", fg="white")
label3.pack(ipadx=45, ipady=15, fill="x")

label4 = tkinter.Label(window, text="label4", bg="salmon", fg="black")
label4.pack(ipadx=15, ipady=15, side="left", fill="x")

label5 = tkinter.Label(window, text="label5", bg="darkslateblue", fg="white")
label5.pack(ipadx=15, ipady=15, side="left", fill="x")

label6 = tkinter.Label(window, text="label6", bg="green", fg="orange")
label6.pack(ipadx=15, ipady=15, side="right")


window.mainloop()