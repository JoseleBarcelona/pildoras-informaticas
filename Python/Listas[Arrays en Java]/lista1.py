#las listas a diferencia que en Java, pueden ser de distintos tipos

miLista = ["José", "Núria", "Neus", "Papa", "Mama"]
#los índices positivos se cuentan desde el principio 0, 1, 2
#Los índices negativos se cuentan desde el final -3,-2,-1

print(miLista)
print(miLista[2]) #Neus
print(miLista[-2]) #Papa
print(miLista[0:3]) #Imprime los 3 primeros elementos desde el indice 0, 0 1 2
print(miLista[:3]) #Forma abreviada de la anterior
print(miLista[1:3]) #Desde el índice 1, imprime el índice 1 2
print(miLista[1:4])
print(miLista[2:4])
print(miLista[3:]) #Desde el índice 3 hasta el final



#['José', 'Núria', 'Neus', 'Papa', 'Mama']
#Neus
#Papa
#['José', 'Núria', 'Neus']
#['José', 'Núria', 'Neus']
#['Núria', 'Neus']
#['Núria', 'Neus', 'Papa']
#['Neus', 'Papa']
#['Papa', 'Mama']
