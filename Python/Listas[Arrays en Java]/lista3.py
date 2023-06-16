miLista = ["José", 5, True, 6.54]

print(miLista)
print(miLista[2])
print(miLista[3])

miLista.remove("José")
print(miLista)

miLista.pop() #elimina el último elemento de la lista
print(miLista)

miLista2 = [50, False, 69.74]
miLista3 = miLista + miLista2 #Concatena listas
print(miLista3)

miLista4 = [1,2,3,4,5,6] * 5 #Repite la lista x veces, en este caso 5 veces
print(miLista4)
