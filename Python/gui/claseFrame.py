from tkinter import *

raiz=Tk()
raiz.title("Creación de un Frame sobre el contenedor raiz")
raiz.iconbitmap("gui/telegram.ico")
raiz.config(bg="yellow")

myFrame=Frame() #Contruimos un marco llamando a la clase Frame()
myFrame.pack() #metemos el marco dentro de la ventana raiz (Lo empaquetamos) y se queda arriba por defecto
# myFrame.pack(side="left", anchor="n") #Podemos anclar el marco a la izquierda y al norte
# myFrame.pack(fill="x") #Podemos rellenar el marco sobre la raiz en el eje x
# myFrame.pack(fill="y", expand=True) #Podemos rellenar el marco sobre la raiz en el eje y
# myFrame.pack(fill="both", expand=True) #Podemos rellenar la raiz por completo a la dimensión del marco
myFrame.config(width="650", height="350") #le damos un tamaño al marco
myFrame.config(bg="purple") #Le damos un color de fondo al marco
myFrame.config(bd="35") #Grueso del borde
myFrame.config(relief="groove") #Tipo de borde
myFrame.config(cursor="spider") #Cambia la imagen del cursor



raiz.mainloop()