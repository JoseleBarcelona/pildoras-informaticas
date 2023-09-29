mitupla = ("Juan", 13, 1, 1995)
print(mitupla)
print(mitupla[1])

milista = list(mitupla) #Convertimos una tupla en una lista (Refundición)
print(milista)

milista2 = ["Antonio", "Federico", 1, 1, 1, 45.5, False]
print(milista2)

mitupla2 = tuple(milista2) #Convertimos una lista en una tupla
print(mitupla2)
print("Juan" in mitupla2)
print("Antonio" in mitupla2)

print(mitupla2.count(1)) #Cuenta cuantos elementos, (entre paréntesis) hay iguales, en este caso tres 1.
print(len(mitupla2)) #lenght te cuenta el número de elementos que hay

mitupla3 = ("Leche",) #Para crear una tupla unitaria, es necesario poner una coma al final de elemento
print(len(mitupla3))
print(mitupla3)

mitupla4 = "Mariano", 141, 15.6 #Si no le ponemos los (), también interpreta que es una tupla
print(mitupla4)

nombre, dia, mes, agno = mitupla #Se puede asignar a variables, los valores de una tupla.(Desempaquetado)
print(dia, agno, nombre, mes)
print(agno, dia, mes, nombre)


#('Juan', 13, 1, 1995)
#13
#['Juan', 13, 1, 1995]
#['Antonio', 'Federico', 1, 1, 1, 45.5, False]
#('Antonio', 'Federico', 1, 1, 1, 45.5, False)
#False
#True
#3
#7
#1
#('Leche',)
#('Mariano', 141, 15.6)
#13 1995 Juan 1
#1995 13 1 Juan
