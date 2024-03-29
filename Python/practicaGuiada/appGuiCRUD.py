from tkinter import *
from tkinter import messagebox
import sqlite3


#------------------------funciones--------------------------#

def conexionBBDD():
    miConexion=sqlite3.connect("Usuarios")
    miCursor=miConexion.cursor()
    try:
        miCursor.execute('''
            CREATE TABLE DATOSUSUARIOS (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NOMBRE_USUARIO VARCHAR(50),
            PASSWORD VARCHAR(50),
            APELLIDO VARCHAR(10),
            DIRECCION VARCHAR(50),
            COMENTARIOS VARCHAR(100))
            ''')
        messagebox.showinfo("BBDD", "BBDD creada con éxito")

    except:
        messagebox.showwarning("¡Atención!", "La BBDD ya existe")

    miCursor.close()
    miConexion.close()

def salirAplicacion():
    valor=messagebox.askquestion("Salir", "¿Deseas salir de la aplicacion?")
    if valor=="yes":
        root.destroy()

def borrarCampos():
    miNombre.set("")
    miId.set("")
    miApellido.set("")
    miPassw.set("")
    miDireccion.set("")
    textoComentario.delete(1.0, END)

def crearRegistros():
    miConexion=sqlite3.connect("Usuarios")
    miCursor=miConexion.cursor()

    # miCursor.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL, '" + miNombre.get() +
    #                 "','" + miPassw.get() +
    #                 "','" + miApellido.get() +
    #                 "','" + miDireccion.get() +
    #                 "','" + textoComentario.get("1.0", END) + "')")

    datos=miNombre.get(), miPassw.get(), miApellido.get(), miDireccion.get(), textoComentario.get("1.0", END)
    miCursor.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL,?,?,?,?,?)",(datos))

    miConexion.commit()
    messagebox.showinfo("BBDD", "Registro insertado con éxito")

    miCursor.close()
    miConexion.close()

def leer():
    miConexion=sqlite3.connect("Usuarios")
    miCursor=miConexion.cursor()

    miCursor.execute("SELECT * FROM DATOSUSUARIOS WHERE ID=" + miId.get())
    elusuario=miCursor.fetchall() #Esto devuelve una array de todos los campos

    for usuario in elusuario: #Con el bucle recorremos el array
        miId.set(usuario[0]) #A miId le establecemos lo que leamos en el índice 0
        miNombre.set(usuario[1]) #A miNombre le establecemos lo que leamos en el índice 1
        miPassw.set(usuario[2])
        miApellido.set(usuario[3])
        miDireccion.set(usuario[4])
        textoComentario.insert(1.0, usuario[5]) #Leemos el cuadro de texto desde el primer caracter

    miConexion.commit()


    miCursor.close()
    miConexion.close()

def actualizar():
    miConexion=sqlite3.connect("Usuarios")
    miCursor=miConexion.cursor()

    # miCursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE_USUARIO='" + miNombre.get() +
    #                  "', PASSWORD='" + miPassw.get() +
    #                  "', APELLIDO='" + miApellido.get() +
    #                  "', DIRECCION='" + miDireccion.get() +
    #                  "', COMENTARIOS='" + textoComentario.get("1.0", END) +
    #                  "' WHERE ID=" + miId.get())

    datos=miNombre.get(), miPassw.get(), miApellido.get(), miDireccion.get(), textoComentario.get("1.0", END)
    miCursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE_USUARIO=?, PASSWORD=?, APELLIDO=?, "
                     "DIRECCION=?, COMENTARIOS=?" + "WHERE ID=" + miId.get(),(datos))

    miConexion.commit()
    messagebox.showinfo("BBDD", "Registro actualizado con éxito")
    miCursor.close()
    miConexion.close()

def eliminarRegistros():
    miConexion=sqlite3.connect("Usuarios")
    miCursor=miConexion.cursor()
    miCursor.execute("DELETE FROM DATOSUSUARIOS WHERE ID=" + miId.get())



    miConexion.commit()
    messagebox.showinfo("BBDD", "Registro borrado con éxito")
    miCursor.close()
    miConexion.close()

    #----------------Creación de menú y submenús----------------#
    
root=Tk()
barraMenu=Menu(root)
root.config(menu=barraMenu, width=300, height=300)
# root.geometry("600x600")

