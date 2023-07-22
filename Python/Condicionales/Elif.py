print("Verificación de acceso")

edad_usuario = int(input("Introduce tu edad, por favor\n"))

if edad_usuario<=0:
    print("La edad es incorrecta")
elif edad_usuario<18:
    print("La entrada no le está permitida")
elif edad_usuario>100:
    print("La edad es incorrecta")
else:
    print("Puede pasar")
