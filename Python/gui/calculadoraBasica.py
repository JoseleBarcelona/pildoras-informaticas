from tkinter import *

root=Tk()
root.geometry("265x290")

miFrame=Frame(root)
miFrame.pack()

operacion=""
resultado=0

#-----------------------------------pantalla----------------------------------#
numeroPantalla=StringVar()
pantalla=Entry(miFrame, width=36, textvariable=numeroPantalla)
pantalla.grid(row=1, column=1, columnspan=4, pady=20)
pantalla.config(background="black", foreground="green", justify="right")
pantalla.config(borderwidth=10)

#----------------------------pulsaciones teclado------------------------------#

def numeroPulsado(num):
    global operacion
    if operacion!="":
        numeroPantalla.set(num)
        operacion=""

    else:
        numeroPantalla.set(numeroPantalla.get() + num)

#--------------------------------funcion suma---------------------------------#  

def suma(num):
    global operacion
    global resultado
    resultado+= int(num)
    operacion="suma"
    numeroPantalla.set(resultado)

#-----------------------------funcion resultado-------------------------------#

def resultadoFinal():
    global resultado
    numeroPantalla.set(resultado + int(numeroPantalla.get()))
    resultado=0

#----------------------------------fila 1-------------------------------------#

boton7=Button(miFrame, text="7", width=6, command=lambda:numeroPulsado("7"))
boton7.grid(row=3, column=1, pady=4)
boton8=Button(miFrame, text="8", width=6, command=lambda:numeroPulsado("8"))
boton8.grid(row=3, column=2, pady=4)
boton9=Button(miFrame, text="9", width=6, command=lambda:numeroPulsado("9"))
boton9.grid(row=3, column=3, pady=4)
botonDiv=Button(miFrame, text="/", width=6)
botonDiv.grid(row=3, column=4, pady=4)

#----------------------------------fila 2-------------------------------------#

boton4=Button(miFrame, text="4", width=6, command=lambda:numeroPulsado("4"))
boton4.grid(row=4, column=1, pady=4)
boton5=Button(miFrame, text="5", width=6, command=lambda:numeroPulsado("5"))
boton5.grid(row=4, column=2, pady=4)
boton6=Button(miFrame, text="6", width=6, command=lambda:numeroPulsado("6"))
boton6.grid(row=4, column=3, pady=4)
botonMult=Button(miFrame, text="x", width=6)
botonMult.grid(row=4, column=4, pady=4)

#----------------------------------fila 3-------------------------------------#

boton1=Button(miFrame, text="1", width=6, command=lambda:numeroPulsado("1"))
boton1.grid(row=5, column=1, pady=4)
boton2=Button(miFrame, text="2", width=6, command=lambda:numeroPulsado("2"))
boton2.grid(row=5, column=2, pady=4)
boton3=Button(miFrame, text="3", width=6, command=lambda:numeroPulsado("3"))
boton3.grid(row=5, column=3, pady=4)
botonResta=Button(miFrame, text="-", width=6)
botonResta.grid(row=5, column=4, pady=4)

#----------------------------------fila 4-------------------------------------#

boton0=Button(miFrame, text="0", width=6, command=lambda:numeroPulsado("0"))
boton0.grid(row=6, column=1, pady=4)
botonComa=Button(miFrame, text=",", width=6, command=lambda:numeroPulsado(","))
botonComa.grid(row=6, column=2, pady=4)
botonIgual=Button(miFrame, text="=", width=6, command=lambda:resultadoFinal())
botonIgual.grid(row=6, column=3, pady=4)
botonSuma=Button(miFrame, text="+", width=6, command=lambda:suma(numeroPantalla.get()))
botonSuma.grid(row=6, column=4, pady=4)


#----------------------------------bucle infinito-------------------------------------#
root.mainloop()

