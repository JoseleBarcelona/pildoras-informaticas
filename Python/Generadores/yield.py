
def generaPares(limite): #Función normal

    num=1
    milista=[]

    while num<limite:
        milista.append(num*2)
        num+=1

    return milista

print(generaPares(10))
#[2, 4, 6, 8, 10, 12, 14, 16, 18]

def generaPares(limite): #Función generadora

    num=1

    while num<limite:
        yield num*2
        num+=1

devuelvePares = generaPares(10)

for i in devuelvePares:
    print(i)
print("")

def generaPares(limite): #Función generadora

    num=1

    while num<limite:
        yield num*2
        num+=1

devuelvePares = generaPares(10)

print(next(devuelvePares))
print("Aquí pordría haber más código")
print(next(devuelvePares))
print("Aquí pordría haber más código")
print(next(devuelvePares))
print("Aquí pordría haber más código")
