from io import open

#DIFERENTES METODOS DE MANEJAR ARCHIVOS

# archivo_texto=open("indext.txt", "w")
# frase="Hola programadores\nbienvenidos al curso de Python."
# archivo_texto.write(frase)
# archivo_texto.close()
# del (archivo_texto) #Borramos la variable para que no se quede en el disco duro

# archivo_texto=open("indext.txt", "r")
# texto=archivo_texto.read()
# archivo_texto.close()
# print(texto)
# del (archivo_texto)

# archivo_texto=open("indext.txt", "r")
# lineas_texto=archivo_texto.readlines()
# archivo_texto.close()
# print(lineas_texto[0])
# del (archivo_texto)

# archivo_texto=open("indext.txt", "a")
# archivo_texto.write("\nSiempre es un placer aprender Python")
# archivo_texto.close()
# del (archivo_texto)

# archivo_texto=open("indext.txt", "r")
# print(archivo_texto.read())
# archivo_texto.seek(0)
# print(archivo_texto.read())
# archivo_texto.close()
# del (archivo_texto)

# archivo_texto=open("indext.txt", "r")
# archivo_texto.seek(11)
# print(archivo_texto.read())
# archivo_texto.close()
# del (archivo_texto)

# archivo_texto=open("indext.txt", "r")
# print(archivo_texto.read(11))
# print(archivo_texto.read())
# archivo_texto.close()
# del (archivo_texto)

# archivo_texto=open("indext.txt", "r")
# archivo_texto.seek(len(archivo_texto.read())/2)
# print(archivo_texto.read())
# archivo_texto.close()
# del (archivo_texto)

# archivo_texto=open("indext.txt", "r")
# archivo_texto.seek(len(archivo_texto.readline()))
# print(archivo_texto.read())
# archivo_texto.close()
# del (archivo_texto)

# archivo_texto=open("indext.txt", "r+")
# archivo_texto.write("Cambio de texto inicial")
# archivo_texto.close()
# del (archivo_texto)

# archivo_texto=open("indext.txt", "r+")
# lista_texto=archivo_texto.readlines()
# lista_texto[1]="Esta linea ha sido incluida desde el exterior\n"
# archivo_texto.seek(0)
# archivo_texto.writelines(lista_texto)
# archivo_texto.close()
# del (archivo_texto)
