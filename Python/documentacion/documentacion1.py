
def areaCuadrado(lado):
    """Esta función calcula el área de un cuadrado
    elevando al cuadrado el lado pasado por parámetro"""

    return "El área del cuadrado es: " + str(lado*lado)

def areaTriangulo(base, altura):
    """Esta función calcula el área de un triángulo
     utilizando los parámetros base y altura"""

    return "El área del triángulo es:" + str((base*altura)/2)

print(areaCuadrado(3))
print(areaTriangulo(5,3))
print(areaCuadrado.__doc__) #Esto imprime la documentación asociada a dicha función
print('')
help(areaCuadrado)
#help() esta función nos imprime información detallada de la documentación asociada a dicha función
help(areaTriangulo)


# El área del cuadrado es: 9
# El área del triángulo es:7.5
# Esta función calcula el área de un cuadrado
#     elevando al cuadrado el lado pasado por parámetro
#
# Help on function areaCuadrado in module __main__:
#
# areaCuadrado(lado)
#     Esta función calcula el área de un cuadrado
#     elevando al cuadrado el lado pasado por parámetro
#
# Help on function areaTriangulo in module __main__:
#
# areaTriangulo(base, altura)
#     Esta función calcula el área de un triángulo
#     utilizando los parámetros base y altura