import tkinter as tk
from tkinter import Menu
import tkinter.messagebox as mbx
import tkinter.filedialog as fbl

root = tk.Tk()
root.title('Блокнот')

mainmenu = Menu(root)
s = str()
root.config(menu=mainmenu)
filemenu = Menu(mainmenu, tearoff=0)
def open_func():
    global s,TextField
    fname = fbl.askopenfilename()
    with open (fname,'r') as f:
        s=f.read()
    TextField.insert(1.0,s)

filemenu.add_command(
    label="Открыть",
    command=open_func
)
def save_func():
    global s,TextField
    fname = fbl.asksaveasfile()
    with open (fname,'w') as f:
        f.write(s)
    TextField.insert(1.0,s)

filemenu.add_command(
    label="Сохранить...",
    command = save_func
)
mainmenu.add_cascade(
    label="Файл",
    menu=filemenu
)

helpmenu = Menu(mainmenu, tearoff=0)

helpmenu.add_command(
    label="Об авторе"
)

mainmenu.add_cascade(
    label="Помощь",
    menu=helpmenu
)
TextField = tk.Text(root,wrap=tk.WORD)
TextField.grid(row=0,column=0)
TextField.insert(1.0,s)

root.mainloop()