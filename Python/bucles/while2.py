import math

print("PROGRAMA DE CÁLCULO DE RAIZ CUADRADA")
numero = int(input("Introduzca un número: "))

intentos = 0

while numero<0:
    print("No se puede hallar la raiz de un número negativo")
    if intentos == 2:
        print("Has agotado el número de intentos, el programa ha finalizado")
        break

    numero = int(input("Introduzca un número: "))
    if numero<0:
        intentos = intentos+1

if intentos<2:
    solucion = math.sqrt(numero)
    print("La raiz cuadrada de " + str(numero) + " es " + str(solucion))

'''
PROGRAMA DE CÁLCULO DE RAIZ CUADRADA
Introduzca un número: -4
No se puede hallar la raiz de un número negativo
Introduzca un número: -5
No se puede hallar la raiz de un número negativo
Introduzca un número: -8
No se puede hallar la raiz de un número negativo
Has agotado el número de intentos, el programa ha finalizado'''