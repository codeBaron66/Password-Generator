import tkinter as tk
from tkinter import *
from random import *
import string
from tkinter.constants import ACTIVE, HORIZONTAL
from typing import NewType
from typing_extensions import IntVar

window = tk.Tk()
window.title("Password Generator")
window.geometry("520x400")
window.option_add("*Font", "Arial 18")
ps_length = tk.IntVar()
specChars = tk.IntVar()
#etra info

def genPswd():
    length = ps_length.get()
    special = specChars.get()
    characters = string.ascii_letters + string.digits
    charPunc = string.ascii_letters + string.digits + string.punctuation
    if special == 0:
        password = "".join(choice(characters) for x in range (length))
    else:
        password = "".join(choice(charPunc) for x in range (length))
    global newPass
    newPass = password
    label.config(text=newPass)
    copyBtn.config(state=NORMAL)
    saveBtn.config(state=NORMAL)

def savePass():
    newWindow = Toplevel(window)
    newWindow.title("Save Password")
    newWindow.geometry("300x500")
    newWindow.option_add("*Font", "Arial 18")
    nameLabel = tk.Label(newWindow, bg="white", padx=15, pady=10, text="Name")
    nameLabel.pack()
    entry = Entry(newWindow, width= 20)
    entry.focus_set()
    entry.pack()
    global kill
    def kill():
        global log
        log = entry.get()
        textFile = open("saved.txt", 'a')
        textFile.write(f"\n" + log + ": " + newPass)
        textFile.close()
        newWindow.destroy()
    # newWindow.bind('<Return>', kill)
    okBtn = tk.Button(newWindow, text="Save", padx=30, pady=10, command=kill)
    okBtn.pack()

def copy():
    window.clipboard_clear()
    window.clipboard_append(newPass)
    window.update()

def savedPass():
    newWindow = Toplevel(window)
    newWindow.title("Saved Passwords")
    newWindow.geometry("500x500")
    scroll = tk.Scrollbar(newWindow, orient=VERTICAL)
    scroll.pack()
    newWindow.option_add("*Font", "Arial 18")
    textFile = open("saved.txt", 'r')
    text = textFile.read()
    textFile.close()
    nameLabel = tk.Label(newWindow, bg="white", padx=15, pady=10, text=f"{text}", command=scroll.set)
    nameLabel.config(yscrollcommand=scroll.set)
    nameLabel.pack()
    scroll.config( command = nameLabel.yview)
    def kill():
        # newWindow.bind('<Return>', kill)
        newWindow.destroy()
    closeBtn = tk.Button(newWindow, text="Close", padx=30, pady=10, command=kill)
    closeBtn.pack()

m = Menu(window, tearoff = 0)
m.add_command(label ="Copy", command=copy)
def do_popup(event):
    try:
        m.tk_popup(event.x_root, event.y_root)
    finally:
        m.grab_release()

# labelBlank = tk.Label(window, bg="red", text="")
# labelBlank.pack()
label = tk.Label(window, bg="white", padx=15, pady=10, text="")
label.bind("<Button-3>", do_popup)
label.pack(side=TOP, pady=20)
slider = tk.Scale(window, from_=5, to=25, orient=HORIZONTAL, variable=ps_length)
slider.pack()
chkBtn4 = tk.Checkbutton(window, text="@!£&#...", variable=specChars, onvalue=1, offvalue=0)
chkBtn4.pack()
genBtn = tk.Button(window, text="Generate", padx=30, pady=10, command=genPswd)
genBtn.pack()
copyBtn = tk.Button(window, text="   Copy    ", padx=30, pady=10, state=DISABLED, command=copy)
copyBtn.pack()
saveBtn = tk.Button(window, text="   Save    ", padx=30, pady=10, state=DISABLED, command=savePass)
saveBtn.pack()
savedBtn = tk.Button(window, text="Saved", padx=30, pady=10, command=savedPass)
savedBtn.pack()

# labelBlank.grid(row=0, column=10)
window.mainloop()
