from tkinter import *

root = Tk()
root.geometry("400x300")
root.title("main")

def topwin():
    top = Toplevel()
    top.geometry("180x100")
    top.title("Level")

    l2 = Label(top, text = "This is the top level window")
    l2.pack()

    top.mainloop()

    l = Label(top, text="This is root window")
    btn = Button(root, text="Click here to open another window", command=topwin)

    l.pack()
    btn.pack()




