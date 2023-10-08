for i in range(5):
    print(i)
print("")
for i in range(5):
    print("Valor de la variable {i}")
print("")
for i in range(5):
    print(f"Valor de la variable {i}") #con la f le decimos a python que concatene texto con variables
print("")
for i in range(20, 25):#hace listas desde un número inicial a uno final
    print(f"Valor de la variable {i}")
print("")
for i in range(5, 20, 3):#el tercer argumento indica de cuanto en cuanto tiene que ir el conteo
    print(f"Valor de la variable {i}")
#Otra manera de comprobar si un email es correcto usando len() y range()

email = False
miEmail = input("Introduce tu dirección de e-mail: ")
for i in range(len(miEmail)):
    if miEmail[i] == '@' and '.' in miEmail:

        email = True

if email == True:
    print("email correcto")
else:
    print("email incorrecto")


# 0
# 1
# 2
# 3
# 4

# Valor de la variable {i}
# Valor de la variable {i}
# Valor de la variable {i}
# Valor de la variable {i}
# Valor de la variable {i}

# Valor de la variable 0
# Valor de la variable 1
# Valor de la variable 2
# Valor de la variable 3
# Valor de la variable 4

# Valor de la variable 20
# Valor de la variable 21
# Valor de la variable 22
# Valor de la variable 23
# Valor de la variable 24

# Valor de la variable 5
# Valor de la variable 8
# Valor de la variable 11
# Valor de la variable 14
# Valor de la variable 17
# Introduce tu dirección de e-mail: josele@gmail.com
# email correcto

