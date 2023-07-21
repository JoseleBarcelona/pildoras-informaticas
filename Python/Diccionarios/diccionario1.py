midiccionario = {"Alemania":"Berlín", "Francia":"París", "Reino Unido":"Londres", "España":"Madrid"}
midiccionario["Italia"] = "Lisboa"

print(midiccionario["Francia"])
print(midiccionario)

midiccionario["Italia"] = "Roma" #sobrescribe
print(midiccionario)

del midiccionario["Reino Unido"] #elimina una entrada
print(midiccionario)

midiccionario2 = {23:"Michael Jordan", "Mosqueteros": 3}
print(midiccionario2)

mitupla = ["España", "Francia", "Italia"]
midiccionario3 = {mitupla[0]: "Madrid", mitupla[1]: "París", mitupla[2]: "Roma"}

print(midiccionario3)
print(midiccionario3["Francia"])

#Tambien podemos insertar una tupla dentro de un diccionario

midiccionario4 = {23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago", "Anillos":[1991, 1992, 1993, 1996, 1997, 1998]}
print(midiccionario4)
print(midiccionario4["Anillos"])

#También podemos meter un diccionario dentro de otro diccionario y dentro del último, meter una tupla

midiccionario4 = {23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago", "Anillos":{"Temporadas":[1991, 1992, 1993, 1996, 1997, 1998]}}
print(midiccionario4["Anillos"])
print(midiccionario4.keys())
print(midiccionario4.values())
print(len(midiccionario4))