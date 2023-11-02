from tkinter import Tk, Label, RAISED

window = Tk()

hei = Label(window, text="Hei", width=10, height=5,
            bd=8, relief=RAISED, fg="#112233", bg="yellow" )
hei.grid(row=0, column=0)

hallo = Label(window, text="Hallo")
hallo.grid(row=1, column=1)

hello = Label(window, text="Hello")
hello.grid(row=2, column=2)

hei_hei = Label(window, text="Hei hei")
hei_hei.grid(row=3, column=3)

window.mainloop()