bbddMenu=Menu(barraMenu, tearoff=0)
bbddMenu.add_command(label="Conectar", command=conexionBBDD)
bbddMenu.add_command(label="Salir", command=salirAplicacion)

borrarMenu=Menu(barraMenu, tearoff=0)
borrarMenu.add_command(label="Borrar campos", command=borrarCampos)

crudMenu=Menu(barraMenu, tearoff=0)
crudMenu.add_command(label="Crear", command=crearRegistros)
crudMenu.add_command(label="Leer", command=leer)
crudMenu.add_command(label="Actualizar", command=actualizar)
crudMenu.add_command(label="Borrar", command=eliminarRegistros)

AyudaMenu=Menu(barraMenu, tearoff=0)
AyudaMenu.add_command(label="Licencia")
AyudaMenu.add_command(label="Acerca de...")

barraMenu.add_cascade(label="BBDD", menu=bbddMenu)
barraMenu.add_cascade(label="Borrar", menu=borrarMenu)
barraMenu.add_cascade(label="CRUD", menu=crudMenu)
barraMenu.add_cascade(label="Ayuda", menu=AyudaMenu)

#----------------Creación de campos-------------------------#

miFrame=Frame(root)
miFrame.pack()

miId=StringVar()
miNombre=StringVar()
miApellido=StringVar()
miPassw=StringVar()
miDireccion=StringVar()

cuadroId=Entry(miFrame, textvariable=miId)
cuadroId.grid(row=0, column=1, padx=10, pady=10)

cuadroNombre=Entry(miFrame, textvariable=miNombre)
cuadroNombre.grid(row=1, column=1, pady=10, padx=10)
cuadroNombre.config(fg="red", justify="right")

cuadroPassw=Entry(miFrame, textvariable=miPassw)
cuadroPassw.grid(row=2, column=1, padx=10, pady=10)
cuadroPassw.config(show="*")

cuadroApellido=Entry(miFrame, textvariable=miApellido)
cuadroApellido.grid(row=3, column=1, pady=10, padx=10)

cuadroDireccion=Entry(miFrame, textvariable=miDireccion)
cuadroDireccion.grid(row=4, column=1, padx=10, pady=10)

textoComentario=Text(miFrame, width=16, height=5)
textoComentario.grid(row=5, column=1, pady=10, padx=10)
scrollVertical=Scrollbar(miFrame, command=textoComentario.yview)
scrollVertical.grid(row=5, column=2, sticky="nsew", padx=4, pady=4)
textoComentario.config(yscrollcommand=scrollVertical.set)

#----------------Creación de etiquetas-------------------------#

idLabel=Label(miFrame, text="Id:")
idLabel.grid(row=0, column=0, sticky="w", pady=10, padx=10)

nombreLabel=Label(miFrame, text="Nombre:")
nombreLabel.grid(row=1, column=0, sticky="w", padx=10, pady=10)

passLabel=Label(miFrame, text="Password:")
passLabel.grid(row=2, column=0, sticky="w", padx=10, pady=10)

apellidoLabel=Label(miFrame, text="Apellido:")
apellidoLabel.grid(row=3, column=0, sticky="w", padx=10, pady=10)

direccionLabel=Label(miFrame, text="Dirección:")
direccionLabel.grid(row=4, column=0, sticky="w", padx=10, pady=10)

comentariosLabel=Label(miFrame, text="Comentarios:")
comentariosLabel.grid(row=5, column=0, sticky="w", padx=10, pady=10)

#----------------Creación de botones-------------------------#

miframe2=Frame(root)
miframe2.pack()

botonCrear=Button(miframe2, text="Create", command=crearRegistros)
botonCrear.grid(row=0, column=0, sticky="e", pady=10, padx=10)

botonLeer=Button(miframe2, text="Read", command=leer)
botonLeer.grid(row=0, column=1, sticky="e", pady=10, padx=10)

botonActualizar=Button(miframe2, text="Update", command=actualizar)
botonActualizar.grid(row=0, column=2, sticky="e", pady=10, padx=10)

botonBorrar=Button(miframe2, text="Delete", command=eliminarRegistros)
botonBorrar.grid(row=0, column=3, sticky="e", pady=10, padx=10)

root.mainloop()
