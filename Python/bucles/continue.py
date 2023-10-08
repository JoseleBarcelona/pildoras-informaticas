for letra in "Python":
    if letra == "h" or letra == "o":
        continue
    print("Viendo la letra " + letra)
print("")

nombre = "Pildoras Informaticas"
print("La frase con espacios tiene " + str(len(nombre)) + " caracteres")  # cuenta 21 caracteres de la longitud del texto, porque se cuentan los espacios en blanco
print("")

nombre = "Pildoras Informaticas"
contador = 0

for i in nombre:
    if i == " ":
        continue  # aquí cuanta 20 caracteres porque al llegar al continue, vuelve a la siguiente iteración sin continuar con el cuerpo del condicional
    contador += 1

print("La frase sin espacios tiene " + str(contador) + " caracteres")

# Viendo la letra P
# Viendo la letra y
# Viendo la letra t
# Viendo la letra n
#
# La frase con espacios tiene 21 caracteres
#
# La frase sin espacios tiene 20 caracteres

