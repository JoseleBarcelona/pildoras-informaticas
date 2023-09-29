
def generaPares(limite): #Función normal

    num=1
    milista=[]

    while num<limite:
        milista.append(num*2)
        num+=1

    return milista

print(generaPares(10))
#[2, 4, 6, 8, 10, 12, 14, 16, 18]

#______________________________________________________________________________________________________

def generaPares2(limite): #Función generadora

    num=1

    while num<limite:
        yield num*2 #yield construye un objeto iterable con los valores de la lista y los almacena de uno en uno
        num+=1
devuelvePares = generaPares2(10) #la variable devulvePares es una variable objeto donde almacenamos el objeto iterable que devuelve la funcion

for i in devuelvePares:
    print(i)
print("")

#_______________________________________________________________________________________________________

def generaPares3(limite): #Función generadora

    num=1

    while num<limite:
        yield num*2
        num+=1

devuelvePares = generaPares3(10)

print(next(devuelvePares))   #next devuelve el primer valor que tiene almacenado el objeto generador
print("Aquí pordría haber más código")
print(next(devuelvePares))
print("Aquí pordría haber más código")
print(next(devuelvePares))
print("Aquí pordría haber más código")


# [2, 4, 6, 8, 10, 12, 14, 16, 18]
# 2
# 4
# 6
# 8
# 10
# 12
# 14
# 16
# 18

# 2
# Aquí pordría haber más código
# 4
# Aquí pordría haber más código
# 6
# Aquí pordría haber más código