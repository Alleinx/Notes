import tkinter as tk

top = tk.Tk()
top.geometry('500x500')
quit = tk.Button(top, text='hello world',
                 command=top.quit)
quit.pack()
tk.mainloop()
