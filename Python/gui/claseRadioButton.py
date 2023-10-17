from tkinter import *

root=Tk()
root.geometry("300x300")

frame=Frame(root)
frame.pack()

# Crear el texto "GÉNERO"
label=Label(frame, text="GÉNERO")

# Alinear el texto en la parte superior
label.grid(row=0)

# Crear tres botones de radio
varOpcion=IntVar()

def imprimir():
    if varOpcion.get()==1:
        etiqueta.config(text="Has elegido masculino")
    elif varOpcion.get()==2:
        etiqueta.config(text="Has elegido femenino")
    else:
        etiqueta.config(text="Has elegido otros")

boton1=Radiobutton(frame, text="Masculino", variable=varOpcion, value=1, command=imprimir)
boton2=Radiobutton(frame, text="Femenino", variable=varOpcion, value=2, command=imprimir)
boton3=Radiobutton(frame, text="Otros", variable=varOpcion, value=3, command=imprimir)

# Alinear los botones de radio verticalmente
boton1.grid(sticky=W)
boton2.grid(sticky=W)
boton3.grid(sticky=W)

# Crear una etiqueta para mostrar el resultado
etiqueta=Label(root)
etiqueta.pack()

# Iniciar el bucle principal de la ventana
root.mainloop()
