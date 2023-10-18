from tkinter import *
from tkinter import filedialog

root=Tk()

def abreFichero():
    fichero=filedialog.askopenfilename(title="Abrir", initialdir="C:", filetypes=(("Ficheros de Excel", "*.xlsx"),
    ("Ficheros de texto", "*.txt"), ("Todos los ficheros", "*.*"))) 
    #Por defecto abre en la carpeta Documentos
    print(fichero) #Esto nos muestra la ruta

Button(root, text="Abrir fichero", command=abreFichero).pack()



root.mainloop()