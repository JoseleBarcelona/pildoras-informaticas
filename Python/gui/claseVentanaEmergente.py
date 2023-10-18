from tkinter import *
from tkinter import messagebox  #importamos la clase que ejecuta ventanas emergentes

root=Tk()

def informacionAdicional():
    messagebox.showinfo("Procesador de texto de José", "Procesador de texto versión 2023")

def avisoLicencia():
    messagebox.showwarning("Licencia", "Producto bajo licencia GNU/Linux")

def salirAplicacion():
    valor=messagebox.askquestion("Salir", "¿Desea salir de la aplicación?") 
    #askquestion devuelve yes o no, por lo que la podemos guardar en una variable y jugar con ella
    
    if valor=="yes":
        root.destroy() #Destroy cierra la aplicación (la ventana principal)

    # valor2=messagebox.askokcancel("Cerrar", "¿Deseas cerrar la aplicación?")
    # if valor2==True:
    #     root.destroy()
    #askokcancel devuelve True o False
        
def cerrarDocumento():
    valor3=messagebox.askretrycancel("Reintentar", "No es posible cerrar, documento bloqueado")
    if valor3==False:
        root.destroy()

barraMenu=Menu(root)
root.config(menu=barraMenu, width=300, height=300, background="pink")

archivoMenu=Menu(barraMenu, tearoff=0)

archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar Como")
archivoMenu.add_separator()  
archivoMenu.add_command(label="Cerrar", command=cerrarDocumento)
archivoMenu.add_command(label="Salir", command=salirAplicacion)

archivoEdicion=Menu(barraMenu, tearoff=0)

archivoEdicion.add_command(label="Copiar")
archivoEdicion.add_command(label="Cortar")
archivoEdicion.add_command(label="Pegar")

archivoHerramientas=Menu(barraMenu, tearoff=0)

archivoHerramientas.add_command(label="Inspeccionar Código")
archivoHerramientas.add_command(label="Depurar Código")
archivoHerramientas.add_command(label="Consola del Navegador")

archivoAyuda=Menu(barraMenu, tearoff=0)

archivoAyuda.add_command(label="Licencia", command=avisoLicencia)
archivoAyuda.add_command(label="Acerca de", command=informacionAdicional)

barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
barraMenu.add_cascade(label="Edición", menu=archivoEdicion)
barraMenu.add_cascade(label="herramientas", menu=archivoHerramientas)
barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)



root.mainloop()