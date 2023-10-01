import math

def calculaRaiz(num1):
    if num1<0:
        raise ValueError("El número en una raiz cuadrada no puede ser negativo")
    else:
        return math.sqrt(num1)
    
op1=(int(input("Introduce un número: ")))

try:
    print(calculaRaiz(op1))
    
except ValueError as ErrorDeNumeroNegativo: #as le da un alias la excepción con el nombre que tú quieras darle.
    print(ErrorDeNumeroNegativo)

print("Programa finalizado")

