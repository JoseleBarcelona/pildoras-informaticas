nombreUsuario=input("Introduce tu número de usuario:\n")
print("El nombre es ", nombreUsuario.upper())
print("El nombre es ", nombreUsuario.capitalize())

edad=input("Introduce la edad:\n")

while(edad.isdigit()==False):
    print("Por favor, introduzca un valor numérico")
    edad=input("Introduce la edad:\n")

if (int(edad)<18):
    print("No puede pasar")
else:
    print("Puede pasar")
