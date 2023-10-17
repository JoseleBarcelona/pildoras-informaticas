from tkinter import *

root=Tk()
miFrame=Frame(root, width=500, height=400) 
#En el constructor le decimos que el marco estará en la raiz (le decimos cual va a ser su contenedor padre)
#  y las dimensiones que va a tener el marco

miFrame.pack() #Lo empaquetamos (metemos dentro de la ventana raiz)

miLabel=Label(miFrame, text="Hola Mundo") #Elegimos el contenedor padre "miFrame" y escribimos el texto de la etiqueta
miLabel.place(x=10, y=10) #Situa el texto dentro de unas coordenadas dentro del marco
miLabel.config(fg="purple")
miLabel.config(font=("Comic Sans MS", 14)) #Elige el tipo y tamaño de la fuente


# Label(miFrame, text="Hola Mundo", fg="purple", font=("Comic Sans MS", 18)).place(x=10, y=10)
# Esto es una manera de abreviar las lineas de código anterior



root.mainloop()