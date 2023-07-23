
i = 1

while i <=5:
    print("Ejecución" + str(i))
    i = i+1
print("")

edad = int(input("Introduzca su edad: "))

while edad<5 or edad>100:
    print("Has introducido una edad incorrecta, vuelva a intentarlo")
    edad = int(input("Introduzca su edad: "))

print("Gracias por colaborar, puede pasar")
print("Edad del aspirante " + str(edad) + " años")

'''
Ejecución1
Ejecución2
Ejecución3
Ejecución4
Ejecución5

Introduzca su edad: -8
Has introducido una edad incorrecta, vuelva a intentarlo
Introduzca su edad: 142
Has introducido una edad incorrecta, vuelva a intentarlo
Introduzca su edad: 18
Gracias por colaborar, puede pasar
Edad del aspirante 18 años

Process finished with exit code 0'''