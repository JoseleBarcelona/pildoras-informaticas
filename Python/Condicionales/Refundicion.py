#input()recibe texto, por lo que hay que refundirlo int(input())
#en python un print no concatena texto con enteros, por lo que hay que pasarlo a texto str() en este ejemplo
#en cambio necesitamos en los comparadores en este ejemplo salariox<salrioy<...etc sean enteros para que funcione


salario_presidente = int(input("Introduce salario Presidente\n"))
print("Salario presidente " + str(salario_presidente) + "eur")

salario_director = int(input("Introduce salario Director\n"))
print("Salario director " + str(salario_director) + "eur")

salario_jefe_area = int(input("Introduce salario Jefe Area\n"))
print("Salario jefe area " + str(salario_jefe_area) + "eur")

salario_administrativo = int(input("Introduce salario Administrativo\n"))
print("Salario administrativo " + str(salario_administrativo) + "eur")

if salario_administrativo<salario_jefe_area<salario_director<salario_presidente:
    print("\nLos salarios son equitativos al cargo")
else:
    print("\nAlgo huele mal en la empresa")


