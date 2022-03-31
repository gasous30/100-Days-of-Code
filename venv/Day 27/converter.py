from ctypes import alignment
from tkinter import *

#convert function
def miles_to_km():
    miles = miles_input.get()
    km_output.config(text=f"{float(miles)*1.609}")

#Window
window = Tk()
window.title('Mile to Km Converter')
window.config(padx=30, pady=30)

#entry
miles_input = Entry(width=10)
miles_input.insert(END, '0')
miles_input.grid(column=2, row=1)

#label miles
miles = Label(text='miles')
miles.grid(column=3, row=1)

#label is equal to
iet = Label(text='is equal to')
iet.grid(column=1, row=2)

#label km
km = Label(text='Km')
km.grid(column=3, row=2)

#output km
km_output = Label(text='0')
km_output.grid(column=2, row=2)

#Button
button = Button(text='Calculate', command=miles_to_km)
button.grid(column=2, row=3)

window.mainloop()