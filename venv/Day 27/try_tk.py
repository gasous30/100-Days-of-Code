from re import T
from tkinter import *

from pyparsing import col

#Window
window = Tk()
window.title("Challenge Tkinter")
window.minsize(width=500, height=500)

#Labels
label = Label(text='This is label')
label.grid(column=1, row=1)

#Button
def action():
    print('button is clicked.')
button = Button(text='button', command=action)
button.grid(column=2, row=2)

#New Button
def action2():
    print('button 2 is clicked.')
button = Button(text='button 2', command=action2)
button.grid(column=3, row=1)

#Entry
entry = Entry(width=30)
entry.grid(column=4, row=4)


window.mainloop()