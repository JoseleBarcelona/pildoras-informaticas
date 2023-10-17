from tkinter import *

root=Tk()
miFrame=Frame(root, width=600, height=600)
miFrame.pack()
miImagen=PhotoImage(file="gui/whatsapp.png")
Label(miFrame, image=miImagen).place(x=30, y=30)


root.mainloop()