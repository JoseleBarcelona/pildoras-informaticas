print("PROGRAMA DE BECAS 2023")
distancia_escuela = int(input("Introduce la distancia en km: "))

numero_hermanos = int(input("Introduce el número de hermanos en el centro: "))

salario_familiar = int(input("Introduce salario anual bruto: "))

if distancia_escuela >= 40 and numero_hermanos >= 2 or salario_familiar <= 20000:

    print("Tienes derecho a beca")

else:
    print("No tienes derecho a beca")
