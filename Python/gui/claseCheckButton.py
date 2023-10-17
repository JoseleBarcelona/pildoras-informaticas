from tkinter import *

root=Tk()
root.geometry("300x300")
root.title("Viajes")

playa=IntVar()
muntanya=IntVar()
turismoRural=IntVar()

def opcionViajes():
    opcionEscogida=""

    if playa.get()==1:
        opcionEscogida+=" Playa,"
    if muntanya.get()==1:
        opcionEscogida+=" Montaña,"
    if turismoRural.get()==1:
        opcionEscogida+=" Turismo rural"

    textoFinal.config(text=opcionEscogida, foreground="blue")

frame=Frame(root)
frame.pack()

foto=PhotoImage(file="gui/plane.png")
etiqueta=Label(frame, image=foto)
etiqueta.grid(row=0)

encabezado=Label(frame, text="ELIGE DESTINOS", fg="blue")
encabezado.grid(row=1)

chequeo1=Checkbutton(frame, text="Playa", variable=playa, onvalue=1, offvalue=0, command=opcionViajes)
chequeo2=Checkbutton(frame, text="Montaña", variable=muntanya, onvalue=1, offvalue=0, command=opcionViajes)
chequeo3=Checkbutton(frame, text="Turismo Rural", variable=turismoRural, onvalue=1, offvalue=0, command=opcionViajes)

chequeo1.grid(sticky=W)
chequeo2.grid(sticky=W)
chequeo3.grid(sticky=W)

textoFinal=Label(root)
textoFinal.pack()


root.mainloop()



