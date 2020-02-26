from tkinter import *


def colourUpdate():
    colour.set('red' if colour.get() != 'red' else 'blue')
    print(colour.get())
    l.configure(fg=colour.get())


root = Tk()

colour = StringVar()
colour.set('red')

button = Button(root, text="Click Me", command=colourUpdate)
l = Label(root, textvariable=colour, fg=colour.get())

l.pack()
button.pack()

root.mainloop()
