for letra in "Python":
    if letra == "h" or letra =="o":
        continue
    print("Viendo la letra " + letra)
print("")

nombre = "Pildoras Informaticas"
print(len(nombre)) #cuenta 21 caracteres de la longitud del texto, porque se cuentan los espacios en blanco
print("")

nombre = "Pildoras Informaticas"
contador = 0

for i in nombre:
    if i == " ":
        continue #aquí cuanta 20 caracteres porque al llegar al continue, vuelve a la siguiente iteración sin continuar con el cuerpo del condicional
    contador+=1

print(contador)

'''
Viendo la letra P
Viendo la letra y
Viendo la letra t
Viendo la letra n

21

20'''