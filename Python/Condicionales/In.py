print("ASIGNATURAS OPTATIVAS 2023")
print("Asignaturas optativas: Informática gráfica - Pruebas de software - Usabilidad y accesibilidad")

opcion = input("Escribe la asignatura escogida: ")
asignatura = opcion.lower() #Esto te convierte el texto en minúsculas

if asignatura in ("informática gráfica", "pruebas de software", "usabilidad y accesibilidad"):
    print("La asignatura elegida es " + asignatura)
else:
    print("La asignatura escogida no está contemplada este año")

