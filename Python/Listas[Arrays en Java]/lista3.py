miLista = ["José", 5, True, 6.54]

print(miLista[:]) #[:] esto dice que imprima toda la lista, es lo mismo que print(miLista)
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


#['José', 5, True, 6.54]
#True
#6.54
#[5, True, 6.54]
#[5, True]
#[5, True, 50, False, 69.74]
#[1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6]
