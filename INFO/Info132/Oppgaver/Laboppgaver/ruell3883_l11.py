from tkinter import Tk, Frame, Entry, StringVar, Button, Label, IntVar

rotwindow = Tk()

frame = Frame(rotwindow)
frame.pack()

string = StringVar()

def show_text():
    current_string = entry.get()
    string.set(current_string)

def increment(num):
    num.set(num.get() + 1)
    numbers.set(f"Alternativ nr1: {num1.get()} - nr2: {num2.get()} - nr3: {num3.get()}")

entry = Entry(frame)
entry.pack()

button = Button(frame, text="Vis Tekst", command = show_text)
button.pack()

label = Label(frame, textvariable = string)
label.pack()

num1 = IntVar()
num1.set(0)
num2 = IntVar()
num2.set(0)
num3 = IntVar()
num3.set(0)

alt1_button = Button(frame, text = "Alternativ 1", command = lambda: increment(num1))
alt1_button.pack()
alt2_button = Button(frame, text = "Alternativ 2", command = lambda: increment(num2))
alt2_button.pack()
alt3_button = Button(frame, text = "Alternativ 3", command = lambda: increment(num3))
alt3_button.pack()

numbers = StringVar()
numbers.set(f"Alternativ nr1: {num1.get()} - nr2: {num2.get()} - nr3: {num3.get()}")

numbers_label = Label(frame, textvariable = numbers)
numbers_label.pack()

rotwindow.mainloop()


