miLista = ["José", "Núria", "Neus"]

print(miLista)

miLista.append("Papa")
print(miLista)

miLista.append("Mama")
print(miLista)

miLista.insert(2, "Juanito")
print(miLista)

miLista.extend(["Andrés", "Lolo", "María"])
print(miLista)

print(miLista.index("Papa")) #índice 4
print(miLista.index("Lolo")) #índice 7

print("José" in miLista) #True
print("Federico" in miLista) #False

#['José', 'Núria', 'Neus']
#['José', 'Núria', 'Neus', 'Papa']
#['José', 'Núria', 'Neus', 'Papa', 'Mama']
#['José', 'Núria', 'Juanito', 'Neus', 'Papa', 'Mama']
#['José', 'Núria', 'Juanito', 'Neus', 'Papa', 'Mama', 'Andrés', 'Lolo', 'María']
#4
#7
#True
#False
