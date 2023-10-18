from tkinter import * #importamos la librería tkinter

raiz=Tk()
#Llamamos a la clase Tk. La raiz es la ventana principal, dentro de la cual irá el marco(frame)
raiz.title("Mi primera ventana con Python")
#Damos el título a la ventana
raiz.resizable(0, 0) 
#(0, 0)No deja que la ventana sea redimensionada
#(1, 0)Solo deja redimensionar el ancho
#(0, 1)Solo deja redimensionar el alto
#(0, 1)Deja redimensionar el ancho y el alto
#También podemos redimensionarlo usando los booleans (True, True), (False, True), ...etc.
raiz.iconbitmap("telegram.ico")
#Para cambiar el icono, tienes que convertir una imagen a una extensión .ico (Hay conversores en google)
raiz.geometry("650x350")
#Establece el tamaño de la ventana
raiz.config(bg="purple")
#bg es background

raiz.mainloop() 
#mainloop es un bucle infinito, para que la ventana esté siempre abierta. Siempre debe estar al final

