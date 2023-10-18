from tkinter import *
root=Tk()
#------------Creamos un menú en la barra de marcadores (Raiz)---------------

barraMenu=Menu(root)
root.config(menu=barraMenu, width=300, height=300, background="pink")

#-------------------Creamos varios submenus---------------------------------

archivoMenu=Menu(barraMenu, tearoff=0)

#----------------Dentro del submenu, creamos opciones-----------------------

archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar Como")
archivoMenu.add_separator()  #colocamos una linea de separación
archivoMenu.add_command(label="Cerrar")
archivoMenu.add_command(label="Salir")

archivoEdicion=Menu(barraMenu, tearoff=0)

archivoEdicion.add_command(label="Copiar")
archivoEdicion.add_command(label="Cortar")
archivoEdicion.add_command(label="Pegar")

archivoHerramientas=Menu(barraMenu, tearoff=0)

archivoHerramientas.add_command(label="Inspeccionar Código")
archivoHerramientas.add_command(label="Depurar Código")
archivoHerramientas.add_command(label="Consola del Navegador")

archivoAyuda=Menu(barraMenu, tearoff=0)

archivoAyuda.add_command(label="Licencia")
archivoAyuda.add_command(label="Acerca de")

#-----------------------Mostramos los 4 submenus-----------------------------

barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
barraMenu.add_cascade(label="Edición", menu=archivoEdicion)
barraMenu.add_cascade(label="herramientas", menu=archivoHerramientas)
barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)



root.mainloop()