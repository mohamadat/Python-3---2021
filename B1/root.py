from tkinter import *

z = 7

def addtext():
    global z
    label = Label(text='Hello world!', fg="red").grid(row=z, column=3)
    z = z + 1




root = Tk()
root.title('my root app')
root.geometry('500x500')

# btn = Button(text='1').pack()
# btn2 = Button(text='1').place(x=1, y=1)
# btn3 = Button(text='1').place(x=1, y=100)
btn4 = Button(text='1').grid(row=1, column=1)
btn5 = Button(text='1').grid(row=2, column=1)
btn6 = Button(text='1').grid(row=3, column=1)

label = Label(text='name').grid(row=1, column=2)
entry = Entry(width=50).grid(row=1, column=3)

label2 = Label(text='name').grid(row=2, column=2)
entry2 = Entry(width=50).grid(row=2, column=3)

label3 = Label(text='name').grid(row=3, column=2)
entry3 = Entry(width=50).grid(row=3, column=3)

button = Button(text= "add text", command=addtext)
button.grid(row=4, column=3)



root.mainloop()