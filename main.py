from tkinter import *


def mile_to_km():
    miles = float(entry.get())
    km = miles * 1.609
    label3.config(text=km)


window = Tk()
window.title("Mile to Km Convertor")
window.config(padx=20, pady=20)

entry = Entry(width=20)
entry.insert(END, string="0")
entry.grid(column=1, row=0)
label1 = Label(text="Miles")
label1.grid(column=2, row=0)

label2 = Label(text="is equal to")
label2.grid(column=0, row=1)

label3 = Label(text="0")
label3.grid(column=1, row=1)

label4 = Label(text="Km")
label4.grid(column=2,row=1)


button = Button(text="CALCULATE", command=mile_to_km)
button.grid(column=1,row=2)


window.mainloop()