import pickle

lista_nombres=["Núria", "Neus", "Jose", "Juanjo"] #Creamos una lista
fichero_binario=open("lista_nombres", "wb") #Creamos un fichero con permisos de escritura binaria
pickle.dump(lista_nombres, fichero_binario) #Volcamios la lista en el fichero binario permanente
fichero_binario.close() #Cerramos el fichero binario
del (fichero_binario) #Borramos el fichero binario de la memoria de nuestro ordenador


fichero=open("lista_nombres", "rb") #Abrimos el archivo binario con permisos de lectura binaria
lista=pickle.load(fichero) #Cargamos el fichero binario y lo guardamos en una variable llamada lista
print(lista) #Imprimimos en consola el resultado de la lista que contiene el fichero binario permanente
del (fichero) #Borramos el fichero binario de la memoria de nuestro ordenador