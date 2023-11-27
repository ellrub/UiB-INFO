# Temaoppgave 7
# Oppgave 1 og 2

from tkinter import Tk, Frame, Button, Label, IntVar

window = Tk()
frame = Frame(window)
frame.pack()

num = IntVar()
num.set("0")

def increment_num():
    current_num = int(num.get())
    num.set(str(current_num + 1))

# text = Label(window, textvariable = num)
# text.pack()

i_button = Button(frame, textvariable = num, command = increment_num)
i_button.pack()

close_button = Button(frame, text="Farvel", command = window.destroy)
close_button.pack()

window.mainloop()
