from tkinter import *
from tkinter import ttk
global root
root = None
global output
output = None
global initialized
initialized = False
def load():
    try:
        loadedfile = open(text.get("1.0","end-1c"))
        output = loadedfile.read()
        print(output)
    except Exception:
        pass
    print(root)
    frm = None
    text = None
    button = None
def init_select_window():
    global root
    root = Tk()
    global frm
    frm = ttk.Frame(root, padding=10)
    global text
    text = Text(root, height=8)
    text.pack()
    global button
    button = ttk.Button(root, text="Load", command=load)
    button.pack(ipadx=5,ipady=5,expand=True)
