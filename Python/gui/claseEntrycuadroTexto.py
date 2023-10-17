from tkinter import *

raiz=Tk()
raiz.geometry("650x350")

miFrame=Frame(raiz)
miFrame.pack()

loginLabel=Label(miFrame, text="Login: ")
loginLabel.grid(row=0, column=0, sticky="w", pady=4)

passwLabel=Label(miFrame, text="Password: ")
passwLabel.grid(row=1, column=0, sticky="w", pady=4)

nombreLabel=Label(miFrame, text="Nombre: ")
nombreLabel.grid(row=2, column=0, sticky="w", pady=4)

apellidoLabel=Label(miFrame, text="Apellido: ")
apellidoLabel.grid(row=3, column=0, sticky="w", pady=4)

direccionLabel=Label(miFrame, text="Dirección: ")
direccionLabel.grid(row=4, column=0, sticky="w", pady=4)

comentariosLabel=Label(miFrame, text="Comentarios: ")
comentariosLabel.grid(row=5, column=0, sticky="w", pady=4)

cuadroTextoLogin=Entry(miFrame)
cuadroTextoLogin.grid(row=0, column=1)
cuadroTextoLogin.config(fg="red", justify="center")

cuadroTextoPassw=Entry(miFrame)
cuadroTextoPassw.grid(row=1, column=1)
cuadroTextoPassw.config(fg="red", justify="center", show="*")

minombre=StringVar()

cuadroTextoNombre=Entry(miFrame, textvariable=minombre)
cuadroTextoNombre.grid(row=2, column=1)
cuadroTextoNombre.config(fg="red", justify="center")

cuadroTextoApellido=Entry(miFrame)
cuadroTextoApellido.grid(row=3, column=1)
cuadroTextoApellido.config(fg="red", justify="center")

cuadroTextoDireccion=Entry(miFrame)
cuadroTextoDireccion.grid(row=4, column=1)
cuadroTextoDireccion.config(fg="red", justify="center")

textoComentarios=Text(miFrame, width=20, height=10)
textoComentarios.grid(row=5, column=1, pady=4)

scrollVertical=Scrollbar(miFrame, command=textoComentarios.yview)
scrollVertical.grid(row=5, column=2, sticky="nsew")
textoComentarios.config(yscrollcommand=scrollVertical.set)

def codigoBoton():
    minombre.set("José")

botonEnviar=Button(raiz, text="Enviar", command=codigoBoton)
botonEnviar.pack()


raiz.mainloop()
