from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

window = Tk()
window.title("Codingal's Text editor")
window.geometry("1080x720")
window.rowconfigure(0, minisize = 800, weight = 1)
window.columfigure(1, minisize = 800, weight = 1)

def open_file():
    """Open a file for editing."""
    filepath = askopenfilename(
     filetypes =[("Text Files","*.txt"),("All Files","*.*")]
    )
    if not filepath:
        return
    txt_edit.delete(1.0, END)

    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(END, text)
        input_file.close()
    window.title(f"Codigal text editor - {filepath}")

def save_file():
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes =[("Text Files","*.txt"),("All Files","*.*")]
    )

txt.edit= Text(window)
fr_buttons = Frame(window, relief=RAISED, bd=2)
btn_open = Button(fr_buttons, text="Open",command=open_file)
btn_save = Button(fr_buttons, text="Save As...",command=open_file)


btn_open.grid(row = 0, column = 0, sticky="ns")
btn_save.grid(row = 0, column = 1, sticky="nsew")

window.mainloop()




    