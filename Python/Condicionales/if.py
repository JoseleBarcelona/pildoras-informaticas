print("CALIFICACIONES GLOBALES")

nota_alumno = int(input("Introduce la nota obtenida\n"))

#Cualquier valor introducido a través de un input, es considerado texto
#por eso hay que hacer una refundición o casting para convertirlo a valor numérico

def evaluacion(nota):
    valoracion = "Estás aprobado"
    if nota < 5:
        valoracion = "Estás suspendido"
    return valoracion

print(evaluacion(nota_alumno))